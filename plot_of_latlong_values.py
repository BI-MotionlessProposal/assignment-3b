import glob
import pandas as pd
import os

filenames = glob.glob(os.path.join("./osm_node_data_per_zipcode","*.csv"))
print(filenames)
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)

big_frame.head()