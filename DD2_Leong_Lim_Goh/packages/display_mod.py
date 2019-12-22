'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''
# This module contains all the display pages and user input box

import pygame
import sys

DISPLAYSURF = pygame.display.set_mode((400,300))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)

westernButton = pygame.image.load('western_button.png')
westernButton = pygame.transform.scale(westernButton, (125,40))
koreanButton = pygame.image.load('korean_button.png')
koreanButton = pygame.transform.scale(koreanButton, (125,40))
chickenriceButton = pygame.image.load('chickenrice_button.png')
chickenriceButton = pygame.transform.scale(chickenriceButton, (125,40))
japaneseButton = pygame.image.load('japanese_button.png')
japaneseButton = pygame.transform.scale(japaneseButton, (125,40))
malayButton = pygame.image.load('malay_button.png')
malayButton = pygame.transform.scale(malayButton, (125,40))
indianButton = pygame.image.load('indian_button.png')
indianButton = pygame.transform.scale(indianButton, (125,40))
ytfButton = pygame.image.load('ytf_button.png')
ytfButton = pygame.transform.scale(ytfButton, (125,40))
caifanButton = pygame.image.load('caifan_button.png')
caifanButton = pygame.transform.scale(caifanButton, (125,40))
vegetarianButton = pygame.image.load('vegetarian_button.png')
vegetarianButton = pygame.transform.scale(vegetarianButton, (125,40))
banmianButton = pygame.image.load('banmian_button.png')
banmianButton = pygame.transform.scale(banmianButton, (125,40))
indianButton = pygame.image.load('indian_button.png')
indianButton = pygame.transform.scale(indianButton, (125,40))
can1Button = pygame.image.load('can1.png')
can1Button = pygame.transform.scale(can1Button, (125,40))
can2Button = pygame.image.load('can2.png')
can2Button = pygame.transform.scale(can2Button, (125,40))
can9Button = pygame.image.load('can9.png')
can9Button = pygame.transform.scale(can9Button, (125,40))
can11Button = pygame.image.load('can11.png')
can11Button = pygame.transform.scale(can11Button, (125,40))
can13Button = pygame.image.load('can13.png')
can13Button = pygame.transform.scale(can13Button, (125,40))
can14Button = pygame.image.load('can14.png')
can14Button = pygame.transform.scale(can14Button, (125,40))
can16Button = pygame.image.load('can16.png')
can16Button = pygame.transform.scale(can16Button, (125,40))
tamarindButton = pygame.image.load('tamarind.png')
tamarindButton = pygame.transform.scale(tamarindButton, (125,40))
northHillButton = pygame.image.load('northhill.png')
northHillButton = pygame.transform.scale(northHillButton, (125,40))
pioneerButton = pygame.image.load('pioneer.png')
pioneerButton = pygame.transform.scale(pioneerButton, (125,40))
koufuButton = pygame.image.load('koufu.png')
koufuButton = pygame.transform.scale(koufuButton, (125,40))
northSpineButton = pygame.image.load('northspine.png')
northSpineButton = pygame.transform.scale(northSpineButton, (125,40))
priceButton = pygame.image.load('price.png')
priceButton = pygame.transform.scale(priceButton, (200,50))
distanceButton = pygame.image.load('distance.png')
distanceButton = pygame.transform.scale(distanceButton, (200,50))
reviewButton = pygame.image.load('review.png')
reviewButton = pygame.transform.scale(reviewButton, (200,50))
nextButton = pygame.image.load('next.png')
nextButton = pygame.transform.scale(nextButton, (125,40))
backButton = pygame.image.load('back.png')
backButton = pygame.transform.scale(backButton, (125,40))
noPreferenceButton = pygame.image.load('no preference.png')
noPreferenceButton = pygame.transform.scale(noPreferenceButton, (125,40))
sortButton = pygame.image.load('sort.png')
sortButton = pygame.transform.scale(sortButton, (200,40))
searchFoodButton = pygame.image.load('search food.png')
searchFoodButton = pygame.transform.scale(searchFoodButton, (200,40))
searchbyPriceButton = pygame.image.load('search price.png')
searchbyPriceButton = pygame.transform.scale(searchbyPriceButton, (200,40))
updateInfoButton = pygame.image.load('update info.png')
updateInfoButton = pygame.transform.scale(updateInfoButton, (200,40))
changePriceButton = pygame.image.load('change price.png')
changePriceButton = pygame.transform.scale(changePriceButton, (200,40))
changeRatingButton = pygame.image.load('change rating.png')
changeRatingButton = pygame.transform.scale(changeRatingButton, (200,40))
addFoodButton = pygame.image.load('add food.png')
addFoodButton = pygame.transform.scale(addFoodButton, (200,40))
removeFoodButton = pygame.image.load('remove food.png')
removeFoodButton = pygame.transform.scale(removeFoodButton, (200,40))
walkingButton = pygame.image.load('walking.png')
walkingButton = pygame.transform.scale(walkingButton, (200,40))
drivingButton = pygame.image.load('driving.png')
drivingButton = pygame.transform.scale(drivingButton, (200,40))
busButton = pygame.image.load('bus.png')
busButton = pygame.transform.scale(busButton, (200,40))

