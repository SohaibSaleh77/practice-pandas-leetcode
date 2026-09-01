"""196. Delete Duplicate Emails"""
import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Mutate in place: lowest id wins per email.
    person.sort_values("id", inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)


def _run_checks() -> None:
    person = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "email": ["john@example.com", "bob@example.com", "john@example.com"],
        }
    )
    delete_duplicate_emails(person)
    want = pd.DataFrame(
        {"id": [1, 2], "email": ["john@example.com", "bob@example.com"]}
    )
    pd.testing.assert_frame_equal(person.reset_index(drop=True), want)
    print("✓ 196 test passed")


if __name__ == "__main__":
    _run_checks()
