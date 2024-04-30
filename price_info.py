
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping(price_list, quantity_list):
    total_cost = 0
    length1=len(price_list)
    length2=len(quantity_list)

    if length1==0 or length2==0:
        return False
    elif length1==length2!=0:
        for key in price_list.keys():
            if key in quantity_list:
                # complete the implementation below:
                total_cost=total_cost+quantity_list.get(key)*price_list.get(key)
    elif length1!=length2:
        return False
    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    if quantity<0:
        return False
        
    elif quantity==0:
        return 0
    
    else:
        for key in price_list.keys():
            if key == fruit:
                cost = quantity*price_list[key]
                break
    print("cost of ", quantity, fruit, "=", cost)
    return cost



def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping(price_list,quantity_list)


if __name__ == "__main__":
    main()