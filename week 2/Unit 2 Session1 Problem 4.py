# Problem 4: Scheduling Conflict
# Demand for your festival has exceeded expectations, 
# so you're expanding the festival to span two different venues. 
# Some artists will perform both venues, while others will perform at just one. 
# To ensure that there are no scheduling conflicts, implement a function 
# identify_conflicts() that accepts two dictionaries venue1_schedule and 
# venue2_schedule each mapping the artists playing at the venue to their set times. 
# Return a dictionary containing the key-value pairs that are the same in each schedule.

# Understand:
# input: 2 dictionaries
# output: a dictionary containing the key-value pairs that are the same in each schedule

# Plan:
# 1. Initialize an empty dictionary to store conflicts.
# 2. Iterate through the keys in the first dictionary.
# 3. Check if the key is present in the second dictionary.
# 4. If the key is present, check if the values are the same.
# 5. If the values are the same, add the key-value pair to the conflicts dictionary.
# 6. Return the conflicts dictionary.


def identify_conflicts(venue1_schedule, venue2_schedule):
    # 1. Initialize an empty dictionary to store conflicts.
    conflicts = {}
    # 2. Iterate through the keys in the first dictionary.
    for artist in venue1_schedule:
        # 3. Check if the key is present in the second dictionary.
        if artist in venue2_schedule:
    # 4. If the key is present, check if the values are the same.
            if venue1_schedule[artist] == venue2_schedule[artist]:
                # 5. If the values are the same, add the key-value pair to the conflicts dictionary.
                conflicts[artist] = venue1_schedule[artist]
    # 6. Return the conflicts dictionary.
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))