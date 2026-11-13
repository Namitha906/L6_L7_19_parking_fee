
import pytest
from parking_fee import parking_fee, find_slot, monthly_pass

# PARKING FEE TESTS

def test_unknown_vehicle():
    with pytest.raises(ValueError):
        parking_fee("bus", 60, False, False)

def test_negative_duration():
    with pytest.raises(ValueError):
        parking_fee("car", -10, False, False)

def test_free_short_stay():
    assert parking_fee("car", 20, False, False) == 0

def test_exactly_30_minutes():
    assert parking_fee("bike", 30, False, False) == 0

def test_parking_31_minutes():
    assert parking_fee("car", 31, False, False) == 30

def test_parking_exactly_one_hour():
    assert parking_fee("car", 60, False, False) == 30

def test_parking_more_than_one_hour():
    assert parking_fee("car", 61, False, False) == 60

def test_ev_discount():
    assert parking_fee("car", 60, True, False) == 15

def test_ev_truck_no_discount():
    assert parking_fee("truck", 60, True, False) == 60

def test_lost_ticket_charge():
    assert parking_fee("bike", 60, False, True) == 210

# FIND SLOT TESTS

def test_no_free_slots():
    assert find_slot("car", 0, False) == "full"

def test_disabled_parking():
    assert find_slot("car", 5, True) == "ground floor"

def test_truck_slot():
    assert find_slot("truck", 5, False) == "basement"

def test_any_floor():
    assert find_slot("car", 5, False) == "any floor"

# MONTHLY PASS TESTS

def test_bike_monthly_pass():
    assert monthly_pass("bike", False) == 500

def test_car_monthly_pass():
    assert monthly_pass("car", False) == 1500

def test_resident_bike_discount():
    assert monthly_pass("bike", True) == 400

def test_resident_car_discount():
    assert monthly_pass("car", True) == 1200

def test_invalid_monthly_pass():
    with pytest.raises(ValueError):
        monthly_pass("truck", False)
