"""511. Game Play Analysis I"""
import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # First login = minimum event_date per player.
    first_login = activity.groupby("player_id", as_index=False)["event_date"].min()
    return first_login.rename(columns={"event_date": "first_login"})


def _run_checks() -> None:
    activity = pd.DataFrame(
        {
            "player_id": [1, 1, 2, 3, 3],
            "device_id": [2, 2, 3, 1, 4],
            "event_date": pd.to_datetime(
                ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"]
            ),
            "games_played": [5, 6, 1, 0, 5],
        }
    )
    out = game_analysis(activity)
    want = pd.DataFrame(
        {
            "player_id": [1, 2, 3],
            "first_login": pd.to_datetime(
                ["2016-03-01", "2017-06-25", "2016-03-02"]
            ),
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 511 test passed")


if __name__ == "__main__":
    _run_checks()
