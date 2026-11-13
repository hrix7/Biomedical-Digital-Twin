# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "baseline_holdout_rmse_mmHg": 16.11710799122507,
  "calibration_best_on_grid_boundary": {
    "C": false,
    "R": false
  },
  "calibration_grid": [
    {
      "C": 1.5,
      "R": 1.2,
      "rmse_mmHg": 1.0474004766192089
    },
    {
      "C": 1.75,
      "R": 1.2,
      "rmse_mmHg": 1.4216915780279746
    },
    {
      "C": 1.25,
      "R": 1.2,
      "rmse_mmHg": 1.7736525772409026
    },
    {
      "C": 2,
      "R": 1.2,
      "rmse_mmHg": 2.116316420067338
    },
    {
      "C": 1,
      "R": 1.2,
      "rmse_mmHg": 3.424304175823109
    },
    {
      "C": 2,
      "R": 1.4,
      "rmse_mmHg": 8.98615655617239
    },
    {
      "C": 1.75,
      "R": 1.4,
      "rmse_mmHg": 10.065426529624908
    },
    {
      "C": 1.5,
      "R": 1.4,
      "rmse_mmHg": 11.30099384046493
    },
    {
      "C": 1.75,
      "R": 1,
      "rmse_mmHg": 12.33248388966636
    },
    {
      "C": 2,
      "R": 1,
      "rmse_mmHg": 12.342085431526593
    },
    {
      "C": 1.5,
      "R": 1,
      "rmse_mmHg": 12.373307418110056
    },
    {
      "C": 1.25,
      "R": 1,
      "rmse_mmHg": 12.516803665856276
    },
    {
      "C": 1.25,
      "R": 1.4,
      "rmse_mmHg": 12.721061649022133
    },
    {
      "C": 1,
      "R": 1,
      "rmse_mmHg": 12.889979747224093
    },
    {
      "C": 1,
      "R": 1.4,
      "rmse_mmHg": 14.399182158428248
    },
    {
      "C": 2,
      "R": 1.6,
      "rmse_mmHg": 17.44068402817939
    },
    {
      "C": 1.75,
      "R": 1.6,
      "rmse_mmHg": 19.270475582025632
    },
    {
      "C": 1.5,
      "R": 1.6,
      "rmse_mmHg": 21.32040473532254
    },
    {
      "C": 1.25,
      "R": 1.6,
      "rmse_mmHg": 23.612128540345257
    },
    {
      "C": 2,
      "R": 0.8,
      "rmse_mmHg": 25.121561453096515
    },
    {
      "C": 1.75,
      "R": 0.8,
      "rmse_mmHg": 25.586786104005952
    },
    {
      "C": 1.5,
      "R": 0.8,
      "rmse_mmHg": 26.084351731530308
    },
    {
      "C": 1,
      "R": 1.6,
      "rmse_mmHg": 26.178137083428645
    },
    {
      "C": 1.25,
      "R": 0.8,
      "rmse_mmHg": 26.629947433690422
    },
    {
      "C": 1,
      "R": 0.8,
      "rmse_mmHg": 27.272586433986394
    }
  ],
  "calibration_rmse_mmHg": 1.0474004766192089,
  "calibration_runner_up_gap_mmHg": 0.37429110140876576,
  "estimated_C": 1.5,
  "estimated_R": 1.2,
  "grid_interpretation": "Calibration-only loss surface, not a confidence region or proof of identifiability; holdout values do not select parameters.",
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

Result SHA-256: `485940255b0c5d617d7000991962252c3bdf8c3f4a6045044299a34167c7a315`
