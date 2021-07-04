import unittest


class BowlingGame(object):
    def __init__(self):
        self.throws = []
        self.score = 0

    def throw(self, pins):
        self.throws.append(pins)

    def calculate_score(self):
        ball = 0
        for frames in range(10):
            # new method that is called if game is incomplete and exits if all frames calculated
            if ball == len(self.throws):
                break
            elif ball > len(self.throws) or ball + 1 > len(self.throws):
                self.score += self.throws[ball]
                break
            elif self.throws[ball] == 10:
                self.score += 10 + self.throws[ball + 1] + self.throws[ball + 2]
                ball += 1
            elif self.throws[ball] + self.throws[ball + 1] == 10:
                self.score += 10 + self.throws[ball + 2]
                ball += 2
            else:
                self.score += self.throws[ball] + self.throws[ball + 1]
                ball += 2


class BowlingGameTests(unittest.TestCase):
    def throw_many(self, game, number_of_times, pins):
        for _ in range(number_of_times):
            game.throw(pins)

    def test_perfect_game(self):
        game = BowlingGame()
        self.throw_many(game, 12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    def test_all_ones(self):
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        self.throw_many(game, number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    def test_different_throws(self):
        game = BowlingGame()
        game.throw(6)
        game.throw(0)
        game.throw(7)
        game.throw(0)
        game.throw(2)
        for _ in range(15):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 15)

    def test_for_spare(self):
        game = BowlingGame()
        game.throw(4)
        game.throw(6)
        game.throw(7)
        game.throw(0)
        for _ in range(16):
            game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 24)

    def test_for_strike(self):
        game = BowlingGame()
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 17, 0)
        game.calculate_score()
        self.assertEqual(game.score, 22)

    # Test Case ID 2.a - this test will show that 21 balls and all [0,10] and [0,10,0] returns correct
    # value of 100
    def test_for_game_of_spares_version_A(self):
        game = BowlingGame()
        for _ in range(10):
            game.throw(0)
            game.throw(10)
        game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 100)

    # Test Case ID 2.b - this will show 21 balls and 10 spares with a different high score of Test Case ID 2.a
    # expected score is 101
    def test_for_game_of_spares_version_B(self):
        game = BowlingGame()
        for _ in range(9):
            game.throw(0)
            game.throw(10)
        game.throw(1)
        game.throw(9)
        game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 101)

    # Test Case ID 2.c - this tests a game of ten spares and strike at the end similar to 2.a and 2.b
    # Expected score is 110
    def test_for_game_of_spares_version_C(self):
        game = BowlingGame()
        for _ in range(10):
            game.throw(0)
            game.throw(10)
        game.throw(10)
        game.calculate_score()
        self.assertEqual(game.score, 110)

    # Test Case ID 2.d - this tests a game of all different combination of spares in one game
    # Expected score 144
    def test_for_game_of_spares_version_D(self):
        game = BowlingGame()
        game.throw(1)
        game.throw(9)
        game.throw(2)
        game.throw(8)
        game.throw(3)
        game.throw(7)
        game.throw(4)
        game.throw(6)
        game.throw(5)
        game.throw(5)
        game.throw(6)
        game.throw(4)
        game.throw(7)
        game.throw(3)
        game.throw(8)
        game.throw(2)
        game.throw(9)
        game.throw(1)
        game.throw(0)
        game.throw(10)
        game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 144)

    # Test Case ID 3 - Throw 20 balls all gutters expected score 0
    def test_all_gutters(self):
        game = BowlingGame()
        self.throw_many(game, 20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    # Test Case ID 4 - this tests a game with no strike or spare and 20 throws expected score 50
    def test_for_no_spares_or_strikes(self):
        game = BowlingGame()
        game.throw(0)
        game.throw(1)
        game.throw(1)
        game.throw(2)
        game.throw(2)
        game.throw(3)
        game.throw(3)
        game.throw(4)
        game.throw(4)
        game.throw(5)
        game.throw(5)
        game.throw(4)
        game.throw(4)
        game.throw(3)
        game.throw(3)
        game.throw(2)
        game.throw(2)
        game.throw(1)
        game.throw(1)
        game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 50)

    # Test Case ID 5 - incomplete game test, four frame and expected score of 41
    def test_for_incomplete_game(self):
        game = BowlingGame()
        game.throw(0)
        game.throw(10)
        game.throw(10)
        game.throw(1)
        game.throw(1)
        game.throw(2)
        game.throw(5)
        game.calculate_score()
        self.assertEqual(game.score, 41)
