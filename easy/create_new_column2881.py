"""2881. Create a New Column"""
import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # `assign` returns a new frame without mutating the caller's input.
    return employees.assign(bonus=employees["salary"] * 2)


def _run_checks() -> None:
    employees = pd.DataFrame(
        {
            "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
            "salary": [4548, 28150, 1103, 6593, 74576, 24433],
        }
    )
    out = createBonusColumn(employees)
    want = pd.DataFrame(
        {
            "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
            "salary": [4548, 28150, 1103, 6593, 74576, 24433],
            "bonus": [9096, 56300, 2206, 13186, 149152, 48866],
        }
    )
    pd.testing.assert_frame_equal(out, want)
    print("✓ 2881 test passed")


if __name__ == "__main__":
    _run_checks()
