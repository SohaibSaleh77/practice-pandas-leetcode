"""2885. Rename Columns"""
import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    mapping = {
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years",
    }
    return students.rename(columns=mapping)


def _run_checks() -> None:
    students = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "first": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
            "last": ["King", "Wright", "Hall", "Thompson", "Moore"],
            "age": [6, 7, 16, 18, 10],
        }
    )
    out = renameColumns(students)
    want = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4, 5],
            "first_name": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
            "last_name": ["King", "Wright", "Hall", "Thompson", "Moore"],
            "age_in_years": [6, 7, 16, 18, 10],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2885 test passed")


if __name__ == "__main__":
    _run_checks()
