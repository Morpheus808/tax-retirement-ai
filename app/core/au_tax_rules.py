# Approx AU personal tax + Medicare levy and super settings (update each FY).
# Figures are indicative (simplified) for demo/MVP purposes.

from typing import List, Tuple

# Each tuple: (threshold, rate, base_tax_at_threshold)
TAX_BANDS: List[Tuple[float, float, float]] = [
    (0.0,      0.00,     0.0),     # 0 – 18,200
    (18200.0,  0.16,     0.0),     # 18,201 – 45,000
    (45000.0,  0.30,  4292.0),     # 45,001 – 135,000
    (135000.0, 0.37, 34292.0),     # 135,001 – 190,000
    (190000.0, 0.45, 54892.0),     # 190,001+
]

MEDICARE_LEVY_RATE = 0.02  # simplified 2%
CONCESSIONAL_CAP   = 27_500.0
NON_CONCESSIONAL_CAP = 110_000.0
SG_RATE_DEFAULT    = 0.115  # 11.5% (adjust per FY)
CONTRIBS_TAX_RATE  = 0.15   # contributions tax inside super

def income_tax(income: float) -> float:
    if income <= TAX_BANDS[1][0]:
        return 0.0
    for thr, rate, base in reversed(TAX_BANDS):
        if income > thr:
            return base + (income - thr) * rate
    return 0.0

def medicare_levy(income: float) -> float:
    return max(0.0, income * MEDICARE_LEVY_RATE)

def total_personal_tax(income: float) -> float:
    return income_tax(income) + medicare_levy(income)

def marginal_rate(income: float) -> float:
    for thr, rate, _ in reversed(TAX_BANDS):
        if income > thr:
            return rate
    return 0.0

def concessional_cap() -> float:
    return CONCESSIONAL_CAP

def non_concessional_cap() -> float:
    return NON_CONCESSIONAL_CAP

def sg_rate() -> float:
    return SG_RATE_DEFAULT

def contributions_tax(amount: float) -> float:
    return amount * CONTRIBS_TAX_RATE
