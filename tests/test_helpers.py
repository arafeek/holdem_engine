import unittest
from .context import holdem

class TestHandScoring(unittest.TestCase):
    "Tests the scoreHand function in correctly recognizing various hands"
    def testAceLowStraightFlush(self):
        "Tests for a Straight flush (Ace Low)"
        hand = [(2, 'c'), (4, 'c')]
        board = [(5, 'c'), (12, 'd'), (3, 'c'), (14, 'c'), (8, 's')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 8000)

    def testAceHighStraightFlush(self):
        "Tests for a straight flush (Ace High)"
        hand = [(10, 'd'), (14, 'd')]
        board = [(2, 'c'), (12, 'd'), (13, 'd'), (14, 'c'), (11, 'd')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 8000)

    def testQuads(self):
        "Tests for 4 of a kind"
        hand = [(10, 'd'), (10, 'c')]
        board = [(2, 'c'), (10, 's'), (13, 'd'), (10, 'h'), (11, 'd')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 7007)

    def testFullHouse(self):
        "Tests for a full house"
        hand = [(10, 'd'), (10, 'c')]
        board = [(2, 'c'), (10, 's'), (13, 'd'), (13, 'h'), (11, 'd')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 6060)

    def testFlush(self):
        "Tests for a flush"
        hand = [(10, 'd'), (2, 'c')]
        board = [(3, 'c'), (10, 's'), (13, 'c'), (10, 'c'), (11, 'c')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 5055)

    def testStraight(self):
        "Tests for a straight"
        hand = [(6, 'd'), (7, 'c')]
        board = [(5, 'c'), (8, 's'), (13, 'c'), (10, 's'), (4, 'h')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 4400)

    def testTrips(self):
        "Tests for 3 of a kind"
        hand = [(10, 'd'), (2, 'c')]
        board = [(3, 'h'), (10, 's'), (13, 'c'), (10, 'c'), (11, 'c')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 3303)

    def testTwoPair(self):
        "Tests for two pair"
        hand = [(10, 'd'), (2, 'c')]
        board = [(3, 'h'), (10, 's'), (13, 'c'), (2, 'h'), (11, 'c')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 2220)

    def testPair(self):
        "Tests for a pair"
        hand = [(10, 'd'), (2, 'c')]
        board = [(3, 'h'), (10, 's'), (13, 'c'), (6, 'h'), (11, 'c')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 1111)

    def testHighCard(self):
        "Tests for valid high card"
        hand = [(10, 'd'), (2, 'c')]
        board = [(3, 'h'), (6, 's'), (13, 'c'), (5, 'c'), (11, 'c')]
        self.assertEqual(holdem.helpers.scoreHand(hand, board), 13)

if __name__ == '__main__':
    unittest.main()