#Displays the main menu / search options page
def main_menu():
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(sortButton, (100,20))
    DISPLAYSURF.blit(searchbyPriceButton, (100,80))
    DISPLAYSURF.blit(searchFoodButton, (100,140))
    DISPLAYSURF.blit(updateInfoButton, (100,200))


# Displays page 1 / food preference selection page
def select_food_page(usage = None):
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(caifanButton, (10,100))
    DISPLAYSURF.blit(ytfButton, (10,150))
    DISPLAYSURF.blit(vegetarianButton, (140,150))
    DISPLAYSURF.blit(banmianButton, (270,150))
    DISPLAYSURF.blit(westernButton, (10,200))
    DISPLAYSURF.blit(koreanButton, (140,200))
    DISPLAYSURF.blit(chickenriceButton, (270,200))
    DISPLAYSURF.blit(japaneseButton, (10,250))
    DISPLAYSURF.blit(malayButton, (140,250))
    DISPLAYSURF.blit(indianButton, (270,250))
    DISPLAYSURF.blit(backButton, (10,10))
    if usage == "sort food": #if sorting function was selected, include nextButton and noPreferenceButton
        DISPLAYSURF.blit(nextButton, (270,10))
        DISPLAYSURF.blit(noPreferenceButton, (150,60))


# Displays page 2 / canteen selection page
def select_canteens_page(usage = None):
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(can1Button, (10,50))
    DISPLAYSURF.blit(can2Button, (140,50))
    DISPLAYSURF.blit(can9Button, (270,50))
    DISPLAYSURF.blit(can11Button, (10,100))
    DISPLAYSURF.blit(can13Button, (140,100))
    DISPLAYSURF.blit(can14Button, (270,100))
    DISPLAYSURF.blit(can16Button, (10,150))
    DISPLAYSURF.blit(tamarindButton, (140,150))
    DISPLAYSURF.blit(northHillButton, (270,150))
    DISPLAYSURF.blit(pioneerButton, (10,200))
    DISPLAYSURF.blit(koufuButton, (140,200))
    DISPLAYSURF.blit(northSpineButton, (270,200))
    DISPLAYSURF.blit(backButton, (10,10))
    if usage == "sort food": #if sorting function was selected, include nextButton and noPreferenceButton
        DISPLAYSURF.blit(nextButton, (270,10))
        DISPLAYSURF.blit(noPreferenceButton, (140, 250))


# Displays page 3 / "Sort by" selection page
def select_sort_page():
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(backButton, (10,10))
    DISPLAYSURF.blit(priceButton, (100,100))
    DISPLAYSURF.blit(distanceButton, (100,160))
    DISPLAYSURF.blit(reviewButton, (100,220))

