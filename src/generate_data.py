"""Generate reproducible synthetic operations data for the portfolio demo."""
from pathlib import Path
import math
import numpy as np
import pandas as pd

SEED = 202604
OUT = Path(__file__).resolve().parents[1] / "data" / "raw" / "operations_raw.csv"

def main() -> None:
    rng = np.random.default_rng(SEED)
    dates = pd.date_range("2025-01-01", "2026-05-31", freq="D")
    sites = ["Sheffield", "Leeds", "Manchester", "Nottingham"]
    products = ["Alpha", "Beta", "Gamma", "Delta"]
    departments = ["Assembly", "Quality", "Packing", "Dispatch"]
    rows = []
    for i in range(1600):
        date = pd.Timestamp(rng.choice(dates))
        site = rng.choice(sites, p=[.30, .24, .25, .21])
        product = rng.choice(products)
        department = rng.choice(departments)
        target = int(rng.integers(70, 180))
        seasonal = 1 + .08 * math.sin(date.month / 12 * 2 * math.pi)
        units = max(20, int(rng.normal(target * seasonal, target * .13)))
        defects = max(0, int(rng.poisson(max(.4, units * (.018 + (.009 if site == "Manchester" else 0))))))
        downtime = max(0, int(rng.gamma(2.0, 7.0) + (10 if department == "Assembly" else 0)))
        labour = round(max(2, rng.normal(units / 13, 1.1)), 2)
        on_time = int((units >= target * .9) and downtime < 35)
        cost = round(units * rng.uniform(4.8, 7.6) + downtime * rng.uniform(1.2, 2.8), 2)
        revenue = round(units * rng.uniform(8.5, 12.8), 2)
        rows.append([f"TXN-{i+1:05d}", date.date(), site, department, product, units, target, defects, downtime, labour, on_time, cost, revenue, "OK"])
    df = pd.DataFrame(rows, columns=["transaction_id","date","site","department","product_line","units_processed","target_units","defects","downtime_minutes","labour_hours","on_time_flag","cost_gbp","revenue_gbp","data_quality_flag"])
    for idx in rng.choice(df.index, 22, replace=False): df.loc[idx, "site"] = None
    df["units_processed"] = df["units_processed"].astype(object)
    for idx in rng.choice(df.index, 18, replace=False): df.loc[idx, "units_processed"] = "missing"
    for idx in rng.choice(df.index, 14, replace=False): df.loc[idx, "date"] = "31/13/2025"
    df = pd.concat([df, df.iloc[:8]], ignore_index=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"Wrote {len(df):,} raw rows to {OUT}")

if __name__ == "__main__":
    main()
