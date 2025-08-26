import pytest
from src.file import Calculator
from contextlib import nullcontext as does_not_raise


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expect",
        [
            (1, 0.5, 2, does_not_raise()),
            (3, 4, 0.75, does_not_raise()),
            (5, 0, 1, pytest.raises(ZeroDivisionError)),
        ],
    )
    def test_divide(self, x, y, res, expect):
        with expect:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 3),
            (5, 6, 11),
        ],
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res
