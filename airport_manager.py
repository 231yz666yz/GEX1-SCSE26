######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = ("OUL", 1, "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"],
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"],
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"],
    },
}


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    target = flight_number.strip().upper()

    for stored_number in flights:
        if stored_number.strip().upper() == target:
            return stored_number

    return None

## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    target = passenger_name.strip().lower()

    for stored_name in passengers:
        if stored_name.strip().lower() == target:
            return True

    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    clean_name = passenger_name.strip().title()

    if clean_name == "":
        return "EMPTY_NAME"

    flight = flights[key]

    if passenger_exists(flight["passengers"], clean_name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    flight["passengers"].append(clean_name)

    return "OK"

## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[key]

    if not passenger_exists(flight["passengers"], passenger_name):
        return "PASSENGER_NOT_FOUND"

    flight["passengers"].remove(passenger_name.strip().title())
    return "OK"

# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    gate = new_gate.strip().upper()

    if gate not in allowed_gates:
        return "INVALID_GATE"

    flights[key]["gate"] = gate

    return "OK"

# Logic to get the status of a flight
def flight_status(flight):
    capacity = flight["capacity"]

    if capacity == 0:
        return "AVAILABLE"

    percentage = len(flight["passengers"]) / capacity * 100

    if percentage == 100:
        return "FULL"

    if percentage >= 75:
        return "ALMOST FULL"

    return "AVAILABLE"

# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)

    if key is None:
        return None

    return sorted(flights[key]["passengers"])

# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    return sum(
        len(flight["passengers"])
        for flight in flights.values()
    )

# Logic to check if any flight is full
def any_full_flight(flights):
    return any(
        len(flight["passengers"]) >= flight["capacity"]
        for flight in flights.values()
    )

# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    return all(
        len(flight["passengers"]) > 0
        for flight in flights.values()
    )