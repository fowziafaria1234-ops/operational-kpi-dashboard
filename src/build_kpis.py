from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]

def main() -> pd.DataFrame:
    df = pd.read_csv(ROOT / "data/processed/operations_clean.csv", parse_dates=["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)
    kpi = df.groupby("month").agg(units=("units_processed","sum"),target=("target_units","sum"),defects=("defects","sum"),downtime=("downtime_minutes","sum"),on_time_rate=("on_time_flag","mean"),revenue=("revenue_gbp","sum"),margin=("gross_margin_gbp","sum")).reset_index()
    kpi["attainment_rate"] = kpi["units"] / kpi["target"]
    kpi["defect_rate"] = kpi["defects"] / kpi["units"]
    kpi.to_csv(ROOT / "data/processed/kpi_monthly.csv", index=False)
    return kpi
if __name__ == "__main__": main()
