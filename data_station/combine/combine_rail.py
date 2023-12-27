import pandas as pd

df1 = pd.read_csv("../data/bts/bts_su_station.csv")
df2 = pd.read_csv("../data/bts/bts_si_station.csv")
df3 = pd.read_csv("../data/bts/bts_g_station.csv")
df4 = pd.read_csv("../data/arl/arl_station.csv")
df5 = pd.read_csv("../data/mrt/mrt_b_station.csv")
df6 = pd.read_csv("../data/mrt/mrt_p_station.csv")
df7 = pd.read_csv("../data/mrt/mrt_y_station.csv")
df8 = pd.read_csv("../data/mrt/mrt_pi_station.csv")
# df8 = df8.rename(columns={"stopid": "sid"})
df_list = [df4, df1, df2, df3, df5, df6, df7, df8]
for i in range(len(df_list)):
    df_list[i] = df_list[i].rename(columns={"sid": "stopid"})
combined_df = pd.concat(
    df_list,
    axis=0,
)
combined_df.to_csv("../data/rail_station.csv", index=False)
