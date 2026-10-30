import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate

#Example test cases:
def test_excellent_band():
    assert credit_band(800) == "excellent"

def test_eligible():
    assert is_eligible(30, 50000, "salaried", 800) is True

#Write the rest of the test cases so that the code is 90- 100% covered.

def test_credit_band_remaining_lines():
  # Hits ValueError line
  with pytest.raises(ValueError):
    credit_band(200)
  # Hits "good", "fair", and "poor" return lines
  assert credit_band(700) == "good"
  assert credit_band(600) == "fair"
  assert credit_band(400) == "poor"


def test_is_eligible_remaining_lines():
  # Hits unknown employment ValueError line
  with pytest.raises(ValueError):
    is_eligible(30, 50000, "freelance", 800)
  # Hits age boundary False line
  assert is_eligible(18, 50000, "salaried", 800) is False
  # Hits income boundary False line
  assert is_eligible(30, 1000, "salaried", 800) is False
  # Hits poor credit False line
  assert is_eligible(30, 50000, "salaried", 400) is False


def test_interest_rate_remaining_lines():
  # Hits "good" rate line (10)
  assert interest_rate(700, "salaried", False) == 10
  # Hits "else" rate line (13) and collateral subtraction line (-2)
  assert interest_rate(400, "salaried", True) == 11
  # Hits self-employed addition line (+1)
  assert interest_rate(800, "self_employed", False) == 9

  # --- Additional branch tests ---


def test_credit_band_score_upper_bound():
  # test score > 900 error
  with pytest.raises(ValueError):
    credit_band(950)


def test_is_eligible_boundary_ages():
  # test exact age limits 21 and 60
  assert is_eligible(21, 50000, "salaried", 800) is True
  assert is_eligible(60, 50000, "salaried", 800) is True


def test_is_eligible_self_employed_income_branch():
  # test self employed income threshold branches
  assert is_eligible(30, 30000, "self_employed", 800) is False
  assert is_eligible(30, 40000, "self_employed", 800) is True


def test_interest_rate_excellent_and_collateral_branches():
  # test excellent band with collateral and good band with self employed
  assert interest_rate(800, "salaried", True) == 6
  assert interest_rate(700, "self_employed", False) == 11
