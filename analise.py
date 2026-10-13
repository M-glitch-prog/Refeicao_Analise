import pandas as pd
dados=pd.read_excel('refeicoes_escola.xlsx')
import matplotlib.pyplot as plt
dados=pd.read_excel('refeicoes_escola.xlsx')
consumo=dados["refeicao"].value_counts()
consumo.plot(kind="bar")
plt.title("Refeições Escolares")
plt.xlabel("Refeições")
plt.ylabel("Quantidade")
plt.show()
