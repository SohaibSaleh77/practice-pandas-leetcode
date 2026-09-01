"""2883. Drop Missing Data"""
import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where name is present, rather than calling .dropna().
    return students[students["name"].notna()]


def _run_checks() -> None:
    students = pd.DataFrame(
        {
            "student_id": [32, 217, 779, 849],
            "name": ["Piper", None, "Georgia", "Willow"],
            "age": [5, 19, 20, 14],
        }
    )
    out = dropMissingData(students)
    want = pd.DataFrame(
        {
            "student_id": [32, 779, 849],
            "name": ["Piper", "Georgia", "Willow"],
            "age": [5, 20, 14],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 2883 test passed")


if __name__ == "__main__":
    _run_checks()
