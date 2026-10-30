# Evaluation protocol

Run `python analytics/evaluate.py` only after creating alerts. It reads `ground_truth_outbreaks.csv` only for evaluation, never operational detection. Report sensitivity, false alerts per district-year, and median days to detection at thresholds 1, 1.5, 2, 2.5, 3 sigma. Forecasts use rolling-origin holdout over the final 52 weeks; report MAE and 80% interval coverage versus seasonal-naive. Compare allocation with population-proportional distribution on weighted unmet demand and minimum district share.

The committed demo is synthetic and deliberately small. Do not claim experimental values until the scale run is completed and logged.
