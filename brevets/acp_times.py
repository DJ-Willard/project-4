"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

MIN_SPEED = {
        0: 15,
        200: 15,
        400: 15,
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
    # Error catching control longer then total race distance
    if control_dist_km > brevet_dist_km:
        return None
    # Error catching if control distance is 0 or less start time is the race start
    if control_dist_km <= 0:
        return brevet_start_time
    if control_dist_km < 0:
        return None

    ride_time = (control_dist_km/ MAX_SPEED[min(control_dist_km, 1000)]) * 60
    ride_hours = math.floor(ride_time/60)
    ride_minutes = math.floor(ride_time % 60)

    return brevet_start_time.shift(hours= ride_hours, minutes= ride_minutes)


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

    # Error catching control longer then total race distance
    if control_dist_km > brevet_dist_km:
        return None
    # Error catching if control distance is 0 or less start time is the race start
    if control_dist_km <= 0:
        return brevet_start_time.shift(hours=1)

    ride_time = (control_dist_km/ MIN_SPEED[min(control_dist_km, 1000)]) * 60
    ride_hours = math.floor(ride_time/60)
    ride_minutes = math.floor(ride_time % 60)

    return brevet_start_time.shift(hours= ride_hours, minutes= ride_minutes)
