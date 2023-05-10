import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

df_41 = pd.read_csv("noise_april_41.csv", sep=';')
df_41.to_feather("noise_april_41.feather")
df_41 = pd.read_feather("noise_april_41.feather")

# df_42 = pd.read_csv("noise_april_42.csv", sep=';')
# df_42.to_feather("noise_april_42.feather")
# df_42 = pd.read_feather("noise_april_42.feather")

# print(df_41.columns)
# print(len(df_41.index))
# print(df_42.columns)

print(df_41['lamax'].describe())

# filtered_df = df_41[df_41['lamax'] > 85]

sns.scatterplot(data=df_41, x=df_41.index, y=df_41['lamax'])
plt.axhline(y=85, color='r', linestyle='-')
plt.show()

