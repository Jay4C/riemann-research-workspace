"""
zeros.py

Utilities for exploring non-trivial zeros
of the Riemann zeta function.
"""

from __future__ import annotations

import mpmath as mp

DEFAULT_PRECISION = 80


###############################################################################
# PRECISION
###############################################################################

def set_precision(dps=DEFAULT_PRECISION):

    mp.mp.dps = dps


###############################################################################
# SINGLE ZERO
###############################################################################

def get_zero(
    n: int,
    dps: int = DEFAULT_PRECISION,
):
    """
    Return nth non-trivial zero.

    Parameters
    ----------
    n : int
        Index >= 1
    """

    if n < 1:
        raise ValueError(
            "Zero index must be >= 1"
        )

    set_precision(dps)

    return mp.zetazero(n)


###############################################################################
# MULTIPLE ZEROS
###############################################################################

def get_first_zeros(
    count: int = 10,
    dps: int = DEFAULT_PRECISION,
):
    """
    Return first 'count' zeros.
    """

    set_precision(dps)

    zeros = []

    for n in range(1, count + 1):

        zeros.append(
            get_zero(
                n,
                dps=dps,
            )
        )

    return zeros


###############################################################################
# DISTANCE TO THE CRITICAL LINE
###############################################################################

def distance_from_critical_line(z):

    return abs(
        mp.re(z) - mp.mpf("0.5")
    )


def check_zero_on_critical_line(
    n: int,
    tolerance=mp.mpf("1e-50"),
    dps: int = DEFAULT_PRECISION,
):
    """
    Numerical check.
    """

    z = get_zero(
        n,
        dps=dps,
    )

    return (
        distance_from_critical_line(z)
        < tolerance
    )


###############################################################################
# ZERO TABLE
###############################################################################

def zero_table(
    count: int = 10,
    dps: int = DEFAULT_PRECISION,
):
    """
    Return a structured table.
    """

    zeros = get_first_zeros(
        count,
        dps=dps,
    )

    table = []

    for k, z in enumerate(zeros, start=1):

        table.append({
            "index": k,
            "real": str(mp.re(z)),
            "imag": str(mp.im(z)),
            "distance_to_critical_line":
                str(distance_from_critical_line(z))
        })

    return table


###############################################################################
#