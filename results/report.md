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
  "calibration_bias_probe": {
    "cases": [
      {
        "calibration_rmse_mmHg": 1.3560125505983607,
        "estimated_C": 1.75,
        "estimated_R": 1.2,
        "offset_mmHg": -1.0
      },
      {
        "calibration_rmse_mmHg": 1.0474004766192089,
        "estimated_C": 1.5,
        "estimated_R": 1.2,
        "offset_mmHg": 0.0
      },
      {
        "calibration_rmse_mmHg": 1.375363954318434,
        "estimated_C": 1.5,
        "estimated_R": 1.2,
        "offset_mmHg": 1.0
      }
    ],
    "method": "Predeclared additive calibration-observation offsets -1, 0, +1 mmHg; refit the same finite grid using calibration inputs only. A systematic-bias sensitivity probe, not bootstrap uncertainty, a confidence region or patient sensor validation. Holdout observations do not select parameters."
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
      "rmse_mmHg": 12.516803665856278
    },
    {
      "C": 1.25,
      "R": 1.4,
      "rmse_mmHg": 12.721061649022133
    },
    {
      "C": 1,
      "R": 1,
      "rmse_mmHg": 12.889979747224091
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
      "rmse_mmHg": 23.612128540345253
    },
    {
      "C": 2,
      "R": 0.8,
      "rmse_mmHg": 25.12156145309652
    },
    {
      "C": 1.75,
      "R": 0.8,
      "rmse_mmHg": 25.586786104005952
    },
    {
      "C": 1.5,
      "R": 0.8,
      "rmse_mmHg": 26.08435173153031
    },
    {
      "C": 1,
      "R": 1.6,
      "rmse_mmHg": 26.17813708342865
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
  "calibration_profiles": {
    "C": [
      {
        "minimum_rmse_mmHg": 3.424304175823109,
        "value": 1
      },
      {
        "minimum_rmse_mmHg": 1.7736525772409026,
        "value": 1.25
      },
      {
        "minimum_rmse_mmHg": 1.0474004766192089,
        "value": 1.5
      },
      {
        "minimum_rmse_mmHg": 1.4216915780279746,
        "value": 1.75
      },
      {
        "minimum_rmse_mmHg": 2.116316420067338,
        "value": 2
      }
    ],
    "R": [
      {
        "minimum_rmse_mmHg": 25.12156145309652,
        "value": 0.8
      },
      {
        "minimum_rmse_mmHg": 12.33248388966636,
        "value": 1
      },
      {
        "minimum_rmse_mmHg": 1.0474004766192089,
        "value": 1.2
      },
      {
        "minimum_rmse_mmHg": 8.98615655617239,
        "value": 1.4
      },
      {
        "minimum_rmse_mmHg": 17.44068402817939,
        "value": 1.6
      }
    ]
  },
  "calibration_residual_diagnostics": {
    "centered_lag1_ratio": -0.06428369095509595,
    "mean_observed_minus_predicted_mmHg": -0.1027108757918534,
    "method": "Calibration observations only, after fitting. Lag-1 adjacent centered products divided by total centered sum of squares; null for constant residuals. Descriptive diagnostic, not an independence/normality test or permission to bootstrap; no holdout fitting or statistical uncertainty claim.",
    "rmse_mmHg": 1.0474004766192089,
    "samples": 300
  },
  "calibration_rmse_mmHg": 1.0474004766192089,
  "calibration_runner_up_gap_mmHg": 0.37429110140876576,
  "estimated_C": 1.5,
  "estimated_R": 1.2,
  "forcing_step_probe": {
    "flow_after_mL_s": 100,
    "flow_before_mL_s": 0,
    "initial_pressure_mmHg": 80,
    "interpretation": "Separate deterministic zero-to-constant-flow probe with an independent two-phase closed form; same ideal model, not physiological or patient validation.",
    "max_abs_error_mmHg": 1.5631940186722204e-13,
    "phase_samples": 50,
    "samples": [
      {
        "closed_form_mmHg": 79.11603114351378,
        "flow_mL_s": 0,
        "pressure_mmHg": 79.11603114351378,
        "time_seconds": 0.02
      },
      {
        "closed_form_mmHg": 78.24182979876804,
        "flow_mL_s": 0,
        "pressure_mmHg": 78.24182979876804,
        "time_seconds": 0.04
      },
      {
        "closed_form_mmHg": 77.37728803856047,
        "flow_mL_s": 0,
        "pressure_mmHg": 77.37728803856047,
        "time_seconds": 0.06
      },
      {
        "closed_form_mmHg": 76.52229912824234,
        "flow_mL_s": 0,
        "pressure_mmHg": 76.52229912824232,
        "time_seconds": 0.08
      },
      {
        "closed_form_mmHg": 75.67675751254123,
        "flow_mL_s": 0,
        "pressure_mmHg": 75.67675751254122,
        "time_seconds": 0.1
      },
      {
        "closed_form_mmHg": 74.84055880252942,
        "flow_mL_s": 0,
        "pressure_mmHg": 74.8405588025294,
        "time_seconds": 0.12
      },
      {
        "closed_form_mmHg": 74.01359976273615,
        "flow_mL_s": 0,
        "pressure_mmHg": 74.01359976273613,
        "time_seconds": 0.14
      },
      {
        "closed_form_mmHg": 73.19577829840247,
        "flow_mL_s": 0,
        "pressure_mmHg": 73.19577829840246,
        "time_seconds": 0.16
      },
      {
        "closed_form_mmHg": 72.38699344287676,
        "flow_mL_s": 0,
        "pressure_mmHg": 72.38699344287674,
        "time_seconds": 0.18
      },
      {
        "closed_form_mmHg": 71.58714534514958,
        "flow_mL_s": 0,
        "pressure_mmHg": 71.58714534514955,
        "time_seconds": 0.2
      },
      {
        "closed_form_mmHg": 70.79613525752629,
        "flow_mL_s": 0,
        "pressure_mmHg": 70.79613525752625,
        "time_seconds": 0.22
      },
      {
        "closed_form_mmHg": 70.0138655234358,
        "flow_mL_s": 0,
        "pressure_mmHg": 70.01386552343575,
        "time_seconds": 0.24
      },
      {
        "closed_form_mmHg": 69.24023956537415,
        "flow_mL_s": 0,
        "pressure_mmHg": 69.24023956537411,
        "time_seconds": 0.26
      },
      {
        "closed_form_mmHg": 68.47516187298122,
        "flow_mL_s": 0,
        "pressure_mmHg": 68.47516187298118,
        "time_seconds": 0.28
      },
      {
        "closed_form_mmHg": 67.71853799124912,
        "flow_mL_s": 0,
        "pressure_mmHg": 67.71853799124908,
        "time_seconds": 0.3
      },
      {
        "closed_form_mmHg": 66.9702745088611,
        "flow_mL_s": 0,
        "pressure_mmHg": 66.97027450886104,
        "time_seconds": 0.32
      },
      {
        "closed_form_mmHg": 66.23027904665902,
        "flow_mL_s": 0,
        "pressure_mmHg": 66.23027904665896,
        "time_seconds": 0.34
      },
      {
        "closed_form_mmHg": 65.49846024623855,
        "flow_mL_s": 0,
        "pressure_mmHg": 65.4984602462385,
        "time_seconds": 0.36
      },
      {
        "closed_form_mmHg": 64.77472775867011,
        "flow_mL_s": 0,
        "pressure_mmHg": 64.77472775867005,
        "time_seconds": 0.38
      },
      {
        "closed_form_mmHg": 64.05899223334464,
        "flow_mL_s": 0,
        "pressure_mmHg": 64.05899223334458,
        "time_seconds": 0.4
      },
      {
        "closed_form_mmHg": 63.351165306942534,
        "flow_mL_s": 0,
        "pressure_mmHg": 63.35116530694247,
        "time_seconds": 0.42
      },
      {
        "closed_form_mmHg": 62.651159592524444,
        "flow_mL_s": 0,
        "pressure_mmHg": 62.65115959252438,
        "time_seconds": 0.44
      },
      {
        "closed_form_mmHg": 61.9588886687427,
        "flow_mL_s": 0,
        "pressure_mmHg": 61.95888866874264,
        "time_seconds": 0.46
      },
      {
        "closed_form_mmHg": 61.2742670691719,
        "flow_mL_s": 0,
        "pressure_mmHg": 61.27426706917183,
        "time_seconds": 0.48
      },
      {
        "closed_form_mmHg": 60.59721027175732,
        "flow_mL_s": 0,
        "pressure_mmHg": 60.59721027175724,
        "time_seconds": 0.5
      },
      {
        "closed_form_mmHg": 59.92763468838006,
        "flow_mL_s": 0,
        "pressure_mmHg": 59.92763468837999,
        "time_seconds": 0.52
      },
      {
        "closed_form_mmHg": 59.26545765453743,
        "flow_mL_s": 0,
        "pressure_mmHg": 59.26545765453735,
        "time_seconds": 0.54
      },
      {
        "closed_form_mmHg": 58.610597419137264,
        "flow_mL_s": 0,
        "pressure_mmHg": 58.61059741913718,
        "time_seconds": 0.56
      },
      {
        "closed_form_mmHg": 57.96297313440515,
        "flow_mL_s": 0,
        "pressure_mmHg": 57.96297313440507,
        "time_seconds": 0.58
      },
      {
        "closed_form_mmHg": 57.32250484590314,
        "flow_mL_s": 0,
        "pressure_mmHg": 57.322504845903055,
        "time_seconds": 0.6
      },
      {
        "closed_form_mmHg": 56.689113482658655,
        "flow_mL_s": 0,
        "pressure_mmHg": 56.68911348265858,
        "time_seconds": 0.62
      },
      {
        "closed_form_mmHg": 56.06272084740262,
        "flow_mL_s": 0,
        "pressure_mmHg": 56.06272084740254,
        "time_seconds": 0.64
      },
      {
        "closed_form_mmHg": 55.44324960691532,
        "flow_mL_s": 0,
        "pressure_mmHg": 55.44324960691524,
        "time_seconds": 0.66
      },
      {
        "closed_form_mmHg": 54.83062328247901,
        "flow_mL_s": 0,
        "pressure_mmHg": 54.83062328247893,
        "time_seconds": 0.68
      },
      {
        "closed_form_mmHg": 54.224766240436026,
        "flow_mL_s": 0,
        "pressure_mmHg": 54.22476624043594,
        "time_seconds": 0.7000000000000001
      },
      {
        "closed_form_mmHg": 53.62560368285115,
        "flow_mL_s": 0,
        "pressure_mmHg": 53.62560368285106,
        "time_seconds": 0.72
      },
      {
        "closed_form_mmHg": 53.03306163827723,
        "flow_mL_s": 0,
        "pressure_mmHg": 53.03306163827715,
        "time_seconds": 0.74
      },
      {
        "closed_form_mmHg": 52.44706695262285,
        "flow_mL_s": 0,
        "pressure_mmHg": 52.44706695262276,
        "time_seconds": 0.76
      },
      {
        "closed_form_mmHg": 51.867547280120775,
        "flow_mL_s": 0,
        "pressure_mmHg": 51.86754728012069,
        "time_seconds": 0.78
      },
      {
        "closed_form_mmHg": 51.29443107439636,
        "flow_mL_s": 0,
        "pressure_mmHg": 51.29443107439628,
        "time_seconds": 0.8
      },
      {
        "closed_form_mmHg": 50.72764757963455,
        "flow_mL_s": 0,
        "pressure_mmHg": 50.727647579634464,
        "time_seconds": 0.8200000000000001
      },
      {
        "closed_form_mmHg": 50.167126821844484,
        "flow_mL_s": 0,
        "pressure_mmHg": 50.1671268218444,
        "time_seconds": 0.84
      },
      {
        "closed_form_mmHg": 49.61279960022068,
        "flow_mL_s": 0,
        "pressure_mmHg": 49.61279960022059,
        "time_seconds": 0.86
      },
      {
        "closed_form_mmHg": 49.064597478599595,
        "flow_mL_s": 0,
        "pressure_mmHg": 49.06459747859951,
        "time_seconds": 0.88
      },
      {
        "closed_form_mmHg": 48.52245277701066,
        "flow_mL_s": 0,
        "pressure_mmHg": 48.522452777010585,
        "time_seconds": 0.9
      },
      {
        "closed_form_mmHg": 47.986298563320666,
        "flow_mL_s": 0,
        "pressure_mmHg": 47.98629856332058,
        "time_seconds": 0.92
      },
      {
        "closed_form_mmHg": 47.45606864497036,
        "flow_mL_s": 0,
        "pressure_mmHg": 47.45606864497027,
        "time_seconds": 0.9400000000000001
      },
      {
        "closed_form_mmHg": 46.93169756080255,
        "flow_mL_s": 0,
        "pressure_mmHg": 46.931697560802455,
        "time_seconds": 0.96
      },
      {
        "closed_form_mmHg": 46.4131205729803,
        "flow_mL_s": 0,
        "pressure_mmHg": 46.41312057298021,
        "time_seconds": 0.98
      },
      {
        "closed_form_mmHg": 45.90027365899462,
        "flow_mL_s": 0,
        "pressure_mmHg": 45.900273658994536,
        "time_seconds": 1.0
      },
      {
        "closed_form_mmHg": 46.71904678848962,
        "flow_mL_s": 100,
        "pressure_mmHg": 46.71904678848953,
        "time_seconds": 1.02
      },
      {
        "closed_form_mmHg": 47.52877279364711,
        "flow_mL_s": 100,
        "pressure_mmHg": 47.52877279364701,
        "time_seconds": 1.04
      },
      {
        "closed_form_mmHg": 48.329551641669,
        "flow_mL_s": 100,
        "pressure_mmHg": 48.32955164166891,
        "time_seconds": 1.06
      },
      {
        "closed_form_mmHg": 49.121482195158606,
        "flow_mL_s": 100,
        "pressure_mmHg": 49.12148219515851,
        "time_seconds": 1.08
      },
      {
        "closed_form_mmHg": 49.90466222432589,
        "flow_mL_s": 100,
        "pressure_mmHg": 49.9046622243258,
        "time_seconds": 1.1
      },
      {
        "closed_form_mmHg": 50.67918841905812,
        "flow_mL_s": 100,
        "pressure_mmHg": 50.679188419058015,
        "time_seconds": 1.12
      },
      {
        "closed_form_mmHg": 51.44515640085689,
        "flow_mL_s": 100,
        "pressure_mmHg": 51.44515640085678,
        "time_seconds": 1.1400000000000001
      },
      {
        "closed_form_mmHg": 52.202660734643445,
        "flow_mL_s": 100,
        "pressure_mmHg": 52.20266073464335,
        "time_seconds": 1.16
      },
      {
        "closed_form_mmHg": 52.9517949404335,
        "flow_mL_s": 100,
        "pressure_mmHg": 52.95179494043341,
        "time_seconds": 1.18
      },
      {
        "closed_form_mmHg": 53.69265150488299,
        "flow_mL_s": 100,
        "pressure_mmHg": 53.69265150488288,
        "time_seconds": 1.2
      },
      {
        "closed_form_mmHg": 54.42532189270625,
        "flow_mL_s": 100,
        "pressure_mmHg": 54.425321892706144,
        "time_seconds": 1.22
      },
      {
        "closed_form_mmHg": 55.149896557968205,
        "flow_mL_s": 100,
        "pressure_mmHg": 55.14989655796809,
        "time_seconds": 1.24
      },
      {
        "closed_form_mmHg": 55.86646495525153,
        "flow_mL_s": 100,
        "pressure_mmHg": 55.86646495525141,
        "time_seconds": 1.26
      },
      {
        "closed_form_mmHg": 56.57511555070058,
        "flow_mL_s": 100,
        "pressure_mmHg": 56.57511555070047,
        "time_seconds": 1.28
      },
      {
        "closed_form_mmHg": 57.2759358329433,
        "flow_mL_s": 100,
        "pressure_mmHg": 57.27593583294318,
        "time_seconds": 1.3
      },
      {
        "closed_form_mmHg": 57.96901232389231,
        "flow_mL_s": 100,
        "pressure_mmHg": 57.969012323892194,
        "time_seconds": 1.32
      },
      {
        "closed_form_mmHg": 58.6544305894268,
        "flow_mL_s": 100,
        "pressure_mmHg": 58.65443058942668,
        "time_seconds": 1.34
      },
      {
        "closed_form_mmHg": 59.3322752499563,
        "flow_mL_s": 100,
        "pressure_mmHg": 59.332275249956176,
        "time_seconds": 1.36
      },
      {
        "closed_form_mmHg": 60.00262999086776,
        "flow_mL_s": 100,
        "pressure_mmHg": 60.002629990867625,
        "time_seconds": 1.3800000000000001
      },
      {
        "closed_form_mmHg": 60.66557757285717,
        "flow_mL_s": 100,
        "pressure_mmHg": 60.66557757285703,
        "time_seconds": 1.4000000000000001
      },
      {
        "closed_form_mmHg": 61.32119984214705,
        "flow_mL_s": 100,
        "pressure_mmHg": 61.32119984214692,
        "time_seconds": 1.42
      },
      {
        "closed_form_mmHg": 61.969577740591056,
        "flow_mL_s": 100,
        "pressure_mmHg": 61.96957774059092,
        "time_seconds": 1.44
      },
      {
        "closed_form_mmHg": 62.61079131566682,
        "flow_mL_s": 100,
        "pressure_mmHg": 62.61079131566669,
        "time_seconds": 1.46
      },
      {
        "closed_form_mmHg": 63.24491973035856,
        "flow_mL_s": 100,
        "pressure_mmHg": 63.24491973035842,
        "time_seconds": 1.48
      },
      {
        "closed_form_mmHg": 63.87204127293028,
        "flow_mL_s": 100,
        "pressure_mmHg": 63.87204127293014,
        "time_seconds": 1.5
      },
      {
        "closed_form_mmHg": 64.49223336659121,
        "flow_mL_s": 100,
        "pressure_mmHg": 64.49223336659105,
        "time_seconds": 1.52
      },
      {
        "closed_form_mmHg": 65.10557257905418,
        "flow_mL_s": 100,
        "pressure_mmHg": 65.10557257905403,
        "time_seconds": 1.54
      },
      {
        "closed_form_mmHg": 65.71213463198866,
        "flow_mL_s": 100,
        "pressure_mmHg": 65.71213463198852,
        "time_seconds": 1.56
      },
      {
        "closed_form_mmHg": 66.31199441036914,
        "flow_mL_s": 100,
        "pressure_mmHg": 66.31199441036901,
        "time_seconds": 1.58
      },
      {
        "closed_form_mmHg": 66.90522597172028,
        "flow_mL_s": 100,
        "pressure_mmHg": 66.90522597172016,
        "time_seconds": 1.6
      },
      {
        "closed_form_mmHg": 67.49190255525994,
        "flow_mL_s": 100,
        "pressure_mmHg": 67.49190255525981,
        "time_seconds": 1.62
      },
      {
        "closed_form_mmHg": 68.07209659094111,
        "flow_mL_s": 100,
        "pressure_mmHg": 68.07209659094099,
        "time_seconds": 1.6400000000000001
      },
      {
        "closed_form_mmHg": 68.645879708394,
        "flow_mL_s": 100,
        "pressure_mmHg": 68.64587970839389,
        "time_seconds": 1.6600000000000001
      },
      {
        "closed_form_mmHg": 69.21332274576935,
        "flow_mL_s": 100,
        "pressure_mmHg": 69.21332274576922,
        "time_seconds": 1.68
      },
      {
        "closed_form_mmHg": 69.7744957584838,
        "flow_mL_s": 100,
        "pressure_mmHg": 69.77449575848368,
        "time_seconds": 1.7
      },
      {
        "closed_form_mmHg": 70.329468027869,
        "flow_mL_s": 100,
        "pressure_mmHg": 70.32946802786888,
        "time_seconds": 1.72
      },
      {
        "closed_form_mmHg": 70.87830806972484,
        "flow_mL_s": 100,
        "pressure_mmHg": 70.87830806972472,
        "time_seconds": 1.74
      },
      {
        "closed_form_mmHg": 71.42108364277826,
        "flow_mL_s": 100,
        "pressure_mmHg": 71.42108364277814,
        "time_seconds": 1.76
      },
      {
        "closed_form_mmHg": 71.95786175704865,
        "flow_mL_s": 100,
        "pressure_mmHg": 71.95786175704856,
        "time_seconds": 1.78
      },
      {
        "closed_form_mmHg": 72.48870868212083,
        "flow_mL_s": 100,
        "pressure_mmHg": 72.48870868212074,
        "time_seconds": 1.8
      },
      {
        "closed_form_mmHg": 73.01368995532644,
        "flow_mL_s": 100,
        "pressure_mmHg": 73.01368995532636,
        "time_seconds": 1.82
      },
      {
        "closed_form_mmHg": 73.53287038983515,
        "flow_mL_s": 100,
        "pressure_mmHg": 73.53287038983507,
        "time_seconds": 1.84
      },
      {
        "closed_form_mmHg": 74.04631408265634,
        "flow_mL_s": 100,
        "pressure_mmHg": 74.04631408265625,
        "time_seconds": 1.86
      },
      {
        "closed_form_mmHg": 74.55408442255234,
        "flow_mL_s": 100,
        "pressure_mmHg": 74.55408442255226,
        "time_seconds": 1.8800000000000001
      },
      {
        "closed_form_mmHg": 75.05624409786441,
        "flow_mL_s": 100,
        "pressure_mmHg": 75.05624409786434,
        "time_seconds": 1.9000000000000001
      },
      {
        "closed_form_mmHg": 75.55285510425199,
        "flow_mL_s": 100,
        "pressure_mmHg": 75.55285510425192,
        "time_seconds": 1.92
      },
      {
        "closed_form_mmHg": 76.04397875234662,
        "flow_mL_s": 100,
        "pressure_mmHg": 76.04397875234656,
        "time_seconds": 1.94
      },
      {
        "closed_form_mmHg": 76.52967567532127,
        "flow_mL_s": 100,
        "pressure_mmHg": 76.52967567532122,
        "time_seconds": 1.96
      },
      {
        "closed_form_mmHg": 77.01000583637591,
        "flow_mL_s": 100,
        "pressure_mmHg": 77.01000583637585,
        "time_seconds": 1.98
      },
      {
        "closed_form_mmHg": 77.4850285361405,
        "flow_mL_s": 100,
        "pressure_mmHg": 77.48502853614045,
        "time_seconds": 2.0
      }
    ],
    "switch_time_seconds": 1.0
  },
  "grid_interpretation": "Calibration-only loss surface, not a confidence region or proof of identifiability; holdout values do not select parameters.",
  "holdout_rmse_vs_observed_mmHg": 0.9798338973871291,
  "holdout_rmse_vs_synthetic_truth_mmHg": 0.0,
  "interpretation": "Synthetic parameter recovery within the same generating model; no patient-specific or clinical validation.",
  "ramp_forcing_probe": {
    "cases": [
      {
        "absolute_endpoint_error_mmHg": 0.9731171367997717,
        "analytic_endpoint_mmHg": 70.966512927195,
        "dt_seconds": 0.08,
        "endpoint_mmHg": 69.99339579039523,
        "samples": 25
      },
      {
        "absolute_endpoint_error_mmHg": 0.4847698527549653,
        "analytic_endpoint_mmHg": 70.966512927195,
        "dt_seconds": 0.04,
        "endpoint_mmHg": 70.48174307444003,
        "samples": 50
      },
      {
        "absolute_endpoint_error_mmHg": 0.24193772814385284,
        "analytic_endpoint_mmHg": 70.966512927195,
        "dt_seconds": 0.02,
        "endpoint_mmHg": 70.72457519905115,
        "samples": 100
      }
    ],
    "duration_seconds": 2,
    "interpretation": "Separate linear-ramp forcing Q(t)=20+30t with independent continuous-forcing closed form. Left-endpoint piecewise-constant flow approximates this ramp; errors should converge with timestep refinement. This is same-model numerical validation, not patient/physiological validation or calibration uncertainty.",
    "q0_mL_s": 20,
    "slope_mL_s2": 30
  },
  "sensitivity": {
    "R_multiplier_0.8": 19.074083575699877,
    "R_multiplier_1": 0.0,
    "R_multiplier_1.2": 18.711469414905515
  },
  "time_convention": "time_seconds labels post-step pressure at (i+1)*dt; each flow value applies on [flow_interval_start_seconds, time_seconds). Initial pressure at t=0 is not an exported observation."
}
```

Result SHA-256: `817338a8954a3067af3eb35371bc98ed62eab7bee50a5c230355fb86fc11a2e1`
