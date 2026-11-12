# Development log

## 2026-11-12 — correctness and reproducibility

Replaced the cancellation-prone 1-exp(-dt/tau) inflow weight with -expm1(-dt/tau). Reject nonfinite simulation inputs and unrepresentable time constants.

Analytic small-step regressions confirm nonzero flow at dt=1e-18 and accumulated flow over 100 steps. Tests reject NaN/infinity and time-constant overflow/underflow while preserving existing analytic and calibration checks.

Validation before publication (Python 3.11.0, macOS):

- Full suite: 12 tests passed with `python3 -m unittest discover -s tests -v`.
- `python3 pipeline.py` regenerated the checked-in data, measured results, report and manifest.
- `python3 pipeline.py --verify` passed independent byte-for-byte recomputation.
- `git diff --check` and actionlint 1.7.12 passed; workflow configuration is unchanged. Optional shellcheck integration is unavailable locally.

Metrics were regenerated, not edited by hand. Source hashes and artifact checksums were refreshed. Linux may differ from macOS in final floating-point bits; CI generates and verifies results within its own runtime. Synthetic data only; no clinical validation is claimed.

Hosted results are available on this repository's [Actions page](https://github.com/hrix7/Biomedical-Digital-Twin/actions). This entry records local checks, not a claim that an as-yet-unobserved hosted run succeeded.
