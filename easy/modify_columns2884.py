"""2884. Modify Columns"""
import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # In-place doubling keeps the original frame's identity.
    employees["salary"] = employees["salary"] * 2
    return employees


def _run_checks() -> None:
    employees = pd.DataFrame(
        {
            "name": ["Jack", "Piper", "Mia", "Ulysses"],
            "salary": [19666, 74754, 62509, 54866],
        }
    )
    out = modifySalaryColumn(employees)
    want = pd.DataFrame(
        {
            "name": ["Jack", "Piper", "Mia", "Ulysses"],
            "salary": [39332, 149508, 125018, 109732],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2884 test passed")


if __name__ == "__main__":
    _run_checks()
