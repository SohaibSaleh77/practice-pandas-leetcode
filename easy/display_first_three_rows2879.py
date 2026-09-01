"""2879. Display the First Three Rows"""
import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # `.iloc` is the most explicit way to slice by position.
    return employees.iloc[:3]


def _run_checks() -> None:
    employees = pd.DataFrame(
        {
            "employee_id": [3, 90, 9, 60, 49],
            "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan"],
            "department": [
                "Operations",
                "Sales",
                "Engineering",
                "InformationTechnology",
                "HumanResources",
            ],
            "salary": [48675, 11096, 33805, 37678, 23793],
        }
    )
    out = selectFirstRows(employees)
    pd.testing.assert_frame_equal(out.reset_index(drop=True), employees.head(3).reset_index(drop=True))
    print("✓ 2879 test passed")


if __name__ == "__main__":
    _run_checks()
