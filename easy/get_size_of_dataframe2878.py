"""2878. Get the Size of a DataFrame"""
import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    rows, cols = players.shape
    return [rows, cols]


def _run_checks() -> None:
    players = pd.DataFrame(
        {
            "player_id": [846, 749, 155, 583],
            "name": ["Mason", "Riley", "Bob", "Isabella"],
            "age": [21, 30, 28, 25],
        }
    )
    assert getDataframeSize(players) == [4, 3]
    print("✓ 2878 test passed")


if __name__ == "__main__":
    _run_checks()
