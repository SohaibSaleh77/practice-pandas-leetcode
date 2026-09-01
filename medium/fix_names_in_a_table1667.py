"""1667. Fix Names in a Table"""
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # `str.capitalize` lowercases everything except the first character.
    users = users.copy()
    users["name"] = users["name"].str.capitalize()
    return users.sort_values("user_id")


def _run_checks() -> None:
    users = pd.DataFrame(
        {"user_id": [1, 2, 3], "name": ["aLice", "bOB", "cHARLIE"]}
    )
    out = fix_names(users)
    want = pd.DataFrame(
        {"user_id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 1667 test passed")


if __name__ == "__main__":
    _run_checks()
