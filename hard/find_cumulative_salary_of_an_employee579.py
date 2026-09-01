"""579. Find Cumulative Salary of an Employee"""
import pandas as pd


def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee.empty:
        return pd.DataFrame(columns=["id", "month", "Salary"])

    employee = employee.sort_values(["id", "month"])
    # Exclude each employee's most recent month (no cumulative there).
    last_month = employee.groupby("id")["month"].transform("max")
    filtered = employee[employee["month"] != last_month].copy()

    if filtered.empty:
        return pd.DataFrame(columns=["id", "month", "Salary"])

    # Rolling 3-month sum per employee.
    filtered["Salary"] = (
        filtered.groupby("id")["salary"]
        .rolling(window=3, min_periods=1)
        .sum()
        .reset_index(level=0, drop=True)
    )

    top3 = (
        filtered.sort_values(["id", "month"], ascending=[True, False])
        .groupby("id")
        .head(3)
    )
    return top3[["id", "month", "Salary"]].reset_index(drop=True)


def _run_checks() -> None:
    employee = pd.DataFrame(
        {
            "id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "month": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
            "salary": [20, 30, 40, 50, 60, 40, 60, 80, 100, 120],
        }
    )
    out = cumulative_salary(employee)
    want = pd.DataFrame(
        {
            "id": [1, 1, 1, 2, 2, 2],
            "month": [4, 3, 2, 4, 3, 2],
            "Salary": [120.0, 90.0, 50.0, 240.0, 180.0, 100.0],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 579 test passed")


if __name__ == "__main__":
    _run_checks()
