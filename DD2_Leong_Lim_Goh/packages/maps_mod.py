'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''
# This module is necessary for getting user location and converting it into latitude and longitude

import pygame
import sys

# Display screen height and width setting
# DO NOT MODIFY as it will affect the get_user_location() function further below
screen_width = 696
screen_height = 835

def display_map():
    # Load the map image from current directory
    Map_Image = pygame.image.load("NTU Campus Map.png")
    # Initialise display window with input size
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Rescale the map image size to FIT display window size.
    # DO NOT MODIFY as it will affect the get_user_location() function below
    Map_Image = pygame.transform.scale(Map_Image, (screen_width, screen_height))
    # add the image over the screen object
    screen.blit(Map_Image,(0,0))
    # Update the contents of the entire display window
    pygame.display.flip()


# Mouse Click get display map coordinates
def MouseClick():
    finish = False
    while finish == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                finish = True
    return (mouseX, mouseY)


# Gets user location on the map with mousclick then returns latitude and longitude coordinates
def get_user_location():
    display_map() # displays map
    pygame.display.flip() # will update the contents of the entire display window
    cord_X, cord_Y = MouseClick() # get outputs of Mouseclick event handler 
    
    multiplier = 0.0000204531  # Ratio for latitude & longitude to pixel distance
    
    # To account for the small offset in position. Note that some negligible discrepancy might still exist
    lat_offset = -0.000070
    long_offset = 0.000180
    
    # Reference points on the map with known latitudes and longitudes. Note that changing the map scale will render these references uselss
    reference_a = (32, 387, 1.348379, 103.676666)
    reference_b = (152, 730, 1.341361, 103.679119)
    reference_c = (237, 692, 1.342129, 103.680878)
    reference_d = (359, 492, 1.346213, 103.683369)
    reference_e = (439, 328, 1.349579, 103.685000)
    reference_f = (467, 579, 1.344493, 103.685584)
    reference_g = (591, 697, 1.342026, 103.688113)
    reference_h = (603, 554, 1.344960, 103.688366)

    reference_list = [reference_a, reference_b, reference_c, reference_d, reference_e, reference_f, reference_g, reference_h]
    
    sum_of_latitude = float(0)
    sum_of_longitude = float(0)
    
    # Calculates the average of the position to every reference point so as to return a more accurate coordinate
    while True:
        for ref in reference_list:
            latitude = ref[2] + (ref[1] - cord_Y) * multiplier
            sum_of_latitude += latitude
            longitude = ref[3] - (ref[0] - cord_X) * multiplier
            sum_of_longitude += longitude
                
        ave_latitude = round(sum_of_latitude / len(reference_list) + lat_offset, 6)
        ave_longitude = round(sum_of_longitude / len(reference_list) + long_offset, 6)
        
        return ave_latitude, ave_longitude