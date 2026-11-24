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
