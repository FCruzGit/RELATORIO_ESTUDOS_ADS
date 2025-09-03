import pandas as pd
import numpy as np

# ATV CIDADE AURORA DADOS NO DATAFRAME
df = pd.DataFrame({
    "idade": [25, 30, 42, 55, 28, 35, 60, 22, 48, 33],
    "renda_anual": [45, 60, 85, 110, 50, 70, 130, 40, 95, 65]
})

# Calculo das Médias de Idade e Renda
Xm = df["idade"].mean()
Ym = df["renda_anual"].mean()

print(f"A média de idade na cidade aurora é {Xm} e renda(milhares) {Ym} anual")

# Numerador e denominador do β1 (Coeficiente Angular)
numerador_b1 = ((df["idade"] - Xm) * (df["renda_anual"] - Ym)).sum()
denominador_b1 = ((df["idade"] - Xm) ** 2).sum()

beta1 = numerador_b1 / denominador_b1
print(f"Valor do Coeficiente angular {beta1}")

# Calculo de β0 (Intercepto)
beta0 = Ym - beta1 * Xm
print(f"Valor do Intercepto {beta0}")

# Estimativa do valor de Y final
Xf = 100
Yf = beta0 + beta1 * Xf

print(f"A renda estimada de uma pessoa com {Xf} anos é de {Yf}")