# Functions which determines display screen size of the output, depending on the number of items to display
def screen_size(canteenList, stallList, input_object, element_type):
    x = 10
    y = 57
    text = ''
    font = pygame.font.Font('freesansbold.ttf', 14)
    if len(input_object) <= 15:
        screen = pygame.display.set_mode((400, 300))
        screen.fill(BLACK)
        screen.blit(backButton, (10,10))
        pygame.display.flip()
        if element_type != "budget":
            for i in range(len(input_object)):
                if element_type == "price":
                    text = canteenList[i] + ": " + stallList[i] + "- $" + str(input_object[i])
                elif element_type == "review":
                    text = canteenList[i] + ": " + stallList[i] + "- " + str(input_object[i])
                elif element_type == "food":
                    text = str(input_object[i])
                text = font.render(text, True, WHITE)
                DISPLAYSURF.blit(text, (x,y))
                y += 19
        if element_type == "budget":
            for i in input_object:
                text = font.render((" ").join(i), True, WHITE)
                DISPLAYSURF.blit(text, (x,y))
                y += 19
                
    elif 15 < len(input_object) <= 30:
        screen = pygame.display.set_mode((640, 300))
        screen.fill(BLACK)
        screen.blit(backButton, (10,10))
        pygame.display.flip()
        if element_type != "budget":
            for i in range(len(input_object)):
                if element_type == "price":
                    text = canteenList[i] + ": " + stallList[i] + "- $" + str(input_object[i])
                elif element_type == "review":
                    text = canteenList[i] + ": " + stallList[i] + "- " + str(input_object[i])
                elif element_type == "food":
                    text = str(input_object[i])
                if y > 290:
                    y = 10
                    x = 320
                text = font.render(text, True, WHITE)
                DISPLAYSURF.blit(text, (x,y))
                y += 19
        if element_type == "budget":
            for i in input_object:
                text = font.render((" ").join(i), True, WHITE)
                if y > 290:
                    y = 10
                    x = 320
                DISPLAYSURF.blit(text, (x,y))
                y += 19
    
    elif 30 < len(input_object) <= 45:
        screen = pygame.display.set_mode((640, 450))
        screen.fill(BLACK)
        screen.blit(backButton, (10,10))
        pygame.display.flip()
        if element_type != "budget":
            for i in range(len(input_object)):
                if element_type == "price":
                    text = canteenList[i] + ": " + stallList[i] + "- $" + str(input_object[i])
                elif element_type == "review":
                    text = canteenList[i] + ": " + stallList[i] + "- " + str(input_object[i])
                elif element_type == "food":
                    text = str(input_object[i])
                if y > 440:
                    y = 10
                    x = 320
                text = font.render(text, True, WHITE)
                DISPLAYSURF.blit(text, (x,y))
                y += 19
        if element_type == "budget":
            for i in input_object:
                text = font.render((" ").join(i), True, WHITE)
                if y > 440:
                    y = 10
                    x = 320
                DISPLAYSURF.blit(text, (x,y))
                y += 19

    elif 45 < len(input_object) <= 64:
        screen = pygame.display.set_mode((640, 625))
        screen.fill(BLACK)
        screen.blit(backButton, (10,10))
        pygame.display.flip()
        if element_type != "budget":
            for i in range(len(input_object)):
                if element_type == "price":
                    text = canteenList[i] + ": " + stallList[i] + "- $" + str(input_object[i])
                elif element_type == "review":
                    text = canteenList[i] + ": " + stallList[i] + "- " + str(input_object[i])
                elif element_type == "food":
                    text = input_object[i]
                if y > 615:
                    y = 10
                    x = 320
                text = font.render(text, True, WHITE)
                DISPLAYSURF.blit(text, (x,y))
                y += 19
        if element_type == "budget":
            for i in input_object:
                text = font.render((" ").join(i), True, WHITE)
                if y > 615:
                    y = 10
                    x = 320
                DISPLAYSURF.blit(text, (x,y))
                y += 19
    
    elif 64 < len(input_object):
        screen = pygame.display.set_mode((960, 625))
        screen.fill(BLACK)
        screen.blit(backButton, (10,10))
        pygame.display.flip()
        if element_type != "budget":
            for i in range(len(input_object)):
                if element_type == "price":
                    text = canteenList[i] + ": " + stallList[i] + "- $" + str(input_object[i])
                elif element_type == "review":
                    text = canteenList[i] + ": " + stallList[i] + "- " + str(input_object[i])
                elif element_type == "food":
                    text = str(input_object[i])
                if x == 10 and y > 615:
                    y = 10
                    x = 320
                elif x == 320 and y > 615:
                    y = 10
                    x = 640
                text = font.render(text, True, WHITE)
                DISPLAYSURF.blit(text, (x,y))
                y += 19
        if element_type == "budget":
            for i in input_object:
                text = font.render((" ").join(i), True, WHITE)
                if x == 10 and y > 615:
                    y = 10
                    x = 320
                elif x == 320 and y > 615:
                    y = 10
                    x = 640
                DISPLAYSURF.blit(text, (x,y))
                y += 19

