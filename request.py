import json
import foodStorage

try:
    with open("data/foodStorage.json") as fs:
        food_storage = json.load(fs)
finally:
    fs.close()

try:
    with open("data/recipe.json") as r:
        recipe = json.load(r)
finally:
    r.close()


# Nhap yeu cau khach hang tu ban phim
def input_request():
    requests = {}
    try:
        s = input("orders (ex: 1 banhmypate, 2 mytomtrung): ").split(",")
        for i in s:
            number, food = i.split()
            if food not in recipe:
                print(food + " is not in menu.")
                return input_request()
            requests[food] = int(number)
    except:
        print("Invalid order...")
        return False
    return requests


# Calculate the profit of each item on the list
def sort_profit():
    real_price = {key: recipe[key][0] for key in recipe}
    dict_profit = {}
    for i in real_price.keys():
        profit = real_price[i] - sum([recipe[i][1][j] * food_storage[j]["price"]
                                      for j in recipe[i][1].keys()])
        dict_profit[i] = profit
    lst_profit = [profit for profit in dict_profit.values()]
    lst_profit.sort(reverse=True)
    sort = {key: value for value in lst_profit for key in dict_profit.keys()
            if dict_profit[key] == value}
    return sort  # {food_name: profit } Sort by descending profits


# arrange requests in descending order of profit
def sort_request_by_profit(request):
    sort = sort_profit()
    new_request = {r_key: request[r_key] for s_key in sort.keys() for r_key in request.keys()
                   if r_key == s_key}
    return new_request


# xxx
def suggest(f_s, count):
    sort = sort_profit()
    instead = {}
    for food in sort:
        number = 0
        while foodStorage.check(f_s, {food: 1})[0]:
            number += 1
            count -= 1
            if count == 0:
                break
            continue
        if number != 0:
            instead[food] = number
        if count == 0:
            break
    return instead
