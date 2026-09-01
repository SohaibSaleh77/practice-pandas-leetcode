"""2891. Method Chaining"""
import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Pure method chaining — no intermediate variables.
    return (
        animals.query("weight > 100")
        .sort_values("weight", ascending=False)
        .loc[:, ["name"]]
    )


def _run_checks() -> None:
    animals = pd.DataFrame(
        {
            "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
            "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
            "age": [98, 50, 6, 45, 100, 26],
            "weight": [464, 41, 328, 463, 50, 349],
        }
    )
    out = findHeavyAnimals(animals)
    want = pd.DataFrame({"name": ["Tatiana", "Jonathan", "Tommy", "Alex"]})
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 2891 test passed")


if __name__ == "__main__":
    _run_checks()
