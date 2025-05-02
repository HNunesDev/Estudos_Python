import pandas as pd
import matplotlib.pyplot as plt

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

df = pd.DataFrame(vendas_2022, index=lojas)
df.index.name = 'Lojas'
# print(df)

fig, axs = plt.subplots(2, 2, figsize=(14, 8))
axs[0, 0].plot(df.columns, df.loc['A'], color='blue')

axs[0, 1].plot(df.columns, df.loc['B'], color='blue')

axs[1, 0].plot(df.columns, df.loc['C'], color='blue')

axs[1, 1].plot(df.columns, df.loc['D'], color='blue')

ymin = 20
ymax = 450
cores = ['darkviolet', 'green', 'darkblue', 'coral']
for i, ax in enumerate(axs.flat):
    ax.plot(df.loc[df.index[i]], color=cores[i], lw=3)
    ax.set_title(f'Vendas na loja {df.index[i]}', loc='left', fontsize=16)
    ax.set_xlabel('Mês', fontsize=14)
    ax.set_ylabel('Número de vendas', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.grid(color='lightgrey')

plt.subplots_adjust(wspace=0.3, hspace=0.4)

fig.suptitle('Vendas por Loja em 2022')
plt.show()



