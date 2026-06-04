import pandas as pd, glob

pd.concat(
    [pd.read_csv(f, encoding='latin1') for f in sorted(glob.glob("CSV_FILES\\SRT-ABC-0*.csv"))]).to_csv(
    "CSV_FILES\\SRT_consolidados.csv", index=False)

print(" Listo: SRT_consolidados.csv")

