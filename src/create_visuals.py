from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
ROSE="#E11D48"; PINK="#EC4899"; BURGUNDY="#881337"
def main():
    df=pd.read_csv(ROOT/'data/processed/operations_clean.csv',parse_dates=['date'])
    kpi=pd.read_csv(ROOT/'data/processed/kpi_monthly.csv')
    out=ROOT/'assets'; out.mkdir(exist_ok=True)
    plt.figure(figsize=(10,5)); plt.plot(kpi.month,kpi.attainment_rate*100,marker='o',color=ROSE); plt.axhline(100,ls='--',color=BURGUNDY); plt.xticks(rotation=45); plt.ylabel('Target attainment (%)'); plt.title('Monthly target attainment'); plt.tight_layout(); plt.savefig(out/'kpi-attainment.png',dpi=160); plt.close()
    plt.figure(figsize=(10,5)); df.groupby('site').defect_rate.mean().sort_values().mul(100).plot(kind='bar',color=PINK); plt.ylabel('Average defect rate (%)'); plt.xticks(rotation=0); plt.title('Quality performance by site'); plt.tight_layout(); plt.savefig(out/'site-quality.png',dpi=160); plt.close()
if __name__=='__main__': main()
