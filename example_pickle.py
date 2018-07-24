import pickle as pk
import pandas as pd

# this is my main reason for using pickle
# its super useful if you want to retain structure of object and not think about it too much
# https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.to_pickle.html

example_data = {
    'col_A': [1, 2, 3, 4, 99999999],
    'col_B': [1, 2, 3, 4, 99999999],
    'col_C': [1, 2, 3, 4, 99999999],
    'col_infinity': [1, 2, 3, 4, 99999999]}

df = pd.DataFrame.from_dict(example_data)

# imageine you have some massive data and want to save a particular state of it in such a way that you can
# reload it back into that state

file_path = "example_data_at_some_state"
df.to_pickle(file_path)

df_reloaded = pd.read_pickle(file_path)

print("are these objects the same?")
if df.equals(df_reloaded):
    print("yes")
else:
    print("no")


