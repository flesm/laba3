import json

def companies():
    firm_profit = {}
    total_profit = 0
    count_profit = 0

    with open("companies.txt", "r", encoding="UTF-8") as file_comp:
        for line in file_comp:
            name, type, income, expense = line.split()
            profit = int(income) - int(expense)
            firm_profit[name] = profit
            if profit > 0:
                total_profit += profit
                count_profit += 1

    if count_profit > 0:
        average_profit = total_profit / count_profit
    else:
        average_profit = 0

    result = [firm_profit, {"average_profit": average_profit}]

    with open('result.json', 'w', encoding="UTF-8") as file_json:
        json.dump(result, file_json)

    print(result)