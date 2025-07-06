# 📊 Análise de Qualidade do Ar com Mineração de Dados

Este projeto tem como objetivo aplicar técnicas de mineração de dados em um conjunto de dados reais sobre qualidade do ar, utilizando Python e bibliotecas de ciência de dados. O trabalho faz parte da disciplina de Tópicos Especiais em Computação.

---

### 📌 Sobre o Dataset

* **Nome:** `AirQualityUCI.csv`
* **Origem:** UCI Machine Learning Repository ([Link direto](https://archive.ics.uci.edu/ml/datasets/Air+Quality))
* **Descrição:** Este conjunto de dados contém medições de poluentes atmosféricos coletadas em uma estação de monitoramento na cidade de Milão (Itália), entre março de 2004 e abril de 2005. As medições foram feitas a cada hora e incluem variáveis como CO, NOx, C6H6, temperatura e umidade relativa.

---

### 🎯 Objetivo

Prever a concentração de monóxido de carbono (CO) com base em outras variáveis ambientais, utilizando **regressão linear** como técnica de mineração de dados.

---

### 🧪 Tecnologias Utilizadas

* Python 3.13.5
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* PyCharm (Ambiente de Desenvolvimento)

---

### 🧭 Estrutura do Projeto

```
Avaliacao_Qualidade_Ar/
├── data/
│   └── AirQualityUCI.csv
├── src/
│   └── air_quality_analysis.py
├── reports/
│   └── Julia_Levandoski_T20233.pdf
└── README.md
```

---

## ⚙️ Como Executar a Análise

### 1. Clone o Repositório

```bash
git clone https://github.com/juliaflevandoski/Avaliacao_Qualidade_Ar
cd Avaliacao_Qualidade_Ar
```

### 2. Crie um Ambiente Virtual (Opcional, mas recomendado)

```bash
# Crie o ambiente
python -m venv .venv

# Ative o ambiente
# No Linux/macOS:
source .venv/bin/activate
# No Windows:
.venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 4. Execute o Script

```bash
python src/air_quality_analysis.py
```

---

## 📈 Resultados Gerados

A execução do script gera as seguintes visualizações para análise:

* Mapa de Correlação (heatmap)
* Histogramas das variáveis
* Boxplot para análise de outliers
* Gráfico Real vs. Previsto
* Gráfico de Resíduos

Todos os gráficos e a análise completa estão incluídos no relatório em PDF.

---

## 📝 Relatório

O relatório detalhado com a análise estatística, descrição dos resultados, gráficos e conclusão está disponível no arquivo:

`reports/Julia_Levandoski_T20233.pdf`

---

### 👨‍🏫 Autor

* **Nome:** Júlia Fernanda Levandoski
* **Turma:** 2023
* **Disciplina:** Tópicos Especiais em Computação I
* **Professor:** Jackson Felipe Magnabosco

## 📚 Referências

- UCI Machine Learning Repository – Air Quality Data Set:  
  https://archive.ics.uci.edu/ml/datasets/Air+Quality

- PEDREGOSA, F. et al. **Scikit-learn: Machine Learning in Python.** Journal of Machine Learning Research, v. 12, p. 2825–2830, 2011.

- WASKOM, M. et al. **Seaborn: Statistical Data Visualization.** Journal of Open Source Software, 2021.  
  https://doi.org/10.21105/joss.03021

- HUNTER, J. D. **Matplotlib: A 2D Graphics Environment.** Computing in Science & Engineering, 2007.

- MCKINNEY, W. **Data Structures for Statistical Computing in Python.** In: Proceedings of the 9th Python in Science Conference, 2010.

---

## 📥 Licença

Este projeto é acadêmico e foi desenvolvido exclusivamente para fins educacionais.  
Você pode reutilizar e adaptar este conteúdo.

---
