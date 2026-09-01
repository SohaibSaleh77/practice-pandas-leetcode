"""1757. Recyclable and Low Fat Products"""
import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Both flags must be 'Y'. Pull just the product_id column.
    keep = (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    return products.loc[keep, ["product_id"]]


def _run_checks() -> None:
    products = pd.DataFrame(
        {
            "product_id": [0, 1, 2, 3, 4],
            "low_fats": ["Y", "Y", "N", "Y", "N"],
            "recyclable": ["N", "Y", "Y", "Y", "N"],
        }
    )
    out = find_products(products)
    want = pd.DataFrame({"product_id": [1, 3]})
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 1757 test passed")


if __name__ == "__main__":
    _run_checks()
