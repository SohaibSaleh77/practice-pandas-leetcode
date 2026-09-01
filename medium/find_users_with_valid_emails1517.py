"""1517. Find Users With Valid Emails"""
import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Prefix must start with a letter, then word/._- characters, ending @leetcode.com.
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"
    return users[users["mail"].str.match(pattern)]


def _run_checks() -> None:
    users = pd.DataFrame(
        {
            "user_id": [1, 2, 3, 4],
            "name": ["Winston", "Jonathan", "Annabelle", "Sally"],
            "mail": [
                "winston@leetcode.com",
                "jonathanisgreat",
                "bella-@leetcode.com",
                "sally.come@leetcode.com",
            ],
        }
    )
    out = valid_emails(users)
    want = pd.DataFrame(
        {
            "user_id": [1, 3, 4],
            "name": ["Winston", "Annabelle", "Sally"],
            "mail": [
                "winston@leetcode.com",
                "bella-@leetcode.com",
                "sally.come@leetcode.com",
            ],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 1517 test passed")


if __name__ == "__main__":
    _run_checks()
