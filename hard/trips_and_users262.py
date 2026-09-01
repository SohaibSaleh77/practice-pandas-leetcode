"""262. Trips and Users"""
import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    if trips.empty or users.empty:
        return pd.DataFrame(columns=["Day", "Cancellation Rate"])

    active_ids = users.loc[users["banned"] == "No", "users_id"]
    valid = trips[
        trips["client_id"].isin(active_ids) & trips["driver_id"].isin(active_ids)
    ]
    window = ["2013-10-01", "2013-10-02", "2013-10-03"]
    valid = valid[valid["request_at"].isin(window)]

    if valid.empty:
        return pd.DataFrame({"Day": window, "Cancellation Rate": [0.00, 0.00, 0.00]})

    grouped = valid.groupby("request_at")["status"].agg(
        total="count",
        cancelled=lambda s: s.str.startswith("cancelled").sum(),
    ).reset_index()
    grouped["Cancellation Rate"] = (grouped["cancelled"] / grouped["total"]).round(2)

    return (
        pd.DataFrame({"Day": window})
        .merge(grouped[["request_at", "Cancellation Rate"]], left_on="Day", right_on="request_at", how="left")
        .fillna(0.00)
        .round({"Cancellation Rate": 2})
        .loc[:, ["Day", "Cancellation Rate"]]
    )


def _run_checks() -> None:
    trips = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "client_id": [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
            "driver_id": [10, 11, 12, 13, 10, 11, 12, 11, 12, 13],
            "city_id": [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
            "status": [
                "completed", "cancelled_by_driver", "completed", "cancelled_by_client",
                "completed", "completed", "completed", "completed", "completed", "cancelled_by_driver",
            ],
            "request_at": [
                "2013-10-01", "2013-10-01", "2013-10-01", "2013-10-01", "2013-10-02",
                "2013-10-02", "2013-10-02", "2013-10-02", "2013-10-03", "2013-10-03",
            ],
        }
    )
    users = pd.DataFrame(
        {
            "users_id": [1, 2, 3, 4, 10, 11, 12, 13],
            "banned": ["No", "Yes", "No", "No", "No", "No", "No", "No"],
            "role": ["client", "client", "client", "client", "driver", "driver", "driver", "driver"],
        }
    )
    out = trips_and_users(trips, users)
    want = pd.DataFrame(
        {
            "Day": ["2013-10-01", "2013-10-02", "2013-10-03"],
            "Cancellation Rate": [0.33, 0.00, 0.50],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want.reset_index(drop=True))
    print("✓ 262 test passed")


if __name__ == "__main__":
    _run_checks()
