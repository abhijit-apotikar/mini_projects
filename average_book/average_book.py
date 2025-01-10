import pandas as pd
import sys
from generate_input import get_dataset

file1 = ''
file2 = ''

if len(sys.argv) ==  2:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

df1 = pd.read_csv(f'./{file1}' if file1 else './output1.csv')
df2 = pd.read_csv(f'./{file2}' if file2 else './output2.csv')

df_final = pd.concat([df1, df2], axis=0).reset_index(drop=True)
#print(df_final.head(n=5))
#print(df_final.shape)
new_df = df_final.groupby(['state']).sum().reset_index()
#print(new_df.head(45))
new_df.to_csv('./average_book.csv', index=False)
#print('end')
