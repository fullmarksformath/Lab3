import price_info

# test_total_cost_shopping()

def test_total_cost_shopping_empty():
    price_list = {}
    quantity_list = {}
    assert(price_info.total_cost_shopping(price_list, quantity_list)==False)

def test_total_cost_shopping_partially_present():
    price_list = {'apple':2, 'banana':1}
    quantity_list = {'apple':3}
    assert(price_info.total_cost_shopping(price_list, quantity_list)==False)

def test_total_cost_shopping_all_present():
    price_list = {'apple': 2, 'banana': 1}
    quantity_list = {'apple': 3, 'banana': 2}
    assert(price_info.total_cost_shopping(price_list, quantity_list)==8)

def test_total_cost_shopping_zero_quantity():
    price_list = {'apple': 2, 'banana': 1}
    quantity_list = {'apple': 0, 'banana': 2}
    assert(price_info.total_cost_shopping(price_list, quantity_list)==2)

# test_cost_of_fruits()

def test_cost_of_fruits_all_present():
    fruit = 'apple'
    quantity = 65
    assert(price_info.cost_of_fruits(fruit,quantity)==78)

def test_cost_of_fruits_negative():
    fruit ='apple'
    quantity=-5
    assert(price_info.cost_of_fruits(fruit,quantity)==False)

def test_cost_of_fruits_zero_quantity():
    fruit ='apple'
    quantity=0
    assert(price_info.cost_of_fruits(fruit,quantity)==0)
    
