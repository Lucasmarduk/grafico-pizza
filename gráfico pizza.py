import matplotlib.pyplot as plt
from cycler import cycler
anos=[2018, 2019, 2020, 2021]
vendas_online=[5, 10, 15, 20]
vendas_lojas = [10, 8, 6, 4]
cores_cycler = cycler('color', plt.get_cmap('Pastel2').colors)
plt.rc('axes', prop_cycle=cores_cycler)
plt.bar(anos, vendas_online, label='Online')
plt.bar(anos, vendas_lojas, bottom=vendas_online, label='Loja')
# forçar os anos a serem exibidos como inteiros
plt.xticks(ticks=anos, labels=anos)
plt.xlabel('Ano')
plt.ylabel('Vendas (em milhões)')
plt.title('Vendas Online vs Loja')
plt.legend()
plt.show()

anos=[2018, 2019, 2020, 2021]
vendas_online = [5, 10, 15, 20]
plt.bar(anos, vendas_online, label='Online')
plt.xticks(ticks=anos)
plt.xlabel('Ano')
plt.ylabel('Vendas (em Milhões)')
plt.title('Vendas Online')
plt.legend()
plt.show()