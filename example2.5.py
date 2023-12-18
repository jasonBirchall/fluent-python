# Genexps use the same symtax as listcomps, but are enclosed in parentheses rather than brackets.

import array

symbols = "$¢£¥€¤"
# If the generator expression is the single argument in a function call, there is no need to duplicate the enclosing parentheses
print(tuple(ord(symbol) for symbol in symbols))


# The array constructor takes two arguments, so the parentheses around the generator expression are mandatory
print(array.array('I', (ord(symbol) for symbol in symbols)))

# Generator expressions (genexps) are more memory-friendly than list comprehensions (listcomps) because they generate values on the fly, not needing to store all the values in memory at once like list comprehensions do. This makes genexps a better choice when dealing with large data streams or when the generated list is only iterated over once.

# However, genexps are not always the best choice. If you need to reuse the generated values, then a list comprehension is a better choice because genexps are single use. They generate the values on the fly and do not store them, so if you try to iterate over a generator expression a second time, it won't return any values.

colors = ['black', 'white']

sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
