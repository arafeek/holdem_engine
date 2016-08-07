from deck import Deck


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
    print "Player 1 has: "
    print P1
    print sep

    print "Player 2 has: "
    print P2
    print sep

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
