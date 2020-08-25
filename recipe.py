import json


def check_materials(data_file, materials):  # Check the martial in the food storage
    with open(data_file, 'r') as File:
        data = json.load(File)
        File.close()
    if data.get(materials, -1) == -1:
        return False
    return True


def check_price(data_file, price, materials):  # Compare the price between the food and its' materials
    with open(data_file, 'r') as File:
        data = json.load(File)
        File.close()
    sum_price = 0
    for i in materials.keys():
        sum_price += data[i]['price'] * materials[i]
    if price >= sum_price:
        return True
    return False


def input_recipe():
    # Input to for the food
    # Input the name of the food
    recipe_file = "data/recipe.json"
    food_storage_file = "data/foodStorage.json"
    print('Input the recipe: ')
    name = input('Name: ')

    # Input the materials of the food
    materials = {}
    while True:
        try:
            a = input('Name of the materials(Finish press enter): ')
            if a == '':
                break
            if not check_materials(food_storage_file, a):
                raise Exception('materialsNotMatch')
            b = int(input('Number: '))
        except:
            print(
                '*****The materials is not found in the food storage*****')  # If the materials is not found, stop input
            return
        materials[a] = b

    # Input the food's price
    try:
        price = int(input('Enter the price: '))
        if not check_price(food_storage_file, price, materials):
            raise Exception('PriceInvalid')
    except:
        print('******The price is invalid (smaller than the materials\'s price)*****')
        return

    # Update to the recipe file
    with open(recipe_file, 'r') as File:
        try:
            data = json.load(File)
            File.close()
        except json.decoder.JSONDecodeError:  # Check if the recipe file is None
            with open(recipe_file, 'w') as File:
                json.dump({}, File)
                data = {}
                File.close()

    data[name] = [price, materials]  # Add {name: materials} to data
    with open(recipe_file, 'w') as File:  # Update data to the file
        json.dump(data, File, indent=4)
        File.close()
        print('*****Update the recipe complete!*****')
