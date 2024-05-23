from timeit import timeit


# Набір монет
coins = [50, 25, 10, 5, 2, 1]

def find_min_coins(amount):
    # Ініціалізація масиву для збереження мінімальної кількості монет для кожної суми від 0 до amount
    min_coins = [float('inf')] * (amount + 1)
    # Ініціалізація масиву для збереження останньої використаної монети для кожної суми
    coin_used = [0] * (amount + 1)
    # Немає потреби в монетах для суми 0
    min_coins[0] = 0

    # Основний цикл для обчислення мінімальної кількості монет для кожної суми
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                if min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                    min_coins[current_amount] = min_coins[current_amount - coin] + 1
                    coin_used[current_amount] = coin

    # Зворотний хід для відновлення комбінації монет
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return print(f"Словник з монетами методом динамічного програмування: {result}")


# Приклад суми для видачі решти
amount = 113

# Виклик функції
result = timeit(str(find_min_coins(amount)), number = 1000)
print(f'Час виконання: {result:.10f} секунд')
