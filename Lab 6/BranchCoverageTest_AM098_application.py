
import pytest
from parking_fee import parking_fee, find_slot, monthly_pass

# PARKING FEE BRANCH TESTS

def test_unknown_vehicle_branch():
    with pytest.raises(ValueError):
        parking_fee("bus", 60, False, False)

def test_valid_vehicle_branch():
    assert parking_fee("bike", 60, False, False) == 10

def test_negative_duration_branch():
    with pytest.raises(ValueError):
        parking_fee("car", -5, False, False)

def test_valid_duration_branch():
    assert parking_fee("car", 60, False, False) == 30

def test_free_parking_branch():
    assert parking_fee("car", 30, False, False) == 0

def test_paid_parking_branch():
    assert parking_fee("car", 45, False, False) == 30

def test_exact_hour_branch():
    assert parking_fee("car", 60, False, False) == 30

def test_extra_minutes_branch():
    assert parking_fee("car", 61, False, False) == 60

def test_ev_discount_branch():
    assert parking_fee("car", 60, True, False) == 15

def test_ev_truck_branch():
    assert parking_fee("truck", 60, True, False) == 60

def test_non_ev_branch():
    assert parking_fee("car", 60, False, False) == 30

def test_lost_ticket_branch():
    assert parking_fee("bike", 60, False, True) == 210

def test_normal_ticket_branch():
    assert parking_fee("bike", 60, False, False) == 10

# FIND SLOT BRANCH TESTS

def test_full_parking_branch():
    assert find_slot("car", 0, False) == "full"

def test_available_slots_branch():
    assert find_slot("car", 5, False) == "any floor"

def test_disabled_slot_branch():
    assert find_slot("car", 5, True) == "ground floor"

def test_truck_slot_branch():
    assert find_slot("truck", 5, False) == "basement"

def test_regular_vehicle_slot_branch():
    assert find_slot("bike", 5, False) == "any floor"

# MONTHLY PASS BRANCH TESTS

def test_bike_pass_branch():
    assert monthly_pass("bike", False) == 500

def test_car_pass_branch():
    assert monthly_pass("car", False) == 1500

def test_invalid_vehicle_pass_branch():
    with pytest.raises(ValueError):
        monthly_pass("truck", False)

def test_resident_discount_branch():
    assert monthly_pass("car", True) == 1200

def test_non_resident_branch():
    assert monthly_pass("car", False) == 1500
