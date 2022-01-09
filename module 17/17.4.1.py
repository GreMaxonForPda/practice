import random as rnd

original_prices = [rnd.randint(-50, 50) for _ in range(10)]
new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0


print(f"Изначальный список цен: {original_prices} \nМы потеряли: {sum(original_prices) - sum(new_prices)}")
