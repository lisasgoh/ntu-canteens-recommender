'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''
# This module contains all the functions which defines the response when a user clicks a button at a particular page

import pygame
import sys
import json
from .search_mod import search_by_price, search_by_food
from .list_mod import *
from .display_mod import *
from .sort_and_merge import merge_sort
from .distances_mod import get_canteen_distance_list
from .maps_mod import get_user_location

save_file = open("trialdic.json", "r")		
canteens = json.loads(save_file.read())

DISPLAYSURF = pygame.display.set_mode((400,300))
BLACK = (0,0,0)
WHITE = (255,255,255)

interestedCanteens = []
interestedStalls = []

# Mouseclick for pages
def click(page, updateButton, clickedButton):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            page, updateButton, clickedButton = getButtonClicked(mousex, mousey, page, updateButton, clickedButton)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    
    return page, updateButton, clickedButton


# Main menu buttons 
def select_purpose(mousex, mousey):
    if mousex >= 100 and mousex <= 300:
        if mousey >= 20 and mousey <= 60:
            return "sort"
        elif mousey >= 80 and mousey <= 120:
            return "search price"
        elif mousey >= 140 and mousey <= 180:
            return "search food"
        elif mousey >= 200 and mousey <= 240:
            return "update info"


# Update info options
def select_update_option(mousex, mousey):
    if mousex >= 100 and mousex <= 300:
        if mousey >= 20 and mousey <= 60:
            return "change price"
        elif mousey >= 80 and mousey <= 120:
            return "change rating"
        elif mousey >= 140 and mousey <= 180:
            return "add food"
        elif mousey >= 200 and mousey <= 240:
            return "remove food"


# When food or stall is selected, it is added to the list for future processing
def mouseclick_stalls(mousex, mousey, usage = None):
    if mousex >= 10 and mousex <= 135 and mousey >= 200 and mousey <= 240:
        interestedStalls.append("western")
    elif mousex >= 10 and mousex <= 135 and mousey >= 250 and mousey <= 290:
        interestedStalls.append("japanese")
    elif mousex >= 140 and mousex <= 265 and mousey >= 200 and mousey <= 240:
        interestedStalls.append("korean")
    elif mousex >= 140 and mousex <= 265 and mousey >= 250 and mousey <= 290:
        interestedStalls.append("malay")
    elif mousex >= 270 and mousex <= 395 and mousey >= 200 and mousey <= 240:
        interestedStalls.append("chicken rice")
    elif mousex >= 270 and mousex <= 395 and mousey >= 250 and mousey <= 290:
        interestedStalls.append("indian")
    elif mousex >= 10 and mousex <= 135 and mousey >= 150 and mousey <= 190:
        interestedStalls.append("yong tau foo")
    elif mousex >= 270 and mousex <= 395 and mousey >= 150 and mousey <= 190:
        interestedStalls.append("ban mian")
    elif mousex >= 140 and mousex <= 265 and mousey >= 150 and mousey <= 190:
        interestedStalls.append("vegetarian")
    elif mousex >= 10 and mousex <= 135 and mousey >= 100 and mousey <= 140:
        interestedStalls.append("economical rice") 
    elif mousex >= 150 and mousex <= 275 and mousey >= 60 and mousey <= 120:
        if usage == "sort food":    # If user selected sort at the main menu
            del interestedStalls[:]
            interestedStalls.append("")
        else:   # else clicking at that area would not lead to anything. This is to differentiate between user who chose to sort food or update information at user menu
            pass


