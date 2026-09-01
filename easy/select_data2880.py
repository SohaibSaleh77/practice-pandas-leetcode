"""2880. Select Data"""
import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    mask = students["student_id"] == 101
    return students.loc[mask, ["name", "age"]]


def _run_checks() -> None:
    students = pd.DataFrame(
        {
            "student_id": [101, 53, 128, 3],
            "name": ["Ulysses", "William", "Henry", "Henry"],
            "age": [13, 10, 6, 11],
        }
    )
    out = selectData(students)
    want = pd.DataFrame({"name": ["Ulysses"], "age": [13]})
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 2880 test passed")


if __name__ == "__main__":
    _run_checks()
