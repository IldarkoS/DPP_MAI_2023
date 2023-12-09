from prettytable import PrettyTable


def optimize_resources(profits, costs, total_resources):
    p = len(profits)  # Количество предприятий
    n = len(profits[0])  # Количество лет

    # Создаем матрицу для хранения максимальной прибыли
    dp = [[[0, []] for _ in range(total_resources + 1)] for _ in range(n + 1)]

    # Итерируемся по годам
    for year in range(1, n + 1):
        # Итерируемся по ресурсам
        for resources in range(total_resources + 1):
            # Перебираем все предприятия
            for company in range(p):
                # Проверяем, можно ли использовать текущее предприятие
                if resources >= costs[company][year - 1]:
                    # Выбираем максимальную прибыль из предыдущего года
                    max_profit_last_year = dp[year - 1][resources - costs[company][year - 1]][0]

                    # Обновляем текущую ячейку матрицы
                    current_profit = profits[company][year - 1] + max_profit_last_year

                    if current_profit > dp[year][resources][0]:
                        dp[year][resources] = [current_profit, dp[year - 1][resources - costs[company][year - 1]][1] + [company + 1]]

                # Если не используем текущее предприятие
                if dp[year][resources][0] < dp[year - 1][resources][0]:
                    dp[year][resources] = dp[year - 1][resources]

    # Находим максимальную прибыль в последнем году
    max_profit = dp[n][total_resources][0]

    # Находим выбранные предприятия в каждом году
    chosen_companies_each_year = dp[n][total_resources][1]

    return max_profit, chosen_companies_each_year


# Пример входных данных (прибыль и затраты предприятий за каждый год)
profits = [
    [10, 20, 15],
    [5, 10, 25],
    [15, 5, 20]
]

costs = [
    [2, 5, 3],
    [1, 3, 4],
    [4, 2, 2]
]

x = PrettyTable()
fields = ["Предприятие", "Объем вложений", "Прибыль"]
x.field_names = fields
for i in range(len(costs)):
    x.add_row(
        [i+1, costs[i], profits[i]]
    )
print(x)

total_resources = 15

result_profit, result_chosen_companies = optimize_resources(profits, costs, total_resources)
print(f"Количество лет: {len(costs[0])}")
print(f"Всего ресурсов: {total_resources}")
print(f"Максимальная прибыль: {result_profit}")
print(f"Выбранные предприятия по годам: {result_chosen_companies}")
