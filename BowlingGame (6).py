import unittest

"""
Bowling Game Program used for adding pins knocked down per throw and stores them into a list,
it also provides a means to calculate the totals and store this value inside that game
"""


class BowlingGame(object):
    def __init__(self):
        """
        object variables, stores throws and score total. Throws stores the number of pins knocked down in a throw

        :param self.throws: empty list for storing number of pins knocked down per throw
        :type self.throws: empty list
        :param self.score: variable for storing total scores
        :type self.score: integer
        """
        self.throws = []
        self.score = 0

    def throw(self, pins):
        """
        Function for adding pin value of a throw to throws list in object

        :param pins: variable for number of pins knocked down on a throw
        :type pins: integer
        :return: null
        :rtype: null
        """
        self.throws.append(pins)

    #
    def calculate_score(self):
        """
        calculates the score total of the game of the currently stored in object variable throws and
        updates the score total for that given game, updates BowlingGame().score with calculated value

        :return: null
        :rtype: null
        """
        ball = 0
        for frames in range(10):
            # new method that is called if game is incomplete and exits if all frames calculated
            if ball == len(self.throws):
                break
            elif len(self.throws) == 1:
                self.score = self.throws[ball]
                break
            elif len(self.throws) == 2:
                self.score += self.throws[ball] + self.throws[ball + 1]
                break
            elif ball > len(self.throws) or ball + 1 > len(self.throws):
                self.score += self.throws[ball]
                break
            # end of new method
            elif self.throws[ball] == 10:
                self.score += 10 + self.throws[ball + 1] + self.throws[ball + 2]
                ball += 1
            elif self.throws[ball] + self.throws[ball + 1] == 10:
                self.score += 10 + self.throws[ball + 2]
                ball += 2
            else:
                self.score += self.throws[ball] + self.throws[ball + 1]
                ball += 2

"""
==========
UNIT TESTS
==========

this is the unit tests for this program

"""


class BowlingGameTests(unittest.TestCase):
    def throw_many(self, game, number_of_times, pins):
        """
        test method for throwing multiple throws of the same value

        :param game: Is the reference to an object of BowlingGame()
        :type game: object
        :param number_of_times: Is the number of times a ball will be thrown
        :type number_of_times: int
        :param pins: Is the value that will be added for each throw
        :type pins: int
        :return: null
        :rtype: null
        """
        for _ in range(number_of_times):
            game.throw(pins)

    def test_perfect_game(self):
        """
        Test Case ID 1
        **************

        Test for perfect game score total 300
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        self.throw_many(game, 12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    def test_for_game_of_spares_version_A(self):
        """
        Test Case ID 2.a
        ****************

        this test will show that 21 balls and all [0,10] and [0,10,0] returns correct value of 100
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        for _ in range(10):
            game.throw(0)
            game.throw(10)
        game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 100)

    def test_for_game_of_spares_version_B(self):
        """
        Test Case ID 2.b
        ****************

        this will show 21 balls and 10 spares with a different high score of Test Case ID 2.a expected score is 101
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        for _ in range(9):
            game.throw(0)
            game.throw(10)
        game.throw(1)
        game.throw(9)
        game.throw(0)
        game.calculate_score()
        self.assertEqual(game.score, 101)

    def test_for_game_of_spares_version_C(self):
        """
        Test Case ID 2.c
        ****************

        this tests a game of ten spares and strike at the end similar to 2.a and 2.b, Expected score is 110
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        for _ in range(10):
            game.throw(0)
            game.throw(10)
        game.throw(10)
        game.calculate_score()
        self.assertEqual(game.score, 110)

    def test_for_game_of_spares_version_D(self):
        """
        Test Case ID 2.d
        ****************

        Test Case ID 2.d - this tests a game of all different combination of spares in one game, Expected score 144
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
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

    def test_all_gutters(self):
        """
        Test Case ID 3
        **************

        Throw 20 balls all gutters expected score 0
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        self.throw_many(game, 20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    def test_for_no_spares_or_strikes(self):
        """
        Test Case ID 4
        **************

        This tests a game with no strike or spare and 20 throws expected score 50
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
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

    def test_for_incomplete_game(self):
        """
        Test Case ID 5
        **************

        Incomplete game test, four frames and expected score of 41
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
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

    def test_for_one_strike(self):
        """
        ^, Test Case ID 5.2
        ^^^^^^^^^^^^^^^^^^^

        ^, Check to see how one value in game will calculate, expected score of 10
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        game.throw(10)
        game.calculate_score()
        self.assertEqual(game.score, 10)

    def test_for_one_spare(self):
        """
        ^, Test Case ID 5.3
        ^^^^^^^^^^^^^^^^^^^

        ^, Check to see how two values in game will calculate, expected score of 10
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        game.throw(0)
        game.throw(10)
        game.calculate_score()
        self.assertEqual(game.score, 10)

    def test_for_frame_variety(self):
        """
        Test Case ID 6
        **************

        Check to see a full game of spares, gutters, strikes and open frames expected score 95
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        game.throw(0)
        game.throw(10)
        game.throw(0)
        game.throw(0)
        game.throw(0)
        game.throw(1)
        game.throw(6)
        game.throw(0)
        game.throw(0)
        game.throw(10)
        game.throw(10)
        game.throw(0)
        game.throw(5)
        game.throw(6)
        game.throw(2)
        game.throw(0)
        game.throw(10)
        game.throw(0)
        game.throw(10)
        game.throw(10)
        game.calculate_score()
        self.assertEqual(game.score, 95)

    def test_all_ones(self):
        """
        Test Case ID 7
        **************

        Check to see if lowest score in each frame except for 0, expected score 20
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        self.throw_many(game, number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    def test_all_even_frames(self):
        """
        Test Case ID 8
        **************

        Check to see if even score values are calculated correctly expected score total 106
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        game.throw(2)
        game.throw(4)
        game.throw(2)
        game.throw(6)
        game.throw(2)
        game.throw(8)
        game.throw(8)
        game.throw(2)
        game.throw(6)
        game.throw(2)
        game.throw(4)
        game.throw(2)
        game.throw(2)
        game.throw(2)
        game.throw(4)
        game.throw(4)
        game.throw(6)
        game.throw(4)
        game.throw(4)
        game.throw(6)
        game.throw(8)
        game.calculate_score()
        self.assertEqual(game.score, 106)

    def test_for_odd_totals(self):
        """
        Test Case ID 9
        **************

        Test game with all frames totaling to odd numbers and expected score total 39
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        game.throw(0)
        game.throw(1)
        game.throw(1)
        game.throw(5)
        game.throw(1)
        game.throw(1)
        game.throw(4)
        game.throw(4)
        game.throw(3)
        game.throw(1)
        game.throw(3)
        game.throw(1)
        game.throw(7)
        game.throw(1)
        game.throw(1)
        game.throw(1)
        game.throw(1)
        game.throw(1)
        game.throw(1)
        game.throw(1)
        game.calculate_score()
        self.assertEqual(game.score, 39)

    def test_different_throws(self):
        """
        Test Case ID 10
        ***************

        Tests game of different values expected total 15
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
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
        """
        Test Case ID 11
        ***************

        Test for game with a spare in it, expected score total 24
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
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
        """
        Test Case ID 12
        ***************

        Test for game with a strike in it, expected total 22
        :return: asserts whether the game score matches expected value
        :rtype: assertEqual
        """
        game = BowlingGame()
        game.throw(10)
        game.throw(4)
        game.throw(2)
        self.throw_many(game, 17, 0)
        game.calculate_score()
        self.assertEqual(game.score, 22)
