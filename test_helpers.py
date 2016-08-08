import unittest
from helpers import scoreHand

class TestHandScoring(unittest.TestCase):
    "Tests the scoreHand function in correctly recognizing various hands"
    def testAceLowStraightFlush(self):
        "Tests for a Straight flush (Ace Low)"
        hand = [(2, 'c'), (4, 'c')]
        board = [(5, 'c'), (12, 'd'), (3, 'c'), (14, 'c'), (8, 's')]
        self.assertEqual(scoreHand(hand, board), 8000)

    def testAceHighStraightFlush(self):
        "Tests for a straight flush (Ace High)"
        hand = [(10, 'd'), (14, 'd')]
        board = [(2, 'c'), (12, 'd'), (13, 'd'), (14, 'c'), (11, 'd')]
        self.assertEqual(scoreHand(hand, board), 8000)

    def testQuads(self):
        "Tests for 4 of a kind"
        hand = [(10, 'd'), (10, 'c')]
        board = [(2, 'c'), (10, 's'), (13, 'd'), (10, 'h'), (11, 'd')]
        self.assertEqual(scoreHand(hand, board), 7007)

    def testFullHouse(self):
        "Tests for a full house"
        hand = [(10, 'd'), (10, 'c')]
        board = [(2, 'c'), (10, 's'), (13, 'd'), (13, 'h'), (11, 'd')]
        self.assertEqual(scoreHand(hand, board), 6060)

    def testFlush(self):
        hand = [(10, 'd'), (2, 'c')]
        board = [(3, 'c'), (10, 's'), (13, 'c'), (10, 'c'), (11, 'c')]
        self.assertEqual(scoreHand(hand, board), 5055)
if __name__ == '__main__':
    unittest.main()
