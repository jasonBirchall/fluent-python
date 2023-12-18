# Chapter 2 is about sequences and collections.
# This makes more sense to me at the moment. I'll have to come back to this later.
symbols = "$¢£¥€¤"

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# This is the list comprehension version of the above code.
codes = [ord(symbol) for symbol in symbols]
print(codes)
# It's certainily more concise and easier to read.

# "A listcomp is more explicit. Its goal is always to build a new list."

# "If the list comprehension spans more than two lines, it is probably best
# to break it apart or rewrite it as a plain old for loop."
