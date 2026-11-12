from hypothesis import given, strategies as st
from loan_eligibility import parse_income, monthly_emi, pan_category

@given(st.text() | st.none())
def test_parse_income_no_crash(s):
    try:
        parse_income(s)
    except ValueError:
        pass  # the only documented rejection
    except Exception as e:
        assert False, f"parse_income crashed with {type(e).__name__}: {e}"

@given(st.text() | st.none())
def test_monthly_emi_no_crash(s):
    try:
        monthly_emi(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"monthly_emi crashed with {type(e).__name__}: {e}"

@given(st.text() | st.none())
def test_pan_category_no_crash(s):
    try:
        pan_category(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"pan_category crashed with {type(e).__name__}: {e}"