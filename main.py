import pandas as pd


if __name__ == "__main__":
    # ans_2: the five cities' real estate data
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

    # ans_3: Merge to 1 df
    frames = [df_a, df_b, df_e, df_f, df_h]
    df_all = pd.concat(frames)
    print(f"df_all shape: {df_all.shape}")
