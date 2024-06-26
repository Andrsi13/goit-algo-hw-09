# goit-algo-hw-09
## Висновки

### Жадібний алгоритм
Жадібний алгоритм шукає найменшу кількість монет для видачі решти, завжди вибираючи монету з найбільшим номіналом, яка не перевищує залишкову суму. 

#### Результат:
Словник з монетами жадібним алгоритмом: {50: 2, 25: 0, 10: 1, 5: 0, 2: 1, 1: 1}

#### Час виконання:
0.0000055000 секунд

### Динамічне програмування
Алгоритм динамічного програмування знаходить мінімальну кількість монет для видачі решти, перевіряючи всі можливі комбінації монет і зберігаючи мінімальну кількість для кожної суми від 0 до заданої суми.

#### Результат:
Словник з монетами методом динамічного програмування: {50: 2, 10: 1, 2: 1, 1: 1}

#### Час виконання:
0.0000052090 секунд

### Порівняння
1. **Час виконання**:
    - Жадібний алгоритм виконався за 0.0000055000 секунд.
    - Алгоритм динамічного програмування виконався за 0.0000052090 секунд.
    - Жадібний алгоритм виявився трохи швидшим.

2. **Результат**:
    - Обидва алгоритми повернули правильну кількість монет.
    - Жадібний алгоритм видав: {50: 2, 10: 1, 2: 1, 1: 1}
    - Динамічне програмування видав: {50: 2, 10: 1, 2: 1, 1: 1}

### Висновок
Обидва алгоритми успішно знайшли правильну комбінацію монет для видачі решти. Жадібний алгоритм виявився трохи швидшим у виконанні, однак різниця у часі є незначною для цього прикладу. Вибір алгоритму залежить від конкретних вимог до оптимізації швидкодії та пам'яті, а також від складності та розміру вхідних даних.
