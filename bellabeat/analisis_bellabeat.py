# -*- coding: utf-8 -*-
"""
Análisis de Comportamiento de Usuarios — Caso de Estudio BellaBeat
Fuente de datos: tabla_maestra_bellabeat_v2 (BigQuery)
Herramientas: Python, Pandas, Seaborn, Matplotlib
"""

from google.colab import auth
auth.authenticate_user()
print('Autenticado con éxito')

# Carga de datos consolidados desde BigQuery
# %%bigquery df --project mi-proyecto-analisis-499721
# select * from `bellabeat_casestudy.tabla_maestra_bellabeat_v2`

# --- Exploración inicial ---
df.info()

resumen = df.describe()
resumen.to_excel('resumen_bellabeat.xlsx')
resumen

# --- Gráfico 1: Pasos Totales vs. Minutos Dormidos ---
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PasosTotales', y='MinutosDormidos', color='blue', alpha=0.6)
sns.regplot(data=df, x='PasosTotales', y='MinutosDormidos',
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})

plt.title('¿Afecta la cantidad de pasos al sueño nocturno?')
plt.xlabel('Pasos Totales al Día')
plt.ylabel('Minutos Dormidos')
plt.show()

# --- Gráfico 2: Sedentarismo vs. Sueño ---
df['HorasSedentarias'] = df['MinutosSedentarios'] / 60

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='HorasSedentarias', y='MinutosDormidos',
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})

plt.title('Relación entre Inactividad Diaria y Horas de Sueño', fontsize=14, fontweight='bold')
plt.xlabel('Horas Sedentarias al Día', fontsize=12)
plt.ylabel('Minutos Dormidos por la Noche', fontsize=12)
plt.show()

# --- Coeficientes de correlación (Pearson) ---
correlacion_pasos_sueno = df['PasosTotales'].corr(df['MinutosDormidos'])
correlacion_sedentarismo_sueno = df['HorasSedentarias'].corr(df['MinutosDormidos'])

print(f'Correlación Pasos-Sueño: {correlacion_pasos_sueno:.2f}')
print(f'Correlación Sedentarismo-Sueño: {correlacion_sedentarismo_sueno:.2f}')

# Resultados obtenidos:
# Correlación Pasos-Sueño:         -0.19  (débil / no significativa)
# Correlación Sedentarismo-Sueño:  -0.60  (negativa, fuerte)
