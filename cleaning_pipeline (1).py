import pandas as pd
import numpy as np

def clean_agent_data(txns, agents):
    """Clean transactions and merge agent information. Returns (clean_df, log)."""
    log = []
    out = txns.copy()

    before = len(out)
    out = out.drop_duplicates(subset="txn_id").copy()
    log.append(f"Removed {before - len(out)} duplicate transactions")

    out["txn_type"] = out["txn_type"].astype("string").str.strip().str.title()
    out = out[out["txn_type"].isin(["Deposit", "Withdrawal"])].copy()

    out["amount"] = pd.to_numeric(
        out["amount"].astype("string").str.replace(",", "", regex=False),
        errors="coerce"
    )
    out["amount_imputed"] = out["amount"].isna()

    median_amount = out["amount"].median()
    if pd.isna(median_amount):
        median_amount = 0
    out["amount"] = out["amount"].fillna(median_amount)

    out["txn_date"] = pd.to_datetime(out["txn_date"], errors="coerce")
    out = out.dropna(subset=["txn_date"]).copy()

    q1, q3 = out["amount"].quantile([0.25, 0.75])
    out["is_outlier"] = out["amount"] > q3 + 1.5 * (q3 - q1)

    out = out.merge(
        agents[["agent_id", "county"]],
        on="agent_id",
        how="left",
        validate="many_to_one"
    )

    log.append(f"Transactions remaining: {len(out)}")
    log.append(f"Unknown agent transactions: {out['county'].isna().sum()}")

    return out, log
