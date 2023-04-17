import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

# df = pd.read_csv("data.csv")
# df.to_feather("data.feather")
df = pd.read_feather("data.feather")

print(df.columns)

# print(df["LC_TEMP_QCL1"].describe())
# print(df["LC_TEMP_QCL2"].describe())
# print(df["LC_TEMP_QCL3"].describe())

print(df["LC_DAILYRAIN"].describe())
# sns.lineplot(data=df, x=range(len(df)), y="LC_DAILYRAIN")

sns.lineplot(data=df, x="Month", y="LC_WINDSPEED")
# sns.lineplot(data=df, x="Day", y="LC_WINDSPEED")
# sns.lineplot(data=df, x="Hour", y="LC_WINDSPEED")
# sns.lineplot(data=df, x="Minute", y="LC_WINDSPEED")
# sns.lineplot(data=df, x=range(len(df)), y="LC_WINDSPEED")
plt.show()

# print(df.columns)
# df["LC_TEMP_QCL1"].describe()
# print(df)

# sns.lineplot(data=df, x=range(len(df)), y="LC_TEMP_QCL3")
# plt.show()
