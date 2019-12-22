# Get travelling time in SECONDS from Google Maps
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyATT3Jc6ZomzcF-7RMlhwJsJK7pDcjyJ4s')

# Request durations in general
def duration_from_google(origin, destination, mode):
    # Stores the retrieved dictionary result under retrieved_result
    retrieved_result = gmaps.distance_matrix(origin, destination, mode, departure_time = datetime.now())
    # Extract the rows list and store under rows_list variable
    duration = retrieved_result['rows'][0]['elements'][0]['duration']['value']
    return(duration)

# Retrieve duration when mode of transport is by driving
def driving_duration(origin, destination):
    return(duration_from_google(origin, destination, mode='driving'))

# Retrieve duration when mode of transport is by walking
def walking_duration(origin, destination):
    return(duration_from_google(origin, destination, mode='walking'))

# Retrieve duration when mode of transport is by public transport
def public_transit_duration(origin, destination):
    return(duration_from_google(origin, destination, mode='transit'))

# Test code below
# print(driving_duration('NTU Hall 12', 'NTU Hall 5'))


# Returns a compilation of the durations by each mode
def duration_dictionary(origin, destination):
    # Run this section if public transport is NOT available
    if public_transit_duration(origin, destination) == walking_duration(origin, destination):
        return {'Driving': driving_duration(origin, destination),
                'Walking': walking_duration(origin, destination),
                'Public Transport': 'Unavailable',
                }
    
    # Otherwise, run this section if public transport is available
    else:
        return {'Driving': driving_duration(origin, destination),
                'Walking': walking_duration(origin, destination),
                'Public Transport': public_transit_duration(origin, destination),
                }

# Test code below
# print(duration_dictionary('NTU Hall 12', 'NTU Hall 5'))