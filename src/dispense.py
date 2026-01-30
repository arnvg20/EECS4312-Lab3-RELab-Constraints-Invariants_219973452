
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.
    """

    # Maximum daily dose limits (example values)
    MAX_DAILY_DOSE = {
        "Aspirin": 4000,
        "Ibuprofen": 3200,
        "Paracetamol": 3000
    }

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.
        """

        # Constraint: Dose must be positive
        if dose_mg <= 0:
            raise ValueError("Dose must be a positive value")

        # Constraint: Quantity must be positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        # Constraint: Medication must exist
        if medication not in self.MAX_DAILY_DOSE:
            raise ValueError("Unknown medication")

        # Constraint: Dose must not exceed maximum allowed dose
        if dose_mg > self.MAX_DAILY_DOSE[medication]:
            raise ValueError("Dose exceeds maximum daily dose")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
        """

        # Invariant: Same patient cannot receive same medication more than once per day
        for event in existing_events:
            if (event.patient_id == new_event.patient_id and
                    event.medication == new_event.medication):
                return False

        return True
