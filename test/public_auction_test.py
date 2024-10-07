import unittest

from public_auction.algorithm.auction_brute_force import auction_brute_force
from public_auction.algorithm.auction_dp import auction_dp
from public_auction.algorithm.auction_greedy import auction_greedy

class PublicAuctionTest(unittest.TestCase):

    def test_auction_brute_force(self):
        print("\nTesting auction_brute_force...")
        A = 1000
        B = 100
        n = 2
        offers = [{'price': 500, 'min': 100, 'max': 600}, 
                  {'price': 450, 'min': 400, 'max': 800},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 400, 0]
        expected_vr = 480000
        assignment, vr = auction_brute_force(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 1: OK")

        n = 3
        offers = [{'price': 500, 'min': 100, 'max': 600}, 
                  {'price': 45, 'min': 400, 'max': 800},
                  {'price': 300, 'min': 100, 'max': 300},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 0, 300, 100]
        expected_vr = 400000
        assignment, vr = auction_brute_force(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 2: OK")

        n = 3
        offers = [{'price': 500, 'min': 100, 'max': 200}, 
                  {'price': 450, 'min': 400, 'max': 300},
                  {'price': 600, 'min': 100, 'max': 1000},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [0, 0, 1000, 0]
        expected_vr = 600000
        assignment, vr = auction_brute_force(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 3: OK")

    def test_auction_dp(self):
        print("\nTesting auction_dp...")
        A = 1000
        B = 100
        n = 2
        offers = [{'price': 500, 'min': 100, 'max': 600}, 
                  {'price': 450, 'min': 400, 'max': 800},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 400, 0]
        expected_vr = 480000
        assignment, vr = auction_dp(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 1: OK")

        n = 3
        offers = [{'price': 500, 'min': 100, 'max': 600}, 
                  {'price': 45, 'min': 400, 'max': 800},
                  {'price': 300, 'min': 100, 'max': 300},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 0, 300, 100]
        expected_vr = 400000
        assignment, vr = auction_dp(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 2: OK")

        n = 4
        offers = [{'price': 500, 'min': 400, 'max': 600},
                  {'price': 450, 'min': 100, 'max': 400},
                  {'price': 400, 'min': 100, 'max': 400},
                  {'price': 200, 'min': 50, 'max': 200},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 400, 0, 0, 0]
        expected_vr = 480000
        assignment, vr = auction_dp(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 3: OK")

    def test_auction_greedy(self):
        print("\nTesting auction_greedy...")
        A = 1000
        B = 100
        n = 2
        offers = [{'price': 500, 'min': 100, 'max': 600}, 
                  {'price': 450, 'min': 400, 'max': 800},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 400, 0]
        expected_vr = 480000
        assignment, vr = auction_greedy(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 1: OK")

        n = 3
        offers = [{'price': 500, 'min': 100, 'max': 600}, 
                  {'price': 45, 'min': 400, 'max': 800},
                  {'price': 300, 'min': 100, 'max': 300},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 0, 300, 100]
        expected_vr = 400000
        assignment, vr = auction_greedy(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 2: OK")

        n = 4
        offers = [{'price': 500, 'min': 400, 'max': 600},
                  {'price': 450, 'min': 100, 'max': 400},
                  {'price': 400, 'min': 100, 'max': 400},
                  {'price': 200, 'min': 50, 'max': 200},
                  {'price': 100, 'min': 0, 'max': 1000}]
        expected_assignment = [600, 400, 0, 0, 0]
        expected_vr = 480000
        assignment, vr = auction_greedy(A, B, n, offers)
        self.assertEqual(assignment, expected_assignment, 'The assignment is not correct.')
        self.assertEqual(vr, expected_vr, 'The value is not correct.')
        print("Test 3: OK")

if __name__ == '__main__':
    unittest.main()
