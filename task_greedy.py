from timeit import timeit

coins_list = [50, 25, 10, 5, 2, 1]

# генеримо словник з ключами монет
coin_dres_dict = {}
for coin in coins_list:
    coin_dres_dict[coin] = 0


# прописуємо функцію
def find_coins_greedy(sum):
    change = 0
    coin_index = 0
    while sum > 0:
        if sum >= coins_list[coin_index]:
            change += coins_list[coin_index]
            coin_dres_dict[coins_list[coin_index]] += 1
            sum -= coins_list[coin_index]
        else:
            coin_index += 1
    return print(f"Словник з монетами жадібним алгоритмом {coin_dres_dict}")


amount = 113
a = timeit(str(find_coins_greedy(amount)), number = 1000)
print(f'Час виконання: {a:.10f} секунд')
