"""2888. Reshape Data: Concatenate"""
import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Reset the index so the result has a clean 0..n-1 range.
    return pd.concat([df1, df2], ignore_index=True)


def _run_checks() -> None:
    df1 = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4],
            "name": ["Mason", "Ava", "Taylor", "Georgia"],
            "age": [6, 7, 16, 18],
        }
    )
    df2 = pd.DataFrame(
        {
            "student_id": [5, 6],
            "name": ["Leo", "Alex"],
            "age": [7, 21],
        }
    )
    out = concatenateTables(df1, df2)
    want = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4, 5, 6],
            "name": ["Mason", "Ava", "Taylor", "Georgia", "Leo", "Alex"],
            "age": [6, 7, 16, 18, 7, 21],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2888 test passed")


if __name__ == "__main__":
    _run_checks()
