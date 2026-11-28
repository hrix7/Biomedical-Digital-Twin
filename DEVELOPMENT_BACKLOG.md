# Development backlog

## Completed

- 2026-11-12: Preserve small-timestep inflow contributions with expm1 and reject nonfinite or unrepresentable simulation inputs.

## Completed — 2026-11-13

Ranked calibration grid, runner-up gap and boundary diagnostics.

## Completed — 2026-11-14

Finite calibration-loss contract and overflow-safe RMSE.

## Completed — 2026-11-15

Correct post-step observation timestamps and expose flow intervals.

## Completed — 2026-11-17

Independent forcing-step probe.

## Completed — 2026-11-18

Avoid intermediate flow-product overflow and underflow.

## Completed — 2026-11-19

Validate experiment configuration before simulation.

## Completed — 2026-11-20

Continuous-ramp forcing convergence probe.

## Next priorities

1. Quantify calibration uncertainty without treating the finite grid as a confidence region.
2. Evaluate model mismatch separately from same-model recovery.
3. Extend analytic probes with explicit numerical-domain limits.

## Completed — 2026-11-21

Preserve tiny continuous-ramp response.

## Completed — 2026-11-24

Discrete calibration loss profiles.

## Current ordered next steps

1. Quantify calibration noise sensitivity with a declared conditional resampling protocol before confidence-region claims.
2. Review public-data terms, exact release/checksums and subject mappings before ingestion; keep synthetic and public-data evaluation distinct.

## Completed — 2026-11-25

Calibration observation-bias sensitivity.

## Current next steps

1. Review a conditional noise-resampling protocol and residual assumptions before statistical uncertainty claims.
2. Review real-data license/version/checksums and subject mappings before ingestion.

## Completed — 2026-11-26

Validate discrete profile inputs.

## Current ordered next steps

1. Review a conditional noise-resampling protocol and residual assumptions before statistical uncertainty claims.
2. Review official data terms/version/checksums and subject mapping before any real-data ingestion.


## Completed — 2026-11-28

Calibration residual diagnostics. Calibration-only observed-minus-predicted mean, RMSE and centered lag-1 ratio; stable scaled computation and explicit constant-residual null. This exposes assumptions before resampling; no normality/independence test, confidence interval or holdout fitting.

## Next ordered work

1. Review these conditional diagnostics before expanding experiments; keep descriptive scenarios separate from statistical uncertainty.
2. Review exact public release/terms/checksums and participant mapping before real-data integration.
