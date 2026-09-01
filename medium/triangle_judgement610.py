"""610. Triangle Judgement"""
import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    x, y, z = triangle["x"], triangle["y"], triangle["z"]
    is_triangle = (x + y > z) & (y + z > x) & (z + x > y)
    triangle = triangle.assign(triangle=is_triangle.map({True: "Yes", False: "No"}))
    return triangle


def _run_checks() -> None:
    triangle = pd.DataFrame(
        {"x": [13, 10, 8, 20], "y": [15, 20, 15, 20], "z": [30, 15, 20, 40]}
    )
    out = triangle_judgement(triangle)
    want = pd.DataFrame(
        {
            "x": [13, 10, 8, 20],
            "y": [15, 20, 15, 20],
            "z": [30, 15, 20, 40],
            "triangle": ["No", "Yes", "Yes", "No"],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 610 test passed")


if __name__ == "__main__":
    _run_checks()
