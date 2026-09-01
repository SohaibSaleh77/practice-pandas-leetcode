"""2887. Fill Missing Data"""
import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Chain fill + cast to guarantee an integer dtype in one expression.
    return products.assign(quantity=products["quantity"].fillna(0).astype(int))


def _run_checks() -> None:
    products = pd.DataFrame(
        {
            "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
            "quantity": [None, None, 779, 849],
            "price": [135, 821, 9319, 3051],
        }
    )
    out = fillMissingValues(products)
    want = pd.DataFrame(
        {
            "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
            "quantity": [0, 0, 779, 849],
            "price": [135, 821, 9319, 3051],
        }
    )
    want["quantity"] = want["quantity"].astype(int)
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2887 test passed")


if __name__ == "__main__":
    _run_checks()
