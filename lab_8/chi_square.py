import numpy as np
from scipy import stats


def check_normality_chi2(data):
    mu = np.mean(data)
    sigma = np.std(data, ddof=1)
    n = len(data)

    num_bins = int((3.78 * (n - 1)) ** (2 / 5))
    observed_freq, bin_edges = np.histogram(data, bins=num_bins)

    cdf_values = stats.norm.cdf(bin_edges, mu, sigma)
    expected_probs = np.diff(cdf_values)

    expected_probs = expected_probs / expected_probs.sum()
    expected_freq = expected_probs * n

    chi2_stat, p_val = stats.chisquare(f_obs=observed_freq, f_exp=expected_freq, ddof=2)

    if p_val < 0.05:
        return False

    else:
        return True
