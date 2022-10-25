states = ["Washinton", "Oregon", "California"]

"""print(states[-1])
print(states[-2])
print(states[-3])
"""

states[2] = "Arizona"
# print(states)

# print(len(states))

# add to the end of a list
states.append("New York")
print(states)

# Remove the last list item from a list
states.pop()
print(states)

# Remove a specific list item
states.pop(1)
print(states)
