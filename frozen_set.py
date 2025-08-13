#frozen set

fs=frozenset([1, 2, 3, 4, 5])
print(fs)

#frozen set functions
print(fs.union([6, 7, 8]))
print(fs.intersection([3, 4, 5, 6]))
print(fs.difference([1, 2, 3]))
print(fs.issubset([1, 2, 3, 4, 5, 6]))
print(fs.issuperset([1, 2, 3, 4, 5]))

