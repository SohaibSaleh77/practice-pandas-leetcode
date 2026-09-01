"""2889. Reshape Data: Pivot"""
import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")


def _run_checks() -> None:
    weather = pd.DataFrame(
        {
            "city": ["Jacksonville"] * 5 + ["ElPaso"] * 5,
            "month": ["January", "February", "March", "April", "May"] * 2,
            "temperature": [13, 23, 38, 5, 34, 20, 6, 26, 2, 43],
        }
    )
    out = pivotTable(weather)
    assert out.loc["January", "Jacksonville"] == 13
    assert out.loc["May", "ElPaso"] == 43
    print("✓ 2889 test passed")


if __name__ == "__main__":
    _run_checks()