# When a canteen is selected, it is added to the list for future processing
def mouseclick_canteens(mousex, mousey, usage = None):
    if mousex >= 10 and mousex <= 135 and mousey >= 50 and mousey <= 90:
        interestedCanteens.append("Canteen 1")
    elif mousex >= 140 and mousex <= 265 and mousey >= 50 and mousey <= 90:
        interestedCanteens.append("canteen 2")
    elif mousex >= 270 and mousex <= 395 and mousey >= 50 and mousey <= 90:
        interestedCanteens.append("canteen 9")
    elif mousex >= 10 and mousex <= 135 and mousey >= 100 and mousey <= 140:
        interestedCanteens.append("canteen 11")
    elif mousex >= 140 and mousex <= 265 and mousey >= 100 and mousey <= 140:
        interestedCanteens.append("canteen 13")
    elif mousex >= 270 and mousex <= 395 and mousey >= 100 and mousey <= 140:
        interestedCanteens.append("canteen 14")
    elif mousex >= 10 and mousex <= 135 and mousey >= 150 and mousey <= 190:
        interestedCanteens.append("canteen 16")
    elif mousex >= 140 and mousex <= 265 and mousey >= 150 and mousey <= 190:
        interestedCanteens.append("tamarind canteen")
    elif mousex >= 270 and mousex <= 395 and mousey >= 150 and mousey <= 190:
        interestedCanteens.append("north hill canteen")
    elif mousex >= 10 and mousex <= 135 and mousey >= 200 and mousey <= 240:
        interestedCanteens.append("pioneer canteen")
    elif mousex >= 140 and mousex <= 265 and mousey >= 200 and mousey <= 240:
        interestedCanteens.append("koufu canteen")
    elif mousex >= 270 and mousex <= 395 and mousey >= 200 and mousey <= 240:
        interestedCanteens.append("north spine canteen")
    elif mousex >= 140 and mousex <= 265 and mousey >= 250 and mousey <= 290:
        if usage == "sort food": # If user selected sort at the main menu, then clicking at that button would be indicating lack of preference
            del interestedCanteens[:]
            interestedCanteens.append("")
        else:   # else clicking at that area would not lead to anything. This is to differentiate between user who chose to sort food or update information at user menu
            pass


# Returns the user selected sort method
def mouseclick_sorting(mousex, mousey):
    if mousex >= 100 and mousex <= 300:
        if mousey >= 100 and mousey <= 150:
            return "price"
        elif mousey >= 160 and mousey <= 210:
            return "distance"
        elif mousey >= 220 and mousey <= 270:
            return "review"

# Returns the selected mode of tranportation to the canteens (walking, driving or transit)
def choose_travel(mousex, mousey):
    if mousex >= 100 and mousex <= 300:
        if mousey >= 80 and mousey <= 120:
            return "walking"
        elif mousey >= 140 and mousey <= 180:
            return "driving"
        elif mousey >= 200 and mousey <= 240:
            return "transit"
        
# This code allows user to ADD or REMOVE food informaion stored in the database
# The following update information code is here as it referenced variables from the main program
def update_info_for_changing_food(page, updateButton):
    # If user selects to ADD information
    if updateButton == "add food":
        while True:
            print("Enter food to be added.")
            food_to_be_added = text_box_display() 
            food_to_be_added = food_to_be_added.lower()
            if food_to_be_added not in canteens[interestedCanteens[0]]: #ensures that food to be added does not already exist in the chosen canteen
                break
        while True:
            print("Enter new price.")
            new_price = text_box_display("price")
            print("Enter new rating.")
            new_ratings = text_box_display("price")
            if 0 <= new_ratings <= 5 and new_price > 0: #check validity of both price and ratings
                new_dict = {food_to_be_added : {"price" : new_price, "ratings" : new_ratings}}
                canteens[interestedCanteens[0]].update(new_dict) #update key, value
                break
            
    # If user selects to REMOVE information
    elif updateButton == "remove food":
        while True:
            print("Enter food to be removed.")
            food_to_be_removed = text_box_display()
            food_to_be_removed = food_to_be_removed.lower()
            if food_to_be_removed in canteens[interestedCanteens[0]]: #ensure that the food to be removed exists in the chosen canteen
                del canteens[interestedCanteens[0]][food_to_be_removed]
                break
    
    # Save user changes        
    save_file = open("trialdic.json", "w") #save the updated info into the json file
    save_file.write(json.dumps(canteens))
    update_info_display() #goes back to first page
    del interestedCanteens[:] #resets the data
    page -= 1        
    return page

