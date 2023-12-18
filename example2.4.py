# Listcomps are clearer than the map and filter built-in functions because they don't require lambda expressions
# Listcomps allow us to easily skip items from the input list, a task that is clumsy with map
# Listcomps are also faster than the map and filter functions
# Listcomps can also be used to build lists of lists, tuples, sets, and even dictionaries
# Listcomps can also be used to produce lists from iterators and generators

# We want to create a list of t-shirts with all possible combinations of colours and sizes
# The listcomps syntax is similar to the one used in mathematics to describe sets
# {x² | x ∈ ℕ, x < 10}
# This is read as: "the set of all x squared such that x is a member of the set of natural numbers and x is less than 10"
# The equivalent listcomps would be:
# [x² for x in range(10)]
# The components of the listcomps are:
# 1. The output expression is x²
# 2. The input sequence is range(10)
# 3. The optional predicate is x < 10
# The same listcomps can be written as:
# listcomp = []
# for x in range(10):
#     listcomp.append(x**2)

colours = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

sizes = ['S', 'M', 'L', 'XL']

# Creates a list of tuples with all possible combinations of colours and sizes
tshirts = [(c, s) for c in colours for s in sizes]

print(tshirts)

for colour in colours:
    for size in sizes:
        print((colour, size))

# Creates a list of tuples with all possible combinations of colours and sizes and orders them by size
tshirts = [(c, s) for s in sizes for c in colours]

print(tshirts)
