from prettytable import PrettyTable

def resource_allocation(costs, profits, total_resources):
    num_enterprises = len(costs)
    dp = [[0 for _ in range(total_resources + 1)] for _ in range(num_enterprises + 1)]

    for i in range(1, num_enterprises + 1):
        for r in range(1, total_resources + 1):
            if costs[i - 1] <= r:
                dp[i][r] = max(profits[i - 1] + dp[i - 1][r - costs[i - 1]], dp[i - 1][r])
            else:
                dp[i][r] = dp[i - 1][r]

    # Восстановление решения
    selected_enterprises = []
    i, r = num_enterprises, total_resources
    while i > 0 and r > 0:
        if dp[i][r] != dp[i - 1][r]:
            selected_enterprises.append(i - 1)
            r -= costs[i - 1]
        i -= 1

    return dp[num_enterprises][total_resources], selected_enterprises[::-1]

# Пример использования
costs = [10,1,1,1]
profits = [5, 7, 8, 10]
total_resources = 2

x = PrettyTable()
fields = ["Предприятие", "Объем вложений", "Прибыль"]
x.field_names = fields
for i in range(len(costs)):
    x.add_row(
        [i+1, costs[i], profits[i]]
    )

print(x)

max_profit, selected_enterprises = resource_allocation(costs, profits, total_resources)
selected_enterprises = list(map(lambda x: x+1 , selected_enterprises))
print(f"Всего ресурсов: {total_resources}")
print(f"Максимальный доход: {max_profit}")
print(f"Выбранные предприятия: {selected_enterprises}")
