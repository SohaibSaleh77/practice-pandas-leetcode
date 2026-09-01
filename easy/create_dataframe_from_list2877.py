"""2877. Create a DataFrame from a List"""
import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    # Build the frame in one shot and tag the columns explicitly.
    return pd.DataFrame(student_data, columns=["student_id", "age"])


def _run_checks() -> None:
    sample = [[1, 15], [2, 11], [3, 11], [4, 20]]
    out = createDataframe(sample)
    want = pd.DataFrame({"student_id": [1, 2, 3, 4], "age": [15, 11, 11, 20]})
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2877 test passed")


if __name__ == "__main__":
    _run_checks()
