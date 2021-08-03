import pandas as pd
import glob

path = r'C:\Users\PC\Desktop\quinto-andar-analise\lista_urls' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv('C:/Users/PC/Desktop/quinto-andar-analise/lista_urls_pandas.csv')
