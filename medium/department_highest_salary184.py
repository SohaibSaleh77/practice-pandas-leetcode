"""184. Department Highest Salary"""
import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    merged = employee.merge(
        department, left_on="departmentId", right_on="id", suffixes=("_emp", "_dep")
    )
    peak = merged.groupby("departmentId")["salary"].transform("max")
    top = merged[merged["salary"] == peak]
    return top.rename(
        columns={"name_dep": "Department", "name_emp": "Employee", "salary": "Salary"}
    )[["Department", "Employee", "Salary"]]


def _run_checks() -> None:
    employee = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "name": ["Joe", "Jim", "Henry", "Sam"],
            "salary": [70000, 90000, 80000, 60000],
            "departmentId": [1, 1, 2, 2],
        }
    )
    department = pd.DataFrame({"id": [1, 2], "name": ["IT", "Sales"]})
    out = department_highest_salary(employee, department)
    want = pd.DataFrame(
        {
            "Department": ["IT", "Sales"],
            "Employee": ["Jim", "Henry"],
            "Salary": [90000, 80000],
        }
    )
    pd.testing.assert_frame_equal(
        out.sort_values("Department").reset_index(drop=True), want
    )
    print("✓ 184 test passed")


if __name__ == "__main__":
    _run_checks()
