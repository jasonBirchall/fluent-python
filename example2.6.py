# Tuples are immutable, but they can contain mutable objects.
# The tuple holds references to items, and those references are not mutable.
#
# They can also hold records with no field names. Each item in the tuple holds the data for one field and the position of the item gives its meaning.

# If you think of a an immutable list, the quantities and the order of the items may not be important, depending on the context. But when a tuple is used to represent a collection of fields, the number of items is often fixed and their order is always vital.
lax_coordinates = (33.9425, -118.408056)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)
