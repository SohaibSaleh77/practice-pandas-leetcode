"""2886. Change Data Type"""
import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Cast explicitly to standard int64 to avoid downcasting side-effects.
    students["grade"] = students["grade"].astype(int)
    return students


def _run_checks() -> None:
    students = pd.DataFrame(
        {
            "student_id": [1, 2],
            "name": ["Ava", "Kate"],
            "age": [6, 15],
            "grade": [73.0, 87.0],
        }
    )
    out = changeDatatype(students)
    want = pd.DataFrame(
        {
            "student_id": [1, 2],
            "name": ["Ava", "Kate"],
            "age": [6, 15],
            "grade": [73, 87],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2886 test passed")


if __name__ == "__main__":
    _run_checks()
