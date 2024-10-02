# Вариант 3
from sympy import symbols
import pandas as pd
import matplotlib.pyplot as plt

k, T, C, L = symbols('k T C L')

# ВХОДНЫЕ ДАННЫЕ
C_ost = 30000  # Первоначальная стоимость
Am_lst = []
C_ost_lst = []
k = 2  # Коэффициент ускорения
T = 7  # Срок полезного использования

# КОНТЕЙНЕР РАСЧЕТА
for i in range(T):
  Am = k / T * C_ost  # Уменьшаемый остаток с коэффициентом ускорения
  C_ost -= Am  # Уменьшаем остаточную стоимость
  Am_lst.append(round(Am, 2))  # Сохраняем амортизационные отчисления
  C_ost_lst.append(round(C_ost, 2))  # Сохраняем остаточную стоимость

print(f'Am_lst={Am_lst}\nC_ost_lst={C_ost_lst}')

# КОНТЕЙГЕР ТАБЛИЧНОГО ПРЕДСТАВЛЕНИЯ
print('Ниже представлен КОНТЕЙГЕР ТАБЛИЧНОГО ПРЕДСТАВЛЕНИЯ')
data = {
    'Амортизационные отчисления (Am_lst)': Am_lst,
    'Остаточная стоимость (C_ost_lst)': C_ost_lst
}

df = pd.DataFrame(data)

# Отображение таблицы
print(df)

# КОНТЕЙНЕР ВИЗУАЛИЗАЦИИ
plt.figure(figsize=(10, 6))

# График амортизационных отчислений
plt.plot(range(1,
               len(Am_lst) + 1),
         Am_lst,
         label='Амортизационные отчисления',
         marker='o')

# График остаточной стоимости
plt.plot(range(1,
               len(C_ost_lst) + 1),
         C_ost_lst,
         label='Остаточная стоимость',
         marker='s')

# Настройка графика
plt.title('Амортизационные отчисления и остаточная стоимость')
plt.xlabel('Периоды')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)

# Показать график
plt.show()