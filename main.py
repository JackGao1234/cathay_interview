import os
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
    filter_a = filtered_df[filtered_df.apply(gte_13_floors, axis=1)]
    print(f"總樓層數>=十三層: {filter_a.shape}")
    print(filter_a.head())

    if not os.path.exists("result"):
        os.makedirs("result")

    filter_a.to_csv(f"result/filter_a.csv", index=False)


    print("==== filter_b.csv ====")
    # 計算總件數
    count = filter_a.shape[0]
    print(f"計算總件數={count}")

    # 總車位數
    parking_space_series = filter_a["交易筆棟數"].str.split('車位').str[-1].astype(int)
    # print(parking_space_series.head())
    parking_spaces = parking_space_series.sum()
    print(f"總車位數={parking_spaces}")

    # 平均總價元
    avg_price = filter_a['總價元'].mean()
    print(f"平均總價元={avg_price}")

    # 平均車位總價元
    avg_parking_space_price = filter_a['車位總價元'].sum() / parking_spaces
    print(f"平均車位總價元={avg_parking_space_price}")

    filter_b = pd.DataFrame({'計算總件數': pd.Series([], dtype='int'),
                             '總車位數': pd.Series([], dtype='int'),
                             '平均總價元': pd.Series([], dtype='float'),
                             '平均車位總價元': pd.Series([], dtype='float')})
    filter_b.loc[-1] = [count, parking_spaces, avg_price, avg_parking_space_price]
    print(filter_b.head(5))
    print(filter_b.dtypes)
    filter_b.to_csv(f"result/filter_b.csv", index=False)
