# Disaster dashboards need a history of published totals

Analysts need to know when a county spending comparison is stable enough to use. Estimating that waiting period requires dated snapshots of the same totals and a consistent population.

**Current state: the inspected source does not establish a usable snapshot history; no stability horizon has been estimated.**

The official [OpenFEMA metadata request](https://www.fema.gov/api/open/v1/OpenFemaDataSets?$filter=name%20eq%20%27PublicAssistanceFundedProjectsDetails%27), captured 30 October 2026, describes the current version-2 Public Assistance Funded Projects Details endpoint and current bulk distributions. Its description says pre-obligation projects are absent and warns that a system migration increased record counts after previously excluded records were incorporated. A count change can therefore include source-system corrections as well as newly obligated projects.

The inspected [API documentation](https://www.fema.gov/about/openfema/api) defines lastDataSetRefresh as the time a dataset reload completed; it explicitly does not establish that individual records changed. The field dictionary defines a record's lastRefresh as its last update in the API store. These timestamps do not supply the values that were visible at each earlier refresh.

A preserved dated archive may be useful, but its population, keys, financial definitions and capture date must be reconciled before comparison. This bounded check does not establish that no suitable archive exists. The next step is to verify repeated, comparable county-level snapshots or begin a dated collection under a separate execution plan. No historical values are reconstructed from today's totals. The original protocol and its data-availability alternative remain visible; the study is not counted as released.
