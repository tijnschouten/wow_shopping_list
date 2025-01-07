import pandas as pd
import re

def parse_shopping_list(raw_shopping_list):
    p = re.compile(r"([0-9]+)x ([^\(\-\n]+)")
    return pd.DataFrame(p.findall(raw_shopping_list), columns=["Amount", "Commodity"])

def export_auctionator(df):
    lines = [f"\"{commodity}\";;0;0;0;0;0;0;0;0;;#;;{amount}" for i, (amount, commodity) in df.iterrows()]
    return "^".join(["export"] + lines)

def export_tsm(df):
    lines = [f"{commodity}/exact/x{amount}" for i, (amount, commodity) in df.iterrows()]
    return ";".join(lines)



