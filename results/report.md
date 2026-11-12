# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "baseline_holdout_rmse_mmHg": 16.11710799122507,
  "calibration_rmse_mmHg": 1.0474004766192089,
  "estimated_C": 1.5,
  "estimated_R": 1.2,
  "holdout_rmse_vs_observed_mmHg": 0.9798338973871292,
  "holdout_rmse_vs_synthetic_truth_mmHg": 0.0,
  "interpretation": "Synthetic parameter recovery within the same generating model; no patient-specific or clinical validation.",
  "sensitivity": {
    "R_multiplier_0.8": 19.074083575699877,
    "R_multiplier_1": 0.0,
    "R_multiplier_1.2": 18.711469414905515
  }
}
```

Result SHA-256: `8c1e9048e5771e9aae308c4c09bfcdd3d95218f6c4964ac80b856e21c9fb27b2`
