import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    This lesson is about the special methods that make objects behave like the built-in types. You can use a number of
    built in functions like len, iter, str, reversed, sorted, etc. on the object. The special method that makes this"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """This is the constructor for the class. It is called when the object is created. It is used to initialize the
        object's state. In this case, it is used to create a list of cards.
        """
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        """This is a special method that makes the object behave like a sequence. It is called when the len() function is
        called on the object.
        """
        return len(self._cards)

    def __getitem__(self, position):
        """This is a special method that makes the object behave like a sequence. It is called when the [] operator is
        used on the object."""
        return self._cards[position]