# This code allows user to MODIFY food informaion, PRICE or RATING, stored in the database
# The following update information code is here as it referenced variables from the main program
def update_info_change_price_ratings(page, updateButton):
    condition = False
    if len(interestedStalls) > 0: #if valid stall chosen
        if interestedStalls[0] in canteens[interestedCanteens[0]]:
            while True:
                text = text_box_display("price")
                print(text)
                if updateButton == "change price" and text > 0:
                    canteens[interestedCanteens[0]][interestedStalls[0]]["price"] = text
                    condition = True
                    break
                elif updateButton == "change rating" and 0 <= text <= 5:
                    canteens[interestedCanteens[0]][interestedStalls[0]]["ratings"] = text
                    condition = True
                    break
        else:
            print("Food not in canteen.")
            del interestedStalls[:]
    if condition: #if successfullly changed price or ratings
        save_file = open("trialdic.json", "w")
        save_file.write(json.dumps(canteens))
        del interestedCanteens[:]
        del interestedStalls[:] #needs to be under this in the event that the food is not in the canteen
        update_info_display()
        page -= 2
    return page


# Control for which of the above selection functions to run as they are dependent on the page the user is viewing
# THE FOLLOWING CODE IS ESSENTIALLY THE SPINE OF THE WHOLE PROGRAM
def getButtonClicked(mousex, mousey, page, updateButton, clickedButton):
    # Welcome page
    if page == -1: #main memu is displayed
        main_menu()
        page += 1
    # At main menu
    elif page == 0: #This is called when user clicks on the main menu page
        if clickedButton == None: #ensure that no button has been clicked upon new display 
            clickedButton = select_purpose(mousex, mousey) #obtains the choice of user regarding what to execute
        if clickedButton == "sort": #if user wants to sort food
            select_food_page("sort food")
            page += 1
        elif clickedButton == "search price": #if user wants to search by price
            text = text_box_display(usage = "price") #this is so that the try-except clause will be executed and non-float will not be returned
            sets_within_budget = search_by_price(text, canteens) #im just wondering why this canteens is automatically the most updated one
            #informs user of all the stalls which is within the budget and the canteen it is in
            if sets_within_budget: #if there are sets within budget
                display_budget_list(sets_within_budget)
                page = 4 #this is to allow user to go back to main menu
            else:
                print("No food within budget.")
        elif clickedButton == "search food":
            text = text_box_display() #displaus a text box to ask user what food to search for
            canteens_with_food = search_by_food(text, canteens)
            if canteens_with_food: #if there are canteens with the necessary food
                display_food_list(canteens_with_food)
                page = 4 #this is to allow user to go back to main menu
            else:
                print("No canteens with food.")
        elif clickedButton == "update info":
            update_info_display()
            page = 7
            
    # At food selection page
    elif page == 1:
        if mousex >= 270 and mousex <= 395 and mousey >= 10 and mousey <= 50 and len(interestedStalls) > 0: #if next button is clicked and valid option selected
            page += 1
            if "" in interestedStalls: #if no preference was selected remove the " "
                interestedStalls.remove("")
            select_canteens_page("sort food")
        elif mousex >= 10 and mousex <= 135 and mousey >= 10 and mousey <= 50: #if back button was clicked, go back to main menu page
            del interestedStalls[:] 
            page -= 1
            clickedButton = None
            main_menu()
        else:
            mouseclick_stalls(mousex, mousey, "sort food")
            print(interestedStalls)
    
    # At canteens selection page
    elif page == 2:
        if mousex >= 270 and mousex <= 395 and mousey >= 10 and mousey <= 50 and len(interestedCanteens) > 0: #if next button is clicked and an option is selected
            page += 1
            if "" in interestedCanteens:
                interestedCanteens.remove("")
            select_sort_page()
        elif mousex >= 10 and mousex <= 135 and mousey >= 10 and mousey <= 50: #if back button is clicked, go back to food display page and clear current information
            del interestedCanteens[:]
            del interestedStalls[:]
            page -= 1 
            select_food_page("sort food")
        else:
            mouseclick_canteens(mousex, mousey, "sort food")
            print(interestedCanteens)
    
    # At sorting method selection page
    elif page == 3:
        if mousex >= 10 and mousex <= 135 and mousey >= 10 and mousey <= 50:
            del interestedCanteens[:]
            page -= 1
            select_canteens_page("sort food")
        else:
            thirdPageButton = mouseclick_sorting(mousex, mousey) #returns user choice of how to filter
            if thirdPageButton != None: #if valid option selected
                generateFoodInfoList(interestedStalls, interestedCanteens) #this would return canteenList, priceList, stallList, reviewList that tries to find similarities between the interestedCanteens and interestedStalls
                print(priceList)
                if canteenList: #if there is a valid result after taking account user's preference
                    if thirdPageButton == "distance":
                        display_distance_options()
                        page = 11
                    else:
                        filterFood(thirdPageButton)
                        page += 1
                else:
                    print("No relevant results")
    
    elif page == 11:
        travel_choice = choose_travel(mousex, mousey)
        if travel_choice != None: #travel choice = walking, driving, or transit
             user_clicked_location = get_user_location() # user_location (latitude, longitude)
             distanceList = merge_sort(get_canteen_distance_list(user_clicked_location, canteenList, travel_choice))
             x = 10
             y = 60 
             display_distance_screen()
             for i in range(len(distanceList)):
                 text = distanceList[i]
                 font = pygame.font.Font('freesansbold.ttf', 11)
                 text = font.render(text, True, WHITE)
                 DISPLAYSURF.blit(text, (x,y))
                 y += 15
             del distanceList[:]
             page = 4

    elif page == 4: #this is the result display page and this also allows user to go back to the main menu
        if 10 <= mousex <= 135 and 10 <= mousey <= 50: #if back button was clicked
            pygame.display.set_mode((400, 300)) #reset back to original size
            pygame.display.flip()   
            page = 0
            main_menu()
            clickedButton = None #clears all these data so can obtain new choice of user
            del interestedCanteens[:] 
            del interestedStalls [:]
            del canteenList[:]
            del priceList[:]
            del reviewList[:]
            del stallList[:]
    
    elif page == 7: #This is called when the user clicks on the update option
        if 10 <= mousex <= 135 and 250 <= mousey <= 290: #if back button is selected
            page = 0 #go back to the main menu page
            main_menu()
            clickedButton = None #clear clickedButton to obtain the new choice of user
        else:
            updateButton = select_update_option(mousex, mousey) #obtain the choice of update of user
            if updateButton != None: #if user selected a valid choice of update
                select_canteens_page() #display canteen page
                page += 1
        
    # This is called when the user clicks on the canteen display
    elif page == 8: 
        if mousex >= 10 and mousex <= 135 and mousey >= 10 and mousey <= 50: #if back button clicked
            page -= 1
            update_info_display() #go back to the update_info page
        else:
            mouseclick_canteens(mousex, mousey) #get the proper button clicked
            if len(interestedCanteens) > 0:
                if updateButton == "add food" or updateButton == "remove food":
                    page = update_info_for_changing_food(page, updateButton)
                elif updateButton == "change price" or updateButton == "change rating":
                    select_food_page()
                    page += 1
        
    elif page == 9: #This is called when the user clicks on the select food page for updating information
        if mousex >= 10 and mousex <= 135 and mousey >= 10 and mousey <= 50: #if back button clicked
            select_canteens_page() #goes back to the canteen page
            page -= 1
            del interestedCanteens[:] #ensures that the existing canteen chosen list is cleared so able to obtain new data
        else:
            mouseclick_stalls(mousex, mousey) #obtain stall that user selected
            page = update_info_change_price_ratings(page, updateButton)
    
    return page, updateButton, clickedButton