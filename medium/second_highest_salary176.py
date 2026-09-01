"""176. Second Highest Salary"""
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if salaries.size < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    return pd.DataFrame({"SecondHighestSalary": [salaries.iloc[1]]})


def _run_checks() -> None:
    emp = pd.DataFrame({"id": [1, 2, 3], "salary": [100, 200, 300]})
    out = second_highest_salary(emp)
    pd.testing.assert_frame_equal(out, pd.DataFrame({"SecondHighestSalary": [200]}))

    emp2 = pd.DataFrame({"id": [1], "salary": [100]})
    out2 = second_highest_salary(emp2)
    pd.testing.assert_frame_equal(out2, pd.DataFrame({"SecondHighestSalary": [None]}))
    print("✓ 176 test passed")


if __name__ == "__main__":
    _run_checks()
