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

## 2026-11-13

Ranked calibration loss grid, runner-up gap and boundary flags.

Exports all calibration-only R/C losses with a runner-up loss gap and flags indicating whether the best grid value is on an edge. These are finite-grid diagnostics, not confidence regions or a proof of identifiable parameters. A constant equilibrium test demonstrates that different compliances can be indistinguishable up to floating-point roundoff. Holdout data never select grid parameters.

Validation: full unittest suite, pipeline regeneration and byte-for-byte verifier, diff review; GitHub validation outcome is tracked after push. No workflow/permission changes.

## 2026-11-14

Finite calibration-loss contract and overflow-safe RMSE.

Rejects nonfinite or incomplete calibration observations before grid ranking and empty parameter grids before selection. RMSE scales finite differences before squaring so large representable errors do not overflow; unrepresentable differences fail explicitly. Existing calibration and holdout protocol remains unchanged.

Validation before publication: full unittest suite, regenerated pipeline artifacts, byte-for-byte verification and diff review. Workflow configuration/permissions unchanged; existing policy tests pass. Hosted CI is followed after the tested source is published.

## 2026-11-15

Correct post-step observation timestamps and expose flow intervals.

The exact simulator returns pressure after each integration step. time_seconds now correctly labels (i+1)*dt rather than i*dt; flow_interval_start_seconds identifies the start of the preceding piecewise-constant-flow interval. Initial pressure at t=0 is not an exported observation. Pressure values, model parameters and calibration/holdout membership are unchanged; this fixes a one-step time-label error, not a performance gain.

Validation before publication: full unittest suite, pipeline regeneration/byte verifier, diff review and existing workflow-policy tests. Workflows and permissions unchanged. Hosted validation is followed after publication.

## 2026-11-17 — Independent forcing-step probe

Completed the retained, unpublished implementation from November 16. Added a zero-to-constant inflow probe and an independently evaluated two-phase closed form. Every post-step pressure is exported with its analytic reference; tests cover the phase boundary, endpoint, invalid phase sizes and unrepresentable duration. This same-model numerical check is not physiological validation. Full unit tests, pipeline regeneration and artifact verification run before publication; no workflow or permission changes.

## 2026-11-18 — Avoid intermediate flow-product overflow and underflow

The exact update now evaluates R*Q*gain with exponent-scaled multiplication. Valid finite contributions survive intermediate overflow or underflow; truly unrepresentable outputs still fail. Independent extreme-magnitude tests cover both paths, signed/zero products and invalid factors. The idealized model and inference scope are unchanged. Full suite: 24 tests passed; pipeline generation, independent --verify and diff checks passed before publication. No workflow/permission changes; workflow policy tests passed.

## 2026-11-19 — Validate experiment configuration before simulation

Added validation for a nonempty calibration/forward holdout, integer counts/seed, positive finite parameters/timestep, nonnegative noise, unique nonempty parameter grids and representable time constants/durations. Invalid settings fail before simulation. Tests use a simulation spy and exercise the smallest valid record and singleton calibration grid. No clinical validity or confidence-region interpretation is implied. Full suite: 26 tests passed; pipeline generation, independent --verify and diff checks passed before publication. No workflow or permission changes; workflow policy tests passed.

## 2026-11-20 — Continuous-ramp forcing convergence probe

Added an independent continuous-linear-inflow closed form and measured endpoint errors for left-endpoint piecewise-constant simulations at 25/50/100 steps over 2 s. Tests verify initial/decay limits, a separately rearranged analytic formula and observed first-order refinement. This is simplified same-model numerical validation, not physiological or clinical validation. Full suite: 29 tests passed; pipeline generation, independent --verify and diff checks passed before publication. Workflow policy tests passed without workflow/permission changes.

## 2026-11-21 — Preserve tiny continuous-ramp response

Replace cancellation-prone time minus tau times gain with a small-argument series below t/tau=0.001. Compare against a 70-digit Decimal analytic integral from 1e-12 through both sides of the switch, without relaxing existing convergence tests. Same-model numerical check, not physiological validation.

Validation: full existing suite plus new tests (30 passed), pipeline generation and independent --verify, scoped diff review and git diff --check before publication. Hosted CI is followed after pushing. Existing read-only validation/publisher workflows unchanged; workflow-policy tests included.

## 2026-11-24 — Discrete calibration loss profiles

For each R and C grid value, report the minimum calibration RMSE over the other grid parameter. Preserve ties and grid limitations. Hand-grid and permutation/singleton tests independently verify minima. These are discrete nuisance-parameter loss summaries, not confidence intervals or proof of continuous identifiability. No holdout observations enter calibration.

Validation before publication: 32 full-suite tests passed, pipeline regeneration and independent --verify passed, scoped diff/checksum review and git diff --check passed. Workflow policy tests included; workflows and permissions unchanged. Hosted validation followed after pushing.

## 2026-11-25 — Calibration observation-bias sensitivity

Refit the same finite grid after additive -1, 0 and +1 mmHg offsets on calibration observations only. Report selected parameters/loss for each offset. Independent hand-grid and invalid-observation tests verify behavior. This is deterministic systematic-bias sensitivity, not a bootstrap confidence region, sensor validation or patient uncertainty.

Pre-publication validation: 34 full-suite tests passed; pipeline generation and independent --verify, scoped diff and checksum review, git diff --check passed. Existing workflow policy tests included; no permission/workflow changes. Hosted CI followed after publication.
