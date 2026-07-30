from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]

def main() -> pd.DataFrame:
    df = pd.read_csv(ROOT / "data/raw/operations_raw.csv")
    df = df.drop_duplicates("transaction_id").copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["units_processed"] = pd.to_numeric(df["units_processed"], errors="coerce")
    df["site"] = df["site"].fillna("Unknown")
    df["data_quality_flag"] = np.where(df[["date","units_processed"]].isna().any(axis=1), "REVIEW", "PASS")
    df = df.dropna(subset=["date","units_processed"]).copy()
    df["units_processed"] = df["units_processed"].astype(int)
    df["variance_units"] = df["units_processed"] - df["target_units"]
    df["defect_rate"] = df["defects"] / df["units_processed"]
    df["productivity_units_per_hour"] = df["units_processed"] / df["labour_hours"]
    df["gross_margin_gbp"] = df["revenue_gbp"] - df["cost_gbp"]
    out = ROOT / "data/processed/operations_clean.csv"; out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    return df
if __name__ == "__main__": main()
