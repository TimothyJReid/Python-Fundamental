#numbers_set = {1, 2, 3, 4, 4} # Duplicate valuse removed
# numbers_set = {1, 2, 3, 4, [5, 6]} # Cannot use mutalbe data types
from urllib.request import AbstractDigestAuthHandler


# numbers_set = {1, 2, 3, 4, (5, 6)} # A tuple is a inmmutable data type, so it is ok.
# print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
# abcd = ""
# for word in words_set:
#     abcd += word
# print(abcd)

# if "Alpha" in words_set:
#     print("Alpha is in set")
# else:
#     print("Alpha is not set")

words_set.add("Delta")
# print(words_set)
words_set.discard("Bravo")
print(words_set)

my_string = "Nucamp"
print(my_string[3:5])