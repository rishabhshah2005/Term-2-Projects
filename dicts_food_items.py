food = {"pizza":100, "burger":40, 'noodles':80, 'panipuri':10, 'butter chicken':500}

print(food.keys())
print(food.values())
print(food.items())
print(food.get('pizza'))
food.update({'chips': 5})
print(food)
del food['chips']
print(food)
food.clear()
print(food)


# OUTPUT 
# dict_keys(['pizza', 'burger', 'noodles', 'panipuri', 'butter chicken'])
# dict_values([100, 40, 80, 10, 500])
# dict_items([('pizza', 100), ('burger', 40), ('noodles', 80), ('panipuri', 10), ('butter chicken', 500)])
# 100
# {'pizza': 100, 'burger': 40, 'noodles': 80, 'panipuri': 10, 'butter chicken': 500, 'chips': 5}
# {'pizza': 100, 'burger': 40, 'noodles': 80, 'panipuri': 10, 'butter chicken': 500}
# {}

# Code by Rishabh Shah