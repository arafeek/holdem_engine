import operator

# Encapsulated this in a function in case I decide to change how
# Ace is represented
def isAce(card):
    "Returns True iff card is an Ace"
    return card[0] == 14

def isConnected(c1, c2):
    "Returns True if c1 = c2 + 1 or vice versa. False otherwise"
    return (abs(c1[0] - c2[0]) == 1) or (isAce(c1) or isAce(c2) and (c2[0] == 2 or c1[0] == 2))

def isSuited(c1, c2):
    "Returns True iff c1 and c2 have the same suit. False otherwise"
    return c1[1] == c2[1]

def areSuitedConnectors(c1, c2):
    "Returns True iff c1 and c2 are suited connectors"
    return isConnected(c1, c2) and isSuited(c1, c2)

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
        elif (sorted_cards[i-1][0] != sorted_cards[i][0]): #if they're the same, just move on
            # we know we caqn reset count since the cards are sorted
            if count > max_count:
                max_count = count

            count = 1
    return max_count

def countSuitedConnectors(cards):
    "Returns the length of the longest continous set of suited cards"
    count = 1
    max_count = 1
    sc = sort(cards)
    # Check for possibility of Ace-low straight
    if (sc[0][0] == 2 and isAce(sc[-1]) and areSuitedConnectors(sc[0], sc[-1])):
        count = 2
        max_count = 2

    for i in range(1, len(sc)):
        if(areSuitedConnectors(sc[i - 1], sc[i])):
            count += 1
            if count > max_count:
                max_count = count
        elif (sc[i-1][0] != sc[i][0]):
            if count > max_count:
                max_count = count

            count = 1
    return max_count

def getFlush(cards):
    "Returns the suit of the flush if one exists. False otherwise"
    suit_counts = countSuits(cards)
    for suit in suit_counts:
        if suit_counts[suit] >= 5:
            return suit
    return False

def hasStraight(cards):
    "Returns True if a straight exits. False otherwise"
    return countConnectors(cards) >= 5

def hasStraightFlush(cards):
    return countSuitedConnectors(cards) >= 5

def scoreHand(hand, board):
    "Evaluates a hand and board and returns the relevant hand code"
    cards = hand + board
    pairs = []
    trips = []
    quads = []
    rest = []
    counts = getPairs(cards)

    for val in counts:
        if counts[val] == 2:
            pairs.append(val)
        elif counts[val] == 3:
            trips.append(val)
        elif counts[val] == 4:
            quads.append(val)
        else:
            rest.append(val) # singletons (highcard contenders)

    if hasStraightFlush(cards):
        # straight flush
        return 8000
    elif len(quads) == 1:
        # 4 of a kind
        return  7007
    elif len(trips) >= 1 and len(pairs) >=1:
        # full house
        return 6060
    elif getFlush(cards) != False:
        # flush
        return 5055
    elif hasStraight(cards):
        # straight
        return 4400
    elif len(trips) >= 1:
        # 3 of a kind
        return 3303
    elif len(pairs) >= 2:
        # 2 pair
        return 2220
    elif  len(pairs) == 1:
        # pair
        return 1111
    else:
        # high card
        return max(rest)

