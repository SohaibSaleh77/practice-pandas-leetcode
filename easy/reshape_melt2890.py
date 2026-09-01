"""2890. Reshape Data: Melt"""
import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        report,
        id_vars=["product"],
        var_name="quarter",
        value_name="sales",
    )


def _run_checks() -> None:
    report = pd.DataFrame(
        {
            "product": ["Umbrella", "SleepingBag"],
            "quarter_1": [417, 800],
            "quarter_2": [224, 936],
            "quarter_3": [379, 93],
            "quarter_4": [611, 875],
        }
    )
    out = meltTable(report)
    want = pd.DataFrame(
        {
            "product": ["Umbrella", "SleepingBag"] * 4,
            "quarter": [
                "quarter_1", "quarter_1",
                "quarter_2", "quarter_2",
                "quarter_3", "quarter_3",
                "quarter_4", "quarter_4",
            ],
            "sales": [417, 800, 224, 936, 379, 93, 611, 875],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2890 test passed")


if __name__ == "__main__":
    _run_checks()
