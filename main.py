# Retirar colunas que não serão utilizadas;
# Normalizar os dados e inserir/substituir se necessário
# Trazer as 5 maiores notas das salas
# Trazer as 5 menores notas das salas
# Trazer a média da sala
# Mostrar em um gráfico de barra vertical quantidade temos de cada nota.
# Mostrar um boxplot de cada avaliação (MA, AM, AB, MB)
# Descrever em um relatório textual a situação dos 5 alunos com menor nota com base na análise dos dados (por que o desempenho deles está assim, e o que provavelmente pode ter acontecido/como melhorar)

import pandas as pd

alunos = pd.read_csv('dataset-alunos.csv')

print(alunos)