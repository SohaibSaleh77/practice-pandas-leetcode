"""1873. Calculate Special Bonus"""
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Bonus = salary if odd employee_id AND name doesn't start with 'M', else 0.
    odd_id = employees["employee_id"] % 2 == 1
    not_m = ~employees["name"].str.startswith("M")
    employees = employees.assign(
        bonus=(odd_id & not_m).astype(int) * employees["salary"]
    )
    return employees[["employee_id", "bonus"]].sort_values("employee_id")


def _run_checks() -> None:
    employees = pd.DataFrame(
        {
            "employee_id": [2, 3, 7, 8, 9],
            "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
            "salary": [3000, 3800, 7400, 6100, 7700],
        }
    )
    out = calculate_special_bonus(employees)
    want = pd.DataFrame(
        {"employee_id": [2, 3, 7, 8, 9], "bonus": [0, 0, 7400, 0, 7700]}
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 1873 test passed")


if __name__ == "__main__":
    _run_checks()
