import pandas as pd

def test_kpi_ranges():
    df = pd.read_csv("data/processed/kpi_monthly.csv")
    assert df["attainment_rate"].between(0.5, 1.5).all()
    assert df["defect_rate"].between(0, 0.2).all()
    assert df["on_time_rate"].between(0, 1).all()
