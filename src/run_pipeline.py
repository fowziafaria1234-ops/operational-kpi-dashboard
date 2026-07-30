from generate_data import main as generate
from clean_transform import main as clean
from build_kpis import main as kpis
from create_visuals import main as visuals
if __name__ == "__main__":
    generate(); clean(); kpis(); visuals(); print("Pipeline completed successfully.")
