
state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacremento"}

"""for state in state_capitals:
    print(state)"""

"""for city in state_capitals.values():
    print(city)"""

# for state in state_capitals:
#     print(state_capitals[state], "is the capitol of", state)


for state, city in state_capitals.items():
    print(city, "is the capitol of", state)