"""
test_zeros.py

Unit tests for riemann_lab.zeros
"""

import mpmath as mp
import pytest

from riemann_lab.zeros import (
    get_zero,
    get_first_zeros,
    distance_from_critical_line,
    check_zero_on_critical_line,
    zero_table,
    consecutive_spacings,
)

###############################################################################
# REFERENCE VALUES
###############################################################################

FIRST_ZERO_IMAG = mp.mpf(
    "14.134725141734693790457251983562"
)

SECOND_ZERO_IMAG = mp.mpf(
    "21.022039638771554992628479593896"
)

###############################################################################
# SINGLE ZERO
###############################################################################

def test_first_zero():

    z = get_zero(1)

    assert abs(
        mp.im(z) - FIRST_ZERO_IMAG
    ) < mp.mpf("1e-20")


def test_second_zero():

    z = get_zero(2)

    assert abs(
        mp.im(z) - SECOND_ZERO_IMAG
    ) < mp.mpf("1e-20")


###############################################################################
# MULTIPLE ZEROS
###############################################################################

def test_first_ten_zeros():

    zeros = get_first_zeros(10)

    assert len(zeros) == 10


def test_first_twenty_zeros():

    zeros = get_first_zeros(20)

    assert len(zeros) == 20


###############################################################################
# CRITICAL LINE
###############################################################################

def test_first_zero_is_on_critical_line():

    z = get_zero(1)

    d = distance_from_critical_line(z)

    assert d < mp.mpf("1e-50")


def test_check_zero_on_line():

    assert check_zero_on_critical_line(1)


def test_check_tenth_zero_on_line():

    assert check_zero_on_critical_line(10)


###############################################################################
# TABLE GENERATION
###############################################################################

def test_zero_table():

    table = zero_table(5)

    assert len(table) == 5


def test_zero_table_fields():

    row = zero_table(1)[0]

    assert "index" in row
    assert "real" in row
    assert "imag" in row
    assert "distance_to_critical_line" in row


###############################################################################
# SPACINGS
###############################################################################

def test_spacing_count():

    spacings = consecutive_spacings(20)

    assert len(spacings) == 19


def test_spacing_positive():

    spacings = consecutive_spacings(20)

    for spacing in spacings:

        assert spacing > 0


###############################################################################
# INVALID INPUTS
###############################################################################

def test_zero_index_zero():

    with pytest.raises(ValueError):

        get_zero(0)


def test_zero_index_negative():

    with pytest.raises(ValueError):

        get_zero(-1)


###############################################################################
# MONOTONICITY
###############################################################################

def test_zero_ordering():

    zeros = get_first_zeros(20)

    imags = [
        mp.im(z)
        for z in zeros
    ]

    for i in range(len(imags) - 1):

        assert imags[i + 1] > imags[i]


###############################################################################
# REGRESSION TESTS
###############################################################################

def test_reference_real_part():

    z = get_zero(1)

    assert abs(
        mp.re(z) - mp.mpf("0.5")
    ) < mp.mpf("1e-50")


def test_reference_tenth_zero():

    z = get_zero(10)

    assert (
        mp.im(z)
        > 49
    )