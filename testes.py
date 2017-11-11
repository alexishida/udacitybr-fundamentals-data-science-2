import pandas as pd

# create a very simple dataframe
df = pd.DataFrame({'col 1':[1, 2, 3], 'col 2': [4, 5, 6]})

# add the third column
df['col 3'] = [7, 8]

# the end result
print df