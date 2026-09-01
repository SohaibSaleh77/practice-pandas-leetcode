"""569. Median Employee Salary"""
import pandas as pd


def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Rank within company; pick the middle rank when (count + 1) // 2.
    ranked = employee.assign(
        rank=employee.groupby("company")["salary"].rank(method="dense")
    )
    ranked["total"] = ranked.groupby("company")["salary"].transform("count")
    ranked["mid"] = (ranked["total"] + 1) // 2
    return ranked[ranked["rank"] == ranked["mid"]][["id", "company", "salary"]]


def _run_checks() -> None:
    employee = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6],
            "company": ["A", "A", "A", "B", "B", "B"],
            "salary": [2341, 341, 15, 15314, 451, 513],
        }
    )
    out = median_employee_salary(employee)
    want = pd.DataFrame(
        {"id": [2, 6], "company": ["A", "B"], "salary": [341, 513]}
    )
    pd.testing.assert_frame_equal(
        out.sort_values(["company", "salary"]).reset_index(drop=True),
        want.sort_values(["company", "salary"]).reset_index(drop=True),
    )
    print("✓ 569 test passed")


if __name__ == "__main__":
    _run_checks()
