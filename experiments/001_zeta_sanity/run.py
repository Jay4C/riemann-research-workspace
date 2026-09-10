"""
EXP-001
Zeta Sanity Checks

Purpose:
    Validate numerical routines before conducting
    larger experiments involving the Riemann zeta function.

Author:
    Jason ALOYAU

Status:
    READY
"""

from pathlib import Path
import json
import mpmath as mp

###############################################################################
# CONFIGURATION
###############################################################################

PRECISION_DIGITS = 80

OUTPUT_FILE = Path(__file__).parent / "results.json"

###############################################################################
# HELPERS
###############################################################################


def set_precision():
    mp.mp.dps = PRECISION_DIGITS


def zeta_2_error():
    """
    Verify:
        zeta(2) = pi² / 6
    """
    lhs = mp.zeta(2)
    rhs = mp.pi**2 / 6
    return abs(lhs - rhs)


def zeta_4_error():
    """
    Verify:
        zeta(4) = pi⁴ / 90
    """
    lhs = mp.zeta(4)
    rhs = mp.pi**4 / 90
    return abs(lhs - rhs)


def functional_equation_residual(s):
    """
    Residual of the Riemann zeta functional equation.
    """

    lhs = mp.zeta(s)

    rhs = (
        2**s
        * mp.pi**(s - 1)
        * mp.sin(mp.pi * s / 2)
        * mp.gamma(1 - s)
        * mp.zeta(1 - s)
    )

    return abs(lhs - rhs)


def compute_reference_zeros(count=10):
    """
    Compute first non-trivial zeros.
    """

    zeros = []

    for n in range(1, count + 1):
        z = mp.zetazero(n)

        zeros.append(
            {
                "index": n,
                "real": str(z.real),
                "imag": str(z.imag),
            }
        )

    return zeros


###############################################################################
# MAIN
###############################################################################


def run():

    set_precision()

    residual = functional_equation_residual(
        mp.mpc("0.3", "7.0")
    )

    results = {
        "experiment": "EXP-001",
        "precision_digits": PRECISION_DIGITS,
        "checks": {
            "zeta_2_error": str(zeta_2_error()),
            "zeta_4_error": str(zeta_4_error()),
            "functional_equation_error": str(residual),
        },
        "first_zeros": compute_reference_zeros(10),
    }

    OUTPUT_FILE.write_text(
        json.dumps(results, indent=4),
        encoding="utf-8",
    )

    print("\nEXP-001 completed successfully.\n")
    print(f"Results written to:\n{OUTPUT_FILE}\n")


if __name__ == "__main__":
    run()