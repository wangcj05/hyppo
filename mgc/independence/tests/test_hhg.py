import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ...benchmarks.simulation import linear
from ..hhg import HHG


class TestHHGStat:
    @pytest.mark.parametrize("n, obs_stat", [
        (10, 560.0),
        (50, 112800.0),
        (100, 950600.0)
    ])
    @pytest.mark.parametrize("obs_pvalue", [1/1000])
    def test_linear_oned(self, n, obs_stat, obs_pvalue):
        np.random.seed()
        x, y = linear(n, 1, dim=1, noise=0)
        hhg = HHG()
        stat = hhg.statistic(x, y)
        pvalue = hhg.p_value(x, y)[0]

        assert_almost_equal(stat, obs_stat, decimal=2)
        assert_almost_equal(pvalue, obs_pvalue, decimal=2)

    @pytest.mark.parametrize("n, obs_stat", [
        (10, 560.0),
        (50, 112800.0),
        (100, 950600.0)
    ])
    @pytest.mark.parametrize("obs_pvalue", [1/1000])
    def test_linear_fived(self, n, obs_stat, obs_pvalue):
        np.random.seed()
        x, y = linear(n, 1, dim=5, noise=0)
        hhg = HHG()
        stat = hhg.statistic(x, y)
        pvalue = hhg.p_value(x, y)[0]

        assert_almost_equal(stat, obs_stat, decimal=2)
        assert_almost_equal(pvalue, obs_pvalue, decimal=2)
