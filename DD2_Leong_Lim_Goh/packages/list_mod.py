'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''
# This module contains all the functions related to lists and updating of information

import json
import pygame
from .display_mod import text_box_display, display_price_list, display_reviews_list
 
DISPLAYSURF = pygame.display.set_mode((400,300))
BLACK = (0, 0, 0)
WHITE = (255,255,255)

#save_file = open("trialdic.json", "r")		
#canteens = json.loads(save_file.read())

priceList = []
reviewList = []
canteenList = []
stallList = []

#interestedCanteens = []
#interestedStalls = []

# Create lists based on what user has chosen
def createLists(canteen, stall, canteens):
    priceList.append(canteens[canteen][stall]["price"])
    reviewList.append(canteens[canteen][stall]["ratings"])
    canteenList.append(canteen) 
    stallList.append(stall)

# Searches for the canteen with the user selected stall
def generateFoodInfoList(interestedStalls, interestedCanteens):
    save_file = open("trialdic.json", "r")		
    canteens = json.loads(save_file.read())
    interestedStalls = set(interestedStalls)
    interestedCanteens = set(interestedCanteens)
    if interestedCanteens and interestedStalls:
        for canteen in interestedCanteens:
            for stall in interestedStalls:
                if stall in canteens[canteen]:
                    createLists(canteen, stall, canteens)
                    
    elif len(interestedCanteens) == 0 and len(interestedStalls)!= 0:
        for stall in interestedStalls:
            for canteen in canteens:
                if stall in canteens[canteen]:
                    createLists(canteen, stall, canteens)
                
    elif len(interestedCanteens) != 0 and len(interestedStalls) == 0:
        for canteen in interestedCanteens:
            for stall in canteens[canteen]:
                createLists(canteen, stall, canteens)
    
    else:
        for canteen in canteens:
            for stall in canteens[canteen]:
                createLists(canteen, stall, canteens)

# Bubble sort for price and/or review sorting
# This sort function is here because it referenced variables from this module
def sort_by_price_or_review(relevantList):
    for passnum in range(len(relevantList)-1):
        swapped = False
        for j in range(len(relevantList)-1-passnum):
            if relevantList[j+1] < relevantList[j]:
                temp = relevantList[j+1]
                relevantList[j+1] = relevantList[j]
                relevantList[j] = temp
                temp1 = canteenList[j+1]
                canteenList[j+1] = canteenList[j]
                canteenList[j] = temp1
                temp2 = stallList[j+1]
                stallList[j+1] = stallList[j]
                stallList[j] = temp2
                swapped = True
        if not swapped:
            break

# Filters according to user's selections
def filterFood(filter_by):
    # Filter by price
    if filter_by == "price":
        print("Type your budget.")
        text = text_box_display("price")
        print(priceList)
        for i in range(len(priceList)-1,-1,-1): #this gets rid of the food with a price greater than budget 
            if priceList[i] > text:
                del priceList[i]
                del stallList[i]
                del canteenList[i]
        if len(priceList) > 0: #if there is a single element that is lower than budget
            sort_by_price_or_review(priceList)
            display_price_list(canteenList, stallList, priceList)
        # If there are no elements in the list, sorting will be skipped
        else:
            print("No relevant results.")
    # Filter by reviews
    elif filter_by == "review":
        sort_by_price_or_review(reviewList)
        display_reviews_list(canteenList, stallList, reviewList)
