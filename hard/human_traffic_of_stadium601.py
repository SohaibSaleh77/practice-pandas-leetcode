"""601. Human Traffic of Stadium"""
import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    if stadium.empty:
        return pd.DataFrame(columns=["id", "visit_date", "people"])

    busy = stadium[stadium["people"] >= 100].copy()
    if busy.shape[0] < 3:
        return pd.DataFrame(columns=["id", "visit_date", "people"])

    # Group consecutive busy days: gap in id => new group.
    busy["group"] = (busy["id"].diff() != 1).cumsum()
    counts = busy.groupby("group")["group"].transform("size")
    busy = busy[counts >= 3]
    return busy[["id", "visit_date", "people"]].sort_values("id")


def _run_checks() -> None:
    stadium = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6, 7, 8],
            "visit_date": pd.to_datetime(
                [
                    "2017-01-01", "2017-01-02", "2017-01-03", "2017-01-04",
                    "2017-01-05", "2017-01-06", "2017-01-07", "2017-01-08",
                ]
            ),
            "people": [10, 109, 150, 99, 145, 1455, 199, 188],
        }
    )
    out = human_traffic(stadium)
    want = pd.DataFrame(
        {
            "id": [5, 6, 7, 8],
            "visit_date": pd.to_datetime(
                ["2017-01-05", "2017-01-06", "2017-01-07", "2017-01-08"]
            ),
            "people": [145, 1455, 199, 188],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 601 test passed")


if __name__ == "__main__":
    _run_checks()
