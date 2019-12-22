'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''

# Get travelling distances in METRES from Google Maps
import googlemaps

# The following Google API key belongs to Lim Yu Jie, BCG 1, NTU, AY 2017-2018
# The API key shall not be disclosed, or used by anyone other than his project groupmates for the purpose of this project
gmaps = googlemaps.Client(key='AIzaSyATT3Jc6ZomzcF-7RMlhwJsJK7pDcjyJ4s')

# Request distance in metres from Google
def distance_by_google(origin, destination, mode):
    # Stores the retrieved dictionary result under retrieved_result
    retrieved_result = gmaps.distance_matrix(origin, destination, mode)
    # Extract the distance value from the retrieved result
    distance_required = retrieved_result['rows'][0]['elements'][0]['distance']['value']
    return(distance_required)

# Retrieve distance when mode of transport is by driving
def driving_distance(origin, destination):
    return(distance_by_google(origin, destination, mode='driving'))

# Retrieve distance when mode of transport is by walking
def walking_distance(origin, destination):
    return(distance_by_google(origin, destination, mode='walking'))

# Retrieve distance when mode of transport is by public transport
def public_transit_distance(origin, destination):
    return(distance_by_google(origin, destination, mode='transit'))


# Returns a compilation of the distances by each mode
def distances_dictionary(origin, destination):
    # Run this section if public transport is NOT available
    if public_transit_distance(origin, destination) == walking_distance(origin, destination):
        return {'Driving': driving_distance(origin, destination),
                'Walking': walking_distance(origin, destination),
                'Public Transport': 'Unavailable',
                }
    
    # Otherwise, run this section if public transport is available
    else:
        return {'Driving': driving_distance(origin, destination),
                'Walking': walking_distance(origin, destination),
                'Public Transport': public_transit_distance(origin, destination),
                }


# Converts the distance in into 4 digit string required for future sorting order
def str_distance(distance):
    if distance < 10:
        distance_str = "000" + str(distance)
    elif distance < 100:
        distance_str = "00" + str(distance)
    elif distance < 1000:
        distance_str = "0" + str(distance)
    else:
        distance_str = str(distance)
    return distance_str


# Compiles the distance from user location to each canteen selected by the user
# Canteens not selected by user will not be displayed
def get_canteen_distance_list(user_location, canteens_input, mode):
    
    # Data will be stored to this dictionary
    canteen_distance_list = []
    
    # Checks if each canteen is selected, then computes and returns the distance
    if 'Canteen 1' in canteens_input or len(canteens_input) == 2:# got problem cause canteen 1 is in canteen 13
        distance_1 = distance_by_google(user_location, 'NTU Canteen 1', mode)
        distance_1_str = str_distance(distance_1) + " metres to Canteen 1"
        canteen_distance_list.append(distance_1_str)
    if 'canteen 2' in canteens_input or len(canteens_input) == 0:
        distance_2 = distance_by_google(user_location, 'NTU Canteen 2', mode)
        distance_2_str = str_distance(distance_2) + " metres to Canteen 2"
        canteen_distance_list.append(distance_2_str)
    if 'canteen 9' in canteens_input or len(canteens_input) == 0:
        distance_9 = distance_by_google(user_location, 'NTU Canteen 9', mode)
        distance_9_str = str_distance(distance_9) + " metres to Canteen 9"
        canteen_distance_list.append(distance_9_str)
    if 'canteen 11' in canteens_input or len(canteens_input) == 0:
        distance_11 = distance_by_google(user_location, 'NTU Canteen 11', mode)
        distance_11_str = str_distance(distance_11) + " metres to Canteen 11"
        canteen_distance_list.append(distance_11_str)
    if 'canteen 13' in canteens_input or len(canteens_input) == 0:
        distance_13 = distance_by_google(user_location, 'NTU Canteen 13', mode)
        distance_13_str = str_distance(distance_13) + " metres to Canteen 13"
        canteen_distance_list.append(distance_13_str)
    if 'canteen 14' in canteens_input or len(canteens_input) == 0:
        distance_14 = distance_by_google(user_location, 'NTU Canteen 14', mode)
        distance_14_str = str_distance(distance_14) + " metres to Canteen 14"
        canteen_distance_list.append(distance_14_str)
    if 'canteen 16' in canteens_input or len(canteens_input) == 0:
        distance_16 = distance_by_google(user_location, 'NTU Canteen 16', mode)
        distance_16_str = str_distance(distance_16) + " metres to Canteen 16"
        canteen_distance_list.append(distance_16_str)
    if 'tamarind canteen' in canteens_input or len(canteens_input) == 0:
        distance_tamarind = distance_by_google(user_location, 'NTU Foodgle Food Court', mode)
        distance_tamarind_str = str_distance(distance_tamarind) + " metres to Tamarind Canteen"
        canteen_distance_list.append(distance_tamarind_str)
    if 'north hill canteen' in canteens_input or len(canteens_input) == 0:
        distance_north_hill = distance_by_google(user_location, 'NTU North Hill Food Court', mode)
        distance_north_hill_str = str_distance(distance_north_hill) + " metres to North Hill Canteen"
        canteen_distance_list.append(distance_north_hill_str)
    if 'pioneer canteen' in canteens_input or len(canteens_input) == 0:
        distance_pioneer = distance_by_google(user_location, 'NTU Pioneer Hall', mode)
        distance_pioneer_str = str_distance(distance_pioneer) + " metres to Pioneer Canteen"
        canteen_distance_list.append(distance_pioneer_str)
    if 'koufu canteen' in canteens_input or len(canteens_input) == 0:
        # minimum function gives the better estimated distance
        distance_koufu =min( \
                            distance_by_google(user_location, 'Canteen B Koufu @ the South Spine', mode),   \
                            distance_by_google(user_location, 'NTU Lee Kong Chian Lecture Theatre', mode))
                            # NTU Lee Kong Chian Lecture Theatre may give a better estimate than Canteen B Koufu @ the South Spine
        distance_koufu_str = str_distance(distance_koufu) + " metres to Koufu"
        canteen_distance_list.append(distance_koufu_str)
    if 'north spine canteen' in canteens_input or len(canteens_input) == 0:
        distance_nsc = distance_by_google(user_location, 'NTU North Spine Food Court', mode)
        distance_nsc_str = str_distance(distance_nsc) + " metres to North Spine Canteen"
        canteen_distance_list.append(distance_nsc_str)
    if 'nie canteen' in canteens_input or len(canteens_input) == 0:
        distance_nie = distance_by_google(user_location, 'NTU NIE Canteen', mode)
        distance_nie_str = str_distance(distance_nie) + " metres to NIE Canteen"
        canteen_distance_list.append(distance_nie_str)
    
    return canteen_distance_list


# Calculates direct distance between two points
def direct_distance(user_location, destination_location):
    # Ratio of actual distance (in metres) to pixel distance
    multiplier = 2.31313131
    
    user_location_x = float(user_location[0])
    user_location_y = float(user_location[1])
    
    destination_location_x = float(destination_location[0])
    destination_location_y = float(destination_location[1])

    squared_distance = (user_location_x - destination_location_x)**2 + (user_location_y - destination_location_y)**2
    direct_distance = (squared_distance)**0.5
    actual_distance_metres = round(direct_distance * multiplier, 2)
    return actual_distance_metres


