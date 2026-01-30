# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import pytest
from src.dispense import DispenseEvent


# Requirement: Dose must be positive
def test_reject_negative_dose():
    with pytest.raises(ValueError):
        DispenseEvent("P001", "Aspirin", -50, 1)


# Requirement: Quantity must be positive integer
def test_reject_zero_quantity():
    with pytest.raises(ValueError):
        DispenseEvent("P002", "Ibuprofen", 200, 0)


# Requirement: Dose must not exceed maximum daily dose
def test_reject_exceeding_max_dose():
    with pytest.raises(ValueError):
        DispenseEvent("P003", "Paracetamol", 5000, 1)


# Requirement: Same medication cannot be dispensed twice to same patient
def test_prevent_duplicate_dispensing():

    existing_events = []

    event1 = DispenseEvent("P004", "Aspirin", 500, 1)
    existing_events.append(event1)

    event2 = DispenseEvent("P004", "Aspirin", 300, 1)

    result = DispenseEvent.invariant_holds(existing_events, event2)

    assert result is False