# Displays Price List result, if user selects to sort by price
def display_price_list(canteenList, stallList, priceList):
    screen_size(canteenList, stallList, priceList, element_type = "price")

# Displays Reviews list result, if user selects to sort by reviews
def display_reviews_list(canteenList, stallList, reviewList):
    screen_size(canteenList, stallList, reviewList, element_type = "review")

# Displays list of food of price within user entered budget
def display_budget_list(sets_within_budget):
    screen_size(None, None, sets_within_budget, element_type = "budget")

# Displays the list of food if user selects to search by food
def display_food_list(canteens_with_food):
    screen_size(None, None, canteens_with_food, element_type = "food")


# Resizes the screen for displaying the result for sorted distances
def display_distance_screen():
    screen = pygame.display.set_mode((400, 300))
    screen.fill((0,0,0))
    screen.blit(backButton, (10,10))
    pygame.display.flip()

def display_distance_options():
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(walkingButton, (100,80))
    DISPLAYSURF.blit(drivingButton, (100,140))
    DISPLAYSURF.blit(busButton, (100,200))

# Text box for user to enter input
def text_box_display(usage = None):
    pygame.init()
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = RED
    color_active = GREEN
    color = color_inactive
    active = False
    text = ''
    done = False
    no_of_tries = 0
    max_tries = 3
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicked on the input_box rect. here got problem when u exit programme
                if input_box.collidepoint(event.pos): # Toggle the active variable.
                    active = not active
                else:
                    active = False # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if usage == "price":
                            try:
                                text = float(text)
                                print(text)
                                return text
                            except:
                                no_of_tries += 1
                                print("Invalid input, please input value. Attempt ", no_of_tries, " of 3")
                                if no_of_tries == max_tries:
                                    done = True
                                    pygame.quit()
                                    sys.exit()
                                else:
                                    continue
                        else:
                            return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        DISPLAYSURF.fill(BLACK) # Render the current text.
        txt_surface = font.render(text, True, color) # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width # Blit the text.
        DISPLAYSURF.blit(txt_surface, (input_box.x+5, input_box.y+5)) # Blit the input_box rect.
        pygame.draw.rect(DISPLAYSURF, color, input_box, 2)
        pygame.display.flip()


# Display options to update information
def update_info_display():
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(changePriceButton, (100,20))
    DISPLAYSURF.blit(changeRatingButton, (100,80))
    DISPLAYSURF.blit(addFoodButton, (100,140))
    DISPLAYSURF.blit(removeFoodButton, (100,200))
    DISPLAYSURF.blit(backButton, (10,250))
