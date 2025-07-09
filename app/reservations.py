def check_availability(reservations, new):
    """
    Check if a new reservation can be made without conflicting with existing reservations.
    
    :param reservations: List of existing reservations, each a dictionary with 'room' and 'time'.
    :param new: New reservation to check, a dictionary with 'room' and 'time'.
    :return: True if the new reservation can be made, False otherwise.
    """
    for reservation in reservations:
        if (new['room'] == reservation['room'] and new['time'] == reservation['time']):
            return False
    return True