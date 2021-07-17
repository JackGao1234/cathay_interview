import pandas as pd


if __name__ == "__main__":
    # ans_2: the five cities' real estate data
    print("==== ans 2 ====")
    df_a = pd.read_csv(r"raw_data\a_lvr_land_a.csv", skiprows=[1])
    df_b = pd.read_csv(r"raw_data\b_lvr_land_a.csv", skiprows=[1])
    df_e = pd.read_csv(r"raw_data\e_lvr_land_a.csv", skiprows=[1])
    df_f = pd.read_csv(r"raw_data\f_lvr_land_a.csv", skiprows=[1])
    df_h = pd.read_csv(r"raw_data\h_lvr_land_a.csv", skiprows=[1])

    print(f"preview: {df_a.head()}")
    print(f"df_a: {df_a.shape}")
    print(f"df_b: {df_b.shape}")
    print(f"df_e: {df_e.shape}")
    print(f"df_f: {df_f.shape}")
    print(f"df_h: {df_h.shape}")

    # ans_3: Merge to 1 df
    print("\n==== ans 3 ====")
    frames = [df_a, df_b, df_e, df_f, df_h]
    df_all = pd.concat(frames)
    print(f"df_all: {df_all.shape}")

    # ans_4: filtering
    print("==== ans 4 ====")
    filtered_df = df_all.loc[df_all["主要用途"] == "住家用"]
    print(f"主要用途==住家用: {filtered_df.shape}")

    # print(filtered_df["建物型態"].unique()) # to see all available values
    filtered_df = filtered_df.loc[filtered_df["建物型態"].str.startswith('住宅大樓')]
    print(f"建物型態==住宅大樓: {filtered_df.shape}")

    def gte_13_floors(row):
        #  possible values of row['總樓層數']
        #  五層' '七層' '十四層' '十三層' '九層' '十層' '四層' '十二層' '十九層' '十八層' '八層' '六層' '十五層'
        #  '二十六層' '二層' '三層' '二十層' '二十七層' '二十八層' '十六層' '十一層' '二十一層' '一層' '十七層' '四十二層'
        #  '二十三層' '三十八層' '二十二層' '二十四層' nan
        floor_in_chinese = row['總樓層數']
        if len(floor_in_chinese) <= 2:
            return False
        if floor_in_chinese in ["十一層", "十二層"]:
            return False
        return True


    filtered_df['總樓層數'] = filtered_df['總樓層數'].astype(str)
    result = filtered_df[filtered_df.apply(gte_13_floors, axis=1)]
    print(f"總樓層數>=十三層: {result.shape}")

    print(result.head())
