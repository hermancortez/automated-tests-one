from app.reservations import check_availability
def test_check_availability():
    # Test case 1: Check availability for a date with no reservations
    reservations = [
        {"room":"A","time":"10:00"},
        {"room":"A","time":"11:00"},
    ]
    new = {"room":"A","time":"12:00"}
    assert check_availability(reservations, new) == True
    
def test_not_available():
    # Test case 2: Check availability for a date with existing reservations
    reservations = [
        {"room":"A","time":"10:00"},
        {"room":"A","time":"11:00"},
    ]
    new = {"room":"A","time":"11:00"}
    assert check_availability(reservations, new) == False