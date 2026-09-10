"""
test_zeta.py

Unit tests for riemann_lab.zeta
"""

import mpmath as mp
import pytest

from riemann_lab.zeta import (
    zeta,
    critical_point,
    critical_value,
    functional_equation_residual,
    verify_known_identity,
    xi,
)

TOL = mp.mpf("1e-50")


###############################################################################
# BASIC VALUES
###############################################################################

def test_zeta_two():

    expected = mp.pi**2 / 6

    assert abs(
        zeta(2) - expected
    ) < TOL


def test_zeta_four():

    expected = mp.pi**4 / 90

    assert abs(
        zeta(4) - expected
    ) < TOL


###############################################################################
# CRITICAL LINE
###############################################################################

def test_critical_point():

    z = critical_point(14)

    assert mp.re(z) == mp.mpf("0.5")
    assert mp.im(z) == 14


def test_critical_value():

    value = critical_value(14)

    assert value is not None


###############################################################################
# FUNCTIONAL EQUATION
###############################################################################

def test_functional_equation():

    s = mp.mpc("0.3", "7.0")

    residual = functional_equation_residual(s)

    assert residual < mp.mpf("1e-40")


###############################################################################
# XI FUNCTION
###############################################################################

def test_xi_symmetry():

    s = mp.mpc("0.7", "11")

    left = xi(s)
    right = xi(1 - s)

    assert abs(left - right) < mp.mpf("1e-40")


###############################################################################
# KNOWN IDENTITY
###############################################################################

def test_euler_identity():

    err = verify_known_identity()

    assert err < mp.mpf("1e-60")


###############################################################################
# SPECIAL VALUES
###############################################################################

def test_zeta_negative_even():

    assert abs(
        zeta(-2)
    ) < mp.mpf("1e-50")


def test_zeta_negative_four():

    assert abs(
        zeta(-4)
    ) < mp.mpf("1e-50")


###############################################################################
# NUMERICAL STABILITY
###############################################################################

@pytest.mark.parametrize(
    "value",
    [2, 3, 4, 5, 6]
)
def test_finite_values(value):

    result = zeta(value)

    assert mp.isfinite(result)