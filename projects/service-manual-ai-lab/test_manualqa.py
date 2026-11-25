import copy
import unittest

from evaluate import evaluate
from manualqa import audit_translation, build_workflow, find_manual, load_data


class ManualWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.data = load_data()
        self.workflow = build_workflow(self.data)

    def test_regression_questions_and_verbatim_citations(self):
        results = evaluate(self.data)
        for row in results["cases"]:
            with self.subTest(case=row["case"]):
                self.assertTrue(row["guarded_correct"])
                if row["expected_revision"]:
                    manual = find_manual(self.data["manuals"], row["asset"], row["expected_revision"])
                    expected_quote = next(s["text"] for s in manual["sections"] if s["id"] == row["expected_section"])
                    self.assertEqual(row["guarded_response"]["quote"], expected_quote)

    def test_competing_released_revision_defers(self):
        competing = copy.deepcopy(find_manual(self.data["manuals"], "Atlas A1", "1.4"))
        competing["revision"] = "9.0"
        self.data["manuals"].append(competing)
        answer = build_workflow(self.data).invoke({"operation": "ask", "asset": "Atlas A1", "question": "Retry interval"})
        self.assertEqual(answer["result"]["status"], "defer")
        self.assertNotIn("quote", answer["result"])

    def test_manual_flags_have_specific_evidence(self):
        answer = self.workflow.invoke({"operation": "audit", "asset": "Atlas A1", "revision": "1.5"})
        self.assertEqual(answer["result"]["status"], "revise")
        self.assertEqual(answer["result"]["findings"], [
            "missing section: export", "duplicate section: retry",
            "unresolved drafting marker: retry at position 2",
            "nonstandard term: escalation uses 'sync key'; glossary uses 'sync token'",
        ])

    def test_released_manual_passes_limited_checks(self):
        answer = self.workflow.invoke({"operation": "audit", "asset": "Atlas A1", "revision": "1.4"})
        self.assertEqual(answer["result"], {"status": "checks_passed", "findings": []})

    def test_clean_localization_still_requires_human_review(self):
        answer = self.workflow.invoke({"operation": "localize", "draft": "complete"})
        self.assertEqual(answer["result"]["status"], "human_review")
        self.assertEqual(answer["result"]["findings"], [])

    def test_localization_flags_specific_differences(self):
        answer = self.workflow.invoke({"operation": "localize", "draft": "altered"})
        self.assertEqual(answer["result"]["status"], "revise")
        self.assertEqual(set(answer["result"]["findings"]), {
            "section structure or order changed", "retry: values changed", "retry: durations changed", "export: codes changed",
            "escalation: values changed", "escalation: links changed", "escalation: variables changed",
            "escalation: glossary term missing",
        })

    def test_missing_and_duplicate_translation_sections_are_flagged(self):
        source = find_manual(self.data["manuals"], "Atlas A1", "1.4")["sections"]
        translation = copy.deepcopy(self.data["spanish_drafts"]["complete"])
        translation[-1] = translation[0]
        result = audit_translation(source, translation)
        self.assertIn("overview: missing or duplicated Spanish section", result["findings"])
        self.assertIn("escalation: missing or duplicated Spanish section", result["findings"])

    def test_duration_unit_change_is_flagged_even_if_the_number_stays(self):
        source = find_manual(self.data["manuals"], "Atlas A1", "1.4")["sections"]
        draft = copy.deepcopy(self.data["spanish_drafts"]["complete"])
        draft[1]["text"] = draft[1]["text"].replace("15 minutos", "15 segundos")
        self.assertEqual(audit_translation(source, draft)["findings"], ["retry: durations changed"])


if __name__ == "__main__":
    unittest.main()
