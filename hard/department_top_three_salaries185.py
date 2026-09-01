"""185. Department Top Three Salaries"""
import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=["Department", "Employee", "Salary"])

    joined = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        suffixes=("_emp", "_dep"),
    )
    joined["rank"] = joined.groupby("departmentId")["salary"].rank(
        method="dense", ascending=False
    )
    top = joined[joined["rank"] <= 3]
    return top.rename(
        columns={"name_dep": "Department", "name_emp": "Employee", "salary": "Salary"}
    )[["Department", "Employee", "Salary"]].reset_index(drop=True)


def _run_checks() -> None:
    employee = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6],
            "name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy"],
            "salary": [85000, 80000, 60000, 90000, 69000, 85000],
            "departmentId": [1, 2, 2, 1, 1, 1],
        }
    )
    department = pd.DataFrame({"id": [1, 2], "name": ["IT", "Sales"]})
    out = top_three_salaries(employee, department)
    want = pd.DataFrame(
        {
            "Department": ["IT", "IT", "IT", "IT", "Sales", "Sales"],
            "Employee": ["Max", "Joe", "Randy", "Janet", "Henry", "Sam"],
            "Salary": [90000, 85000, 85000, 69000, 80000, 60000],
        }
    )
    pd.testing.assert_frame_equal(
        out.sort_values(["Department", "Salary"], ascending=[True, False]).reset_index(
            drop=True
        ),
        want.sort_values(["Department", "Salary"], ascending=[True, False]).reset_index(
            drop=True
        ),
    )
    print("✓ 185 test passed")


if __name__ == "__main__":
    _run_checks()
