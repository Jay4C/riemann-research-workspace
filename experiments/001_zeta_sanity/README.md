# EXP-001 — Zeta Sanity Checks

## Experiment Identifier

```text
EXP-001
```

## Purpose

This experiment validates that the numerical environment is correctly configured before any larger investigation concerning the Riemann zeta function.

The objective is **not** to test the Riemann Hypothesis itself.

Instead, the goal is to ensure that:

- Arbitrary precision arithmetic works correctly.
- Known identities involving the zeta function are reproduced.
- The implementation remains stable across environments.
- Numerical precision behaves as expected.

---

# Scientific Motivation

Before attempting any advanced computation involving:

- critical-line zeros,
- Gram points,
- Turing's methods,
- Riemann–Siegel evaluations,

it is necessary to establish confidence in the computational environment.

This experiment acts as a baseline diagnostic.

---

# Checks Performed

## Check A

Validate:

\[
\zeta(2)=\frac{\pi^2}{6}
\]

This identity is known exactly from Euler's solution of the Basel problem.

---

## Check B

Validate:

\[
\zeta(4)=\frac{\pi^4}{90}
\]

---

## Check C

Compute the first non-trivial zeros using mpmath.

Expected values:

\[
0.5 + 14.134725i
\]

\[
0.5 + 21.022040i
\]

\[
0.5 + 25.010857i
\]

---

## Check D

Evaluate the residual of the functional equation

\[
\zeta(s)=
2^s
\pi^{s-1}
\sin\left(
\frac{\pi s}{2}
\right)
\Gamma(1-s)
\zeta(1-s)
\]

for selected complex values.

The residual should be close to zero.

---

# Numerical Precision

Default precision:

```yaml
precision_digits: 80
```

---

# Output

The experiment generates:

```text
results.json
```

containing:

```json
{
  "zeta_2_error": "...",
  "zeta_4_error": "...",
  "functional_equation_error": "...",
  "first_zeros": [...]
}
```

---

# Reproducibility

Environment:

```yaml
python: 3.11+
library: mpmath
precision: arbitrary
```

---

# Expected Interpretation

Successful completion indicates:

- the numerical environment appears healthy;
- arbitrary precision arithmetic behaves correctly;
- the zeta wrapper functions operate as expected.

Successful completion does **not** provide evidence for or against the Riemann Hypothesis.

---

# Future Extensions

Potential EXP-002:

- Gram points

Potential EXP-003:

- Hardy Z function

Potential EXP-004:

- Turing method validation

Potential EXP-005:

- Jensen polynomial experiments

Potential EXP-006:

- Li coefficient computations