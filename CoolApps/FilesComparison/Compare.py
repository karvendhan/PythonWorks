import pandas as pd
import pprint as pp
import sys

def dfDiff(oldfile,newfile,comkey):
    df1 = pd.read_csv(oldfile)
    df2 = pd.read_csv(newfile)
    sorted_df1 = df1.set_index(comkey).sort_index()
    sorted_df2 = df2.set_index(comkey).sort_index()
    dfBool = (sorted_df1 != sorted_df2).stack()
    diff = pd.concat([sorted_df1.stack()[dfBool],
                      sorted_df2.stack()[dfBool]], axis=1)
    diff.columns = ["Old", "New"]
    print(diff)

file1,file2,comkey=sys.argv[1],sys.argv[2],sys.argv[3]

dfDiff(file1,file2,comkey)

