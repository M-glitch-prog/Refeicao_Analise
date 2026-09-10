import pandas as pd
dados=pd.read_excel('refeicoes_escola.xlsx')
print(dados["repetiu"].value_counts())
