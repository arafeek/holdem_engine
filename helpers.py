import operator

# Encapsulated this in a function in case I decide to change how
# Ace is represented
def isAce(card):
    "Returns True iff card is an Ace"
    return card[0] == 14

def isConnected(c1, c2):
    "Returns True if c1 = c2 + 1 or vice versa. False otherwise"
    return (abs(c1[0] - c2[0]) == 1) or (isAce(c1) or isAce(c2) and (c2[0] == 2 or c1[0] == 2))


def sort(cards):
    "Returns a list of cards sorted by value"
    return sorted(cards, key=operator.itemgetter(0))

def getPairs(cards):
    "Returns a dictionary containing the count of each card present in the hand + board"
    d = {}
    for card in cards:
        key = card[0]
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

def countSuits(cards):
    "Returns a dict containing the counts of each suit in cards"
    d = {}
    for card in cards:
        suit = card[1]
        if suit not in d:
            d[suit] = 1
        else:
            d[suit] += 1
    return d

def countConnectors(cards):
    "Returns the length of the longest continious set of cards"
    count = 1
    max_count = 1
    sorted_cards = sort(cards)
    if (sorted_cards[0][0] == 2 and isAce(sorted_cards[-1])): #check for A-2 case
        count = 2
        max_count = 2
    for i in range(1, len(sorted_cards)):
        if (isConnected(sorted_cards[i-1], sorted_cards[i])):
            count += 1
            if count > max_count:
                max_count = count
        elif (sorted_cards[i-1] != sorted_cards[i]): #if they're the same, just move on
            # we know we caqn reset count since the cards are sorted
            if count > max_count:
                max_count = count

            count = 1
    return max_count

            


