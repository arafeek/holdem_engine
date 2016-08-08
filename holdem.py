from deck import Deck
from hand_names import Hands
import helpers

sep = "=============\n\n"

D = []
P1 = []
P2 = []
board = []

def start_game():
    global D
    global P1
    global P2
    D = Deck()
    P1 = D.take(2)
    P2 = D.take(2)

    print "Player 1 has: "
    print P1[0]
    print sep

    print "Player 2 has: "
    print P2[0]
    print sep


def flop():
    global board
    global D
    board = D.take(3);
    print "Flop is: "
    print board
    print sep

def turn():
    global board
    global D
    print "Turn:"
    board.append(D.take(1)[0])
    print board
    print sep

def river():
    global board
    global D
    print "River:"
    board.append(D.take(1)[0])
    print board
    print sep

def showdown():
    p1_score = helpers.scoreHand(P1, board)
    p2_score = helpers.scoreHand(P2, board)
    print "Player 1 has: %s" %Hands[p1_score]
    print P1
    print sep

    print "Player 2 has: %s" %Hands[p2_score]
    print P2
    print sep
    if p1_score > p2_score:
        print "Player 1 wins."
    elif p2_score > p1_score:
        print "Player 2 wins."
    else:
        print "It's a chop!"

def run_game():
    start_game()
    raw_input("Press anything for flop\n")
    flop()
    raw_input("Press anything for turn\n")
    turn()
    raw_input("Press anything for river\n")
    river()
    raw_input("Press anything for showdown\n")
    showdown()

run_game()
