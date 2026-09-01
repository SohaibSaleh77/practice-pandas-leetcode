"""2882. Drop Duplicate Rows"""
import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Keep the first occurrence per email address.
    return customers.drop_duplicates(subset=["email"], keep="first")


def _run_checks() -> None:
    customers = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4, 5, 6],
            "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
            "email": [
                "emily@example.com",
                "michael@example.com",
                "sarah@example.com",
                "john@example.com",
                "john@example.com",
                "alice@example.com",
            ],
        }
    )
    out = dropDuplicateEmails(customers)
    want = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4, 6],
            "name": ["Ella", "David", "Zachary", "Alice", "Violet"],
            "email": [
                "emily@example.com",
                "michael@example.com",
                "sarah@example.com",
                "john@example.com",
                "alice@example.com",
            ],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 2882 test passed")


if __name__ == "__main__":
    _run_checks()
