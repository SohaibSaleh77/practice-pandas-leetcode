"""183. Customers Who Never Order"""
import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Anti-join via set membership: customers whose id is NOT in orders.customerId.
    no_orders = ~customers["id"].isin(orders["customerId"])
    return customers.loc[no_orders, ["name"]].rename(columns={"name": "Customers"})


def _run_checks() -> None:
    customers = pd.DataFrame(
        {"id": [1, 2, 3, 4], "name": ["Joe", "Henry", "Sam", "Max"]}
    )
    orders = pd.DataFrame({"id": [1, 2], "customerId": [3, 1]})
    out = find_customers(customers, orders)
    want = pd.DataFrame({"Customers": ["Henry", "Max"]})
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 183 test passed")


if __name__ == "__main__":
    _run_checks()
