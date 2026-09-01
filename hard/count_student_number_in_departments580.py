"""580. Count Student Number in Departments"""
import pandas as pd


def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if department.empty:
        return pd.DataFrame(columns=["dept_name", "student_number"])

    if student.empty:
        counts = pd.DataFrame(columns=["dept_id", "student_number"])
    else:
        counts = (
            student.groupby("dept_id").size().reset_index(name="student_number")
        )

    merged = department.merge(counts, on="dept_id", how="left")
    merged["student_number"] = merged["student_number"].fillna(0).astype(int)
    merged = merged.sort_values(
        ["student_number", "dept_name"], ascending=[False, True]
    )
    return merged[["dept_name", "student_number"]].reset_index(drop=True)


def _run_checks() -> None:
    student = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4, 5],
            "student_name": ["Jack", "Jane", "Mark", "Ann", "Joe"],
            "gender": ["M", "F", "M", "F", "M"],
            "dept_id": [1, 1, 2, 3, 4],
        }
    )
    department = pd.DataFrame(
        {
            "dept_id": [1, 2, 3, 4, 5],
            "dept_name": ["Engineering", "Science", "Law", "Arts", "Music"],
        }
    )
    out = count_students(student, department)
    want = pd.DataFrame(
        {
            "dept_name": ["Engineering", "Arts", "Law", "Science", "Music"],
            "student_number": [2, 1, 1, 1, 0],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 580 test passed")


if __name__ == "__main__":
    _run_checks()
