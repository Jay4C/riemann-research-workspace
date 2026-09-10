"""
riemann_lab

Research utilities for experiments involving the
Riemann zeta function.

This package provides:

- High precision evaluation of zeta(s)
- Functional equation checks
- Critical line utilities
- Zero exploration helpers
- Numerical diagnostics

IMPORTANT

This package provides exploratory numerical tools.

Numerical computations are not proofs of the
Riemann Hypothesis.
"""

__version__ = "0.1.0"

__author__ = "Jason ALOYAU"

__all__ = [
    "zeta",
    "critical_value",
    "functional_equation_residual",
    "get_zero",
    "get_first_zeros",
]