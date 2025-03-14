# Importowanie bibliotek
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ustawienie stylu dla wykresów
sns.set(style="whitegrid")

# Tworzenie przykładowych danych
data = {
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Łódź'],
    'Dzień_1': [12, 14, 16, 13, 15, 14],
    'Dzień_2': [14, 16, 18, 15, 17, 16],
    'Dzień_3': [15, 17, 19, 16, 18, 17],
    'Dzień_4': [16, 18, 20, 17, 19, 18],
    'Dzień_5': [18, 20, 22, 19, 21, 20],
}

# Tworzenie DataFrame z danych
df = pd.DataFrame(data)

# Ustawienie 'Miasto' jako indeks
df.set_index('Miasto', inplace=True)

# Obliczanie średniej temperatury w każdym mieście
df['Średnia'] = df.mean(axis=1)

# Wizualizacja danych za pomocą matplotlib i seaborn

# Wykres liniowy dla temperatur w poszczególnych dniach
plt.figure(figsize=(10, 6))
for miasto in df.index:
    plt.plot(df.columns[:-1], df.loc[miasto, :-1], label=miasto)

plt.title('Temperatury w różnych miastach w ciągu 5 dni', fontsize=16)
plt.xlabel('Dzień', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.legend(title='Miasto', loc='upper left')
plt.grid(True)
plt.show()

# Wykres słupkowy średnich temperatur dla każdego miasta
plt.figure(figsize=(10, 6))
sns.barplot(x=df.index, y=df['Średnia'], palette='viridis')
plt.title('Średnia temperatura w różnych miastach', fontsize=16)
plt.xlabel('Miasto', fontsize=12)
plt.ylabel('Średnia temperatura (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Heatmapa temperatur dla wszystkich dni
plt.figure(figsize=(10, 6))
sns.heatmap(df.iloc[:, :-1], annot=True, cmap="coolwarm", cbar_kws={'label': 'Temperatura (°C)'}, linewidths=0.5)
plt.title('Heatmapa temperatur w różnych miastach', fontsize=16)
plt.xlabel('Dzień', fontsize=12)
plt.ylabel('Miasto', fontsize=12)
plt.show()
