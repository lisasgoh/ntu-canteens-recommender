'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''
# This module contains all the searching functions

# Searches based on user input budget
def search_by_price(budget, canteens):
    set_within_budget = []
    for canteen in canteens:
        for stall in canteens[canteen]:
            if canteens[canteen][stall]["price"] <= budget:  
                stall_within_budget = [] #if price of the food is within budget, add the food into list1
                stall_within_budget.append(stall)
                stall_within_budget.append(canteen)
                stall_within_budget.append(str(canteens[canteen][stall]["price"]))
                set_within_budget.append(stall_within_budget)
    return set_within_budget     


# Searches based on user selected food preference
def search_by_food(text, canteens):
    canteens_with_food = []
    for canteen in canteens:
        for stall in canteens[canteen]: 
            if stall == text.lower():
                canteens_with_food.append(canteen)
                break
    return canteens_with_food