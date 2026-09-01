"""607. Sales Person"""
import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    red_ids = company.loc[company["name"] == "RED", "com_id"]
    if red_ids.empty:
        return sales_person[["name"]]
    sellers_for_red = orders.loc[orders["com_id"].isin(red_ids), "sales_id"].unique()
    return sales_person[~sales_person["sales_id"].isin(sellers_for_red)][["name"]]


def _run_checks() -> None:
    sp = pd.DataFrame(
        {
            "sales_id": [1, 2, 3, 4, 5],
            "name": ["John", "Amy", "Mark", "Pam", "Alex"],
            "salary": [100000, 12000, 65000, 25000, 5000],
            "commission_rate": [6, 5, 12, 25, 10],
            "hire_date": ["4/1/2006", "5/1/2010", "12/25/2008", "1/1/2005", "2/3/2007"],
        }
    )
    co = pd.DataFrame(
        {
            "com_id": [1, 2, 3, 4],
            "name": ["RED", "ORANGE", "YELLOW", "GREEN"],
            "city": ["Boston", "New York", "Boston", "Austin"],
        }
    )
    od = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "order_date": ["1/1/2014", "2/1/2014", "3/1/2014", "4/1/2014"],
            "com_id": [3, 4, 1, 1],
            "sales_id": [4, 5, 1, 4],
            "amount": [10000, 5000, 50000, 20000],
        }
    )
    out = sales_person(sp, co, od)
    want = pd.DataFrame({"name": ["Amy", "Mark", "Alex"]})
    pd.testing.assert_frame_equal(
        out.sort_values("name").reset_index(drop=True),
        want.sort_values("name").reset_index(drop=True),
    )
    print("✓ 607 test passed")


if __name__ == "__main__":
    _run_checks()
