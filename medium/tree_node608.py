"""608. Tree Node"""
import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Vectorised type assignment: default to Leaf, then override Root/Inner.
    parents = tree["p_id"]
    has_parent = parents.notna()
    is_parent = tree["id"].isin(parents.dropna().unique())

    out = tree.copy()
    out["type"] = "Leaf"
    out.loc[~has_parent, "type"] = "Root"
    out.loc[has_parent & is_parent, "type"] = "Inner"
    return out[["id", "type"]]


def _run_checks() -> None:
    tree = pd.DataFrame({"id": [1, 2, 3, 4, 5], "p_id": [None, 1, 1, 2, 2]})
    out = tree_node(tree)
    want = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "type": ["Root", "Inner", "Leaf", "Leaf", "Leaf"],
        }
    )
    pd.testing.assert_frame_equal(out.reset_index(drop=True), want)
    print("✓ 608 test passed")


if __name__ == "__main__":
    _run_checks()
