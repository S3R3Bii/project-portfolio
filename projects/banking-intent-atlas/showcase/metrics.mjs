// Replay recorded outcomes; never fit or change a model from the explorer.
export function summarize(rows, model, threshold) {
  const p = model === 'semantic' ? 4 : 2;
  let accepted = 0, errors = 0;
  for (const row of rows) if (row[p + 1] >= threshold) { accepted++; errors += +(row[p] !== row[1]); }
  const rate = accepted ? errors / accepted : null;
  let interval = null;
  if (accepted) {
    const z = 1.959963984540054, d = 1 + z*z/accepted;
    const center = (rate + z*z/(2*accepted))/d;
    const half = z*Math.sqrt(rate*(1-rate)/accepted+z*z/(4*accepted*accepted))/d;
    interval = [center-half, center+half];
  }
  return {accepted, errors, rate, interval, coverage:accepted/rows.length, review:rows.length-accepted};
}
export function curve(rows, model) {
  return Array.from({length:101},(_,i)=>summarize(rows,model,i/100)).filter(x=>x.accepted>=100);
}
