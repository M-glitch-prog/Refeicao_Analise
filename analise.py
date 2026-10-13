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

print (dados.info())
consumo= dados["quantidade_consumida"].mean()
maior_desperdicio=dados["desperdicio_estimado"].max()
apareceu=(dados["refeicao"].value_counts())

relatorio=f"""
Relatorio de Análise de Dados - Refeições Escolares
1. A média de consumo estimado de acordo com a análise de dados referente à planilha: {consumo}
2. O maior desperdício estimado de acordo com a análise de dados referente à planilha       : {maior_desperdicio}
3. A quantidade de vezes que cada refeição apareceu de acordo com a análise de dados referente à planilha: {apareceu.to_dict()}
"""
with open("relatorio.txt", "w") as arquivo:
    arquivo.write(relatorio)
