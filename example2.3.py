symbols = "$¢£¥€¤"

# "Listcomps versus map and filter"
# "Listcomps do everything the map and filter functions do, without the contortions"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
