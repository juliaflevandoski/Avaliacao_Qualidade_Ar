import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('../data/AirQualityUCI.csv', sep=';', decimal=',')
df = df.iloc[:, :-2]

for col in df.columns[2:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna()

# Heatmap de correlação apenas com variáveis numéricas
plt.figure(figsize=(12, 10))
numericas = df.select_dtypes(include='number')
sns.heatmap(numericas.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title('Mapa de Correlação entre Variáveis Numéricas')
plt.tight_layout()
plt.show()

# Histogramas de todas as variáveis numéricas
numericas.hist(bins=20, figsize=(16, 12))
plt.suptitle('Distribuição das Variáveis')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Boxplot de uma variável de exemplo (C6H6(GT))
plt.figure(figsize=(8, 6))
sns.boxplot(x=numericas['C6H6(GT)'])
plt.title('Boxplot da variável C6H6(GT)')
plt.tight_layout()
plt.show()

X = df.drop(columns=['Date', 'Time', 'CO(GT)'])  # Variáveis independentes
y = df['CO(GT)']                                 # Variável alvo

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Erro Quadrático Médio (MSE): {mse:.3f}")
print(f"Coeficiente de Determinação (R²): {r2:.3f}")

# Gráfico Real vs Previsto
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('CO(GT) Real')
plt.ylabel('CO(GT) Previsto')
plt.title('Gráfico Real vs Previsto')
plt.tight_layout()
plt.show()

# Gráfico de Resíduos
residuos = y_test - y_pred
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuos, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('CO(GT) Previsto')
plt.ylabel('Resíduos')
plt.title('Gráfico de Resíduos')
plt.tight_layout()
plt.show()