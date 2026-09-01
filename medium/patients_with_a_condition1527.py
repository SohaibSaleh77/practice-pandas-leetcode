"""1527. Patients With a Condition"""
import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Word boundary ensures DIAB1 is the prefix of a condition token.
    return patients[patients["conditions"].str.contains(r"\bDIAB1", regex=True)]


def _run_checks() -> None:
    patients = pd.DataFrame(
        {
            "patient_id": [1, 2, 3, 4],
            "patient_name": ["Daniel", "Alice", "Bob", "George"],
            "conditions": ["YFEV COUGH", "", "DIAB100 MYOP", "ACNE DIAB100"],
        }
    )
    out = find_patients(patients)
    want = pd.DataFrame(
        {
            "patient_id": [3, 4],
            "patient_name": ["Bob", "George"],
            "conditions": ["DIAB100 MYOP", "ACNE DIAB100"],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 1527 test passed")


if __name__ == "__main__":
    _run_checks()
