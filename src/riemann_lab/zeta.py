"""
zeta.py

Core numerical utilities for the Riemann zeta function.
"""

from __future__ import annotations

import mpmath as mp

DEFAULT_PRECISION = 80


###############################################################################
# PRECISION MANAGEMENT
###############################################################################

def set_precision(dps: int = DEFAULT_PRECISION) -> None:
    """
    Set working precision.

    Parameters
    ----------
    dps : int
        Decimal digits.
    """
    mp.mp.dps = dps


###############################################################################
# ZETA FUNCTION
###############################################################################

def zeta(s, dps: int = DEFAULT_PRECISION):
    """
    Evaluate zeta(s).

    Parameters
    ----------
    s : complex-like
    dps : int

    Returns
    -------
    complex
    """
    set_precision(dps)
    return mp.zeta(s)


###############################################################################
# CRITICAL LINE
###############################################################################

def critical_point(t):
    """
    Return

        1/2 + i t
    """

    return mp.mpf("0.5") + 1j * mp.mpf(t)


def critical_value(t, dps: int = DEFAULT_PRECISION):
    """
    Evaluate zeta on the critical line.
    """

    return zeta(
        critical_point(t),
        dps=dps,
    )


###############################################################################
# FUNCTIONAL EQUATION
###############################################################################

def functional_equation_rhs(s):
    """
    RHS of the Riemann functional equation.
    """

    return (
        2**s
        * mp.pi**(s - 1)
        * mp.sin(mp.pi * s / 2)
        * mp.gamma(1 - s)
        * mp.zeta(1 - s)
    )


def functional_equation_residual(
    s,
    dps: int = DEFAULT_PRECISION,
):
    """
    Absolute residual:

    |LHS - RHS|
    """

    set_precision(dps)

    lhs = mp.zeta(s)
    rhs = functional_equation_rhs(s)

    return abs(lhs - rhs)


###############################################################################
# RIEMANN XI FUNCTION
###############################################################################

def xi(s, dps: int = DEFAULT_PRECISION):
    """
    Riemann Xi function.

    Xi(s) =
    1/2 * s(s-1)
    * pi^{-s/2}
    * Gamma(s/2)
    * zeta(s)
    """

    set_precision(dps)

    return (
        0.5
        * s
        * (s - 1)
        * mp.pi ** (-s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


###############################################################################
# DIAGNOSTICS
###############################################################################

def verify_known_identity(
    dps: int = DEFAULT_PRECISION,
):
    """
    Verify:

        zeta(2) = pi²/6
    """

    set_precision(dps)

    lhs = mp.zeta(2)
    rhs = mp.pi**2 / 6

    return abs(lhs - rhs)


if __name__ == "__main__":

    print("zeta(2) =", zeta(2))
    print("identity error =", verify_known_identity())