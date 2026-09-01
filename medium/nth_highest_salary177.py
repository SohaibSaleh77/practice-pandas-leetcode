"""177. Nth Highest Salary"""
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f"getNthHighestSalary({N})"
    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if N <= 0 or N > salaries.size:
        return pd.DataFrame({col: [None]})
    return pd.DataFrame({col: [salaries.iloc[N - 1]]})


def _run_checks() -> None:
    emp = pd.DataFrame({"id": [1, 2, 3], "salary": [100, 200, 300]})
    out = nth_highest_salary(emp, 2)
    pd.testing.assert_frame_equal(out, pd.DataFrame({"getNthHighestSalary(2)": [200]}))
    out2 = nth_highest_salary(emp, 5)
    pd.testing.assert_frame_equal(out2, pd.DataFrame({"getNthHighestSalary(5)": [None]}))
    print("✓ 177 test passed")


if __name__ == "__main__":
    _run_checks()
