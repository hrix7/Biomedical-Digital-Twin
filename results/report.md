# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "baseline_holdout_rmse_mmHg": 16.117107991225073,
  "calibration_rmse_mmHg": 1.0474004766192089,
  "estimated_C": 1.5,
  "estimated_R": 1.2,
  "holdout_rmse_vs_observed_mmHg": 0.9798338973871292,
  "holdout_rmse_vs_synthetic_truth_mmHg": 0.0,
  "interpretation": "Synthetic parameter recovery within the same generating model; no patient-specific or clinical validation.",
  "sensitivity": {
    "R_multiplier_0.8": 19.074083575700307,
    "R_multiplier_1": 0.0,
    "R_multiplier_1.2": 18.711469414905494
  }
}
```

Result SHA-256: `464a463017ba729f02da19422f9fb430fd213135f5acf1f20dc54d1b1afa7ff0`
