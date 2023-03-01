"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

MIN_SPEED = {
        0: 15,
        600: 11.428,
        1000: 13.333
        }

MAX_SPEED = {
        0: 34,
        200: 32,
        400: 30,
        600: 28,
        1000: 26
        }

DISTANCE_SPEED = {
        200: MAX_SPEED[200],
        400: MAX_SPEED[400],
        600: MAX_SPEED[600],
        1000: MAX_SPEED[1000]
        }


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    # Error catching control longer than total race distance
    if control_dist_km > brevet_dist_km:
        return None
    # Error catching if control distance is 0 or less, start time is the race start
    if control_dist_km <= 0:
        return brevet_start_time

    opening_times = []
    control_dist = control_dist_km
    for distance in DISTANCE_SPEED:
        if control_dist > distance
            time = (distance / DISTANCE_SPEED[distance])*60
            control_dist -= distance
        else:
            time = (control_dist/ DISTANCE_SPEED[distance])*60
            control_dist = 0
        opening_times.append(time)

    #max_speed_dist = next(x for x in MAX_SPEED.keys() if x <= control_dist_km)
    ride_time = sum(opening_times)
    ride_hours = math.floor(ride_time / 60)
    print(f'openH: {ride_hours}')
    ride_minutes = round(ride_time % 60)
    print(f'openM: {ride_minutes}')
    s_time = brevet_start_time.shift(hours=ride_hours, minutes=ride_minutes)
    return s_time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    # Error catching control longer than total race distance
    if control_dist_km > brevet_dist_km:
        return None
    # Error catching if control distance is 0 or less, start time is the race start + 1 hour
    if control_dist_km <= 0:
        return brevet_start_time.shift(hours=1)

    # Calculate control closing time for distances up to 600km
    if control_dist_km <= 600:
            closing_time =


    # Calculate control closing time for distances between 600km and 1000km
    if control_dist_km > 600:


    # Calculate control closing time for distances between 600km and 1000km
    if control_dist_km > 600:

    min_speed_dist = next(x for x in MIN_SPEED.keys() if x <= control_dist_km)
    ride_time = (control_dist_km / MIN_SPEED[min_speed_dist]) * 60
    ride_hours = math.floor(ride_time / 60)
    print(f'closeH= {ride_hours}')
    ride_minutes = round(ride_time % 60)
    print(f'closeM= {ride_minutes}')
    c_time = brevet_start_time.shift(hours=ride_hours, minutes=ride_minutes)

    return c_time
