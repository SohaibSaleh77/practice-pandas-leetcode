"""178. Rank Scores"""
import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # `dense` rank so ties share the same number with no gap.
    ranked = scores.assign(
        rank=scores["score"].rank(method="dense", ascending=False).astype(int)
    )
    return ranked[["score", "rank"]].sort_values("score", ascending=False)


def _run_checks() -> None:
    scores = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5, 6], "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]}
    )
    out = order_scores(scores)
    want = pd.DataFrame(
        {
            "score": [4.00, 4.00, 3.85, 3.65, 3.65, 3.50],
            "rank": [1, 1, 2, 3, 3, 4],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 178 test passed")


if __name__ == "__main__":
    _run_checks()
