import numpy as np
import unittest
from src import scoring as sc

class TestScoring(unittest.TestCase):
    def test_minutes(self):
        self.assertEqual(sc.minutes_played(65), 2)
        self.assertEqual(sc.minutes_played(57), 1)
        self.assertEqual(sc.minutes_played(0), 0)

    def test_goals_scored(self):
        self.assertEqual(sc.goals_scored(2, 'G'), 12)
        self.assertEqual(sc.goals_scored(0, 'G'), 0)
        self.assertEqual(sc.goals_scored(0, 'D'), 0)
        self.assertEqual(sc.goals_scored(1, 'D'), 6)
        self.assertEqual(sc.goals_scored(0, 'M'), 0)
        self.assertEqual(sc.goals_scored(1, 'M'), 5)
        self.assertEqual(sc.goals_scored(2, 'M'), 10)
        self.assertEqual(sc.goals_scored(0, 'F'), 0)
        self.assertEqual(sc.goals_scored(1, 'F'), 5)
        self.assertEqual(sc.goals_scored(2, 'F'), 10)
        self.assertEqual(sc.goals_scored(3, 'F'), 15)

    def test_assists(self):
        self.assertEqual(sc.assists(0), 0)
        self.assertEqual(sc.assists(1), 3)
        self.assertEqual(sc.assists(2), 6)

    def test_clean_sheet(self):
        self.assertEqual(sc.clean_sheet(0, 'G'), 0)
        self.assertEqual(sc.clean_sheet(1, 'G'), 5)
        self.assertEqual(sc.clean_sheet(0, 'D'), 0)
        self.assertEqual(sc.clean_sheet(1, 'D'), 5)
        self.assertEqual(sc.clean_sheet(0, 'M'), 0)
        self.assertEqual(sc.clean_sheet(1, 'M'), 1)
        self.assertEqual(sc.clean_sheet(0, 'F'), 0)
        self.assertEqual(sc.clean_sheet(1, 'F'), 0)
        self.assertEqual(sc.clean_sheet(0, 'D'), 0)
        self.assertEqual(sc.clean_sheet(2, 'D'), 0)
        with self.assertRaises(ValueError):
            sc.clean_sheet(3, 'u')
        with self.assertRaises(ValueError):
            sc.clean_sheet(3, '')

    def test_penalty_saves(self):
        self.assertEqual(sc.penalty_save(0), 0)
        self.assertEqual(sc.penalty_save(1), 5)
        self.assertEqual(sc.penalty_save(2), 10)

    def test_penalty_earned(self):
        self.assertEqual(sc.penalty_earned(0), 0)
        self.assertEqual(sc.penalty_earned(1), 2)
        self.assertEqual(sc.penalty_earned(3), 6)

    def test_penalty_missed(self):
        self.assertEqual(sc.penalty_missed(0), 0)
        self.assertEqual(sc.penalty_missed(1), -2)
        self.assertEqual(sc.penalty_missed(4), -8)

    def test_goal_against(self):
        self.assertEqual(sc.goal_against(0, 'D'), 0)
        self.assertEqual(sc.goal_against(0, 'G'), 0)
        self.assertEqual(sc.goal_against(0, 'M'), 0)
        self.assertEqual(sc.goal_against(0, 'F'), 0)
        self.assertEqual(sc.goal_against(1, 'D'), 0)
        self.assertEqual(sc.goal_against(1, 'G'), 0)
        self.assertEqual(sc.goal_against(1, 'M'), 0)
        self.assertEqual(sc.goal_against(1, 'F'), 0)
        self.assertEqual(sc.goal_against(2, 'D'), -1)
        self.assertEqual(sc.goal_against(2, 'G'), -1)
        self.assertEqual(sc.goal_against(2, 'M'), 0)
        self.assertEqual(sc.goal_against(2, 'F'), 0)
        self.assertEqual(sc.goal_against(3, 'D'), -1)
        self.assertEqual(sc.goal_against(3, 'G'), -1)
        self.assertEqual(sc.goal_against(3, 'M'), 0)
        self.assertEqual(sc.goal_against(3, 'F'), 0)
        self.assertEqual(sc.goal_against(4, 'D'), -2)
        self.assertEqual(sc.goal_against(4, 'G'), -2)
        self.assertEqual(sc.goal_against(5, 'D'), -2)
        self.assertEqual(sc.goal_against(6, 'D'), -3)
        with self.assertRaises(ValueError):
            sc.goal_against(2, 'U')
        with self.assertRaises(ValueError):
            sc.goal_against(3, '')

    def test_saves(self):
        self.assertEqual(sc.saves(0), 0)
        self.assertEqual(sc.saves(1), 0)
        self.assertEqual(sc.saves(3), 1)
        self.assertEqual(sc.saves(4), 1)
        self.assertEqual(sc.saves(6), 2)

    def test_yellows(self):
        self.assertEqual(sc.yellow_cards(0), 0)
        self.assertEqual(sc.yellow_cards(1), -1)
        self.assertEqual(sc.yellow_cards(2), -2)

    def test_reds(self):
        self.assertEqual(sc.red_cards(0), 0)
        self.assertEqual(sc.red_cards(1), -3)

    def test_own_goals(self):
        self.assertEqual(sc.own_goal(0), 0)
        self.assertEqual(sc.own_goal(1), -2)
        self.assertEqual(sc.own_goal(3), -6)

    def test_tackles(self):
        self.assertEqual(sc.tackles(0), 0)
        self.assertEqual(sc.tackles(1), 0)
        self.assertEqual(sc.tackles(3), 0)
        self.assertEqual(sc.tackles(4), 1)
        self.assertEqual(sc.tackles(7), 1)
        self.assertEqual(sc.tackles(8), 2)
        self.assertEqual(sc.tackles(11), 2)
        self.assertEqual(sc.tackles(12), 3)

    def test_passes(self):
        self.assertEqual(sc.passes(0), 0)
        self.assertEqual(sc.passes(20), 0)
        self.assertEqual(sc.passes(35), 1)
        self.assertEqual(sc.passes(55), 1)
        self.assertEqual(sc.passes(70), 2)
        self.assertEqual(sc.passes(75), 2)
        self.assertEqual(sc.passes(110), 3)

    def test_key_passes(self):
        self.assertEqual(sc.key_passes(0), 0)
        self.assertEqual(sc.key_passes(1), 0)
        self.assertEqual(sc.key_passes(2), 0)
        self.assertEqual(sc.key_passes(3), 1)
        self.assertEqual(sc.key_passes(4), 1)
        self.assertEqual(sc.key_passes(6), 2)
        self.assertEqual(sc.key_passes(8), 2)
        self.assertEqual(sc.key_passes(9), 3)