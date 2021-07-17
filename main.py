import pandas as pd


if __name__ == "__main__":
    # ans_2
    df_a = pd.read_csv(r"raw_data\a_lvr_land_a.csv")
    df_b = pd.read_csv(r"raw_data\b_lvr_land_a.csv")
    df_e = pd.read_csv(r"raw_data\e_lvr_land_a.csv")
    df_f = pd.read_csv(r"raw_data\f_lvr_land_a.csv")
    df_h = pd.read_csv(r"raw_data\h_lvr_land_a.csv")

    print(df_a.head())
    print(df_a.shape)
    print(df_b.shape)
    print(df_e.shape)
    print(df_f.shape)
    print(df_h.shape)
