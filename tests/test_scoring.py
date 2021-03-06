import numpy as np
import unittest

import sys

sys.path.append("../")

from src import scoring_functions as sc

GOALIE1 =   [90, 5, 3, 0, 2, 2, 2, 4, 7, 2, 1, 2, 0, 0, 0, 0, 0, 0, 5, 4, 3, 0, 1, 0, 0]
GOALIE2 =   [65, 2, 1, 1, 1, 1, 1, 2, 3, 1, 0, 1, 3, 10, 1, 1, 1, 1, 3, 1, 0, 1, 0, 1, 1]
GOALIE3 =   [57, 2, 1, 1, 1, 0, 0, 1, 1, 0, 1, 3, 4, 35, 3, 3, 3, 4, 4, 0, 6, 2, 2, 4, 4]
GOALIE4 =   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 40, 5, 5, 2, 5, 1, 5, 7, 3, 3, 5, 5]
DEFENDER1 = [90, 3, 3, 0, 2, 2, 2, 9, 2, 2, 1, 2, 8, 70, 6, 6, 4, 8, 0, 8, 12, 0, 4, 8, 8]
DEFENDER2 = [65, 1, 1, 1, 1, 1, 1, 7, 5, 1, 0, 3, 10, 75, 7, 7, 5, 9, 8, 11, 13, 0, 5, 11, 11]
DEFENDER3 = [57, 1, 1, 1, 1, 0, 0, 5, 6, 0, 1, 1, 12, 100, 9, 9, 6, 12, 9, 12, 11, 0, 0, 12, 12]
DEFENDER4 = [0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 15, 105, 10, 10, 7, 15, 12, 0, 18, 0, 0, 14, 14]
MIDFIELD1 = [90, 5, 3, 0, 2, 2, 2, 2, 2, 2, 1, 2, 16, 110, 12, 12, 8, 16, 13, 0, 19, 0, 0, 16, 16]
MIDFIELD2 = [65, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 17, 140, 15, 15, 0, 17, 7, 0, 24, 0, 0, 17, 17]
MIDFIELD3 = [57, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 20, 0, 16, 16, 0, 20, 6, 0, 25, 0, 0, 20, 20]
MIDFIELD4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 17, 0, 21, 0, 0, 0, 0, 0, 21, 21]
FORWARD1 =  [90, 3, 3, 1, 2, 2, 2, 3, 2, 2, 1, 0, 24, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 24, 24]
FORWARD2 =  [57, 1, 1, 1, 1, 1, 1, 5, 1, 1, 0, 0, 27, 145, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0]
FORWARD3 =  [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 28, 175, 0, 21, 0, 0, 0, 0, 0, 4, 0, 0, 0]

class TestScoring(unittest.TestCase):
    def setUp(self):
        self.g1 = sc.GoalieOrDefender(*GOALIE1)
        self.g2 = sc.GoalieOrDefender(*GOALIE2)
        self.g3 = sc.GoalieOrDefender(*GOALIE3)
        self.g4 = sc.GoalieOrDefender(*GOALIE4)
        self.d1 = sc.GoalieOrDefender(*DEFENDER1)
        self.d2 = sc.GoalieOrDefender(*DEFENDER2)
        self.d3 = sc.GoalieOrDefender(*DEFENDER3)
        self.d4 = sc.GoalieOrDefender(*DEFENDER4)
        self.m1 = sc.Midfielder(*MIDFIELD1)
        self.m2 = sc.Midfielder(*MIDFIELD2)
        self.m3 = sc.Midfielder(*MIDFIELD3)
        self.m4 = sc.Midfielder(*MIDFIELD4)
        self.f1 = sc.Forward(*FORWARD1)
        self.f2 = sc.Forward(*FORWARD2)
        self.f3 = sc.Forward(*FORWARD3)
        
    def test_minutes(self):
        self.assertEqual(self.g1.minutes_played(), 2)
        self.assertNotEqual(self.g1.minutes_played(), 1)
        self.assertEqual(self.g2.minutes_played(), 2)
        self.assertNotEqual(self.g2.minutes_played(), 1)
        self.assertEqual(self.g3.minutes_played(), 1)
        self.assertNotEqual(self.g3.minutes_played(), 2)
        self.assertNotEqual(self.g3.minutes_played(), 0)
        self.assertEqual(self.g4.minutes_played(), 0)
        self.assertNotEqual(self.g4.minutes_played(), 1)
        self.assertNotEqual(self.g4.minutes_played(), 2)

    def test_goals_scored(self):
        self.assertEqual(self.g1.goals_scored(), 30)
        self.assertNotEqual(self.g1.goals_scored(), 24)
        self.assertEqual(self.g2.goals_scored(), 12)
        self.assertNotEqual(self.g2.goals_scored(), 0)
        self.assertEqual(self.g4.goals_scored(), 0)
        self.assertNotEqual(self.g4.goals_scored(), 6)
        self.assertEqual(self.d1.goals_scored(), 18)
        self.assertNotEqual(self.d1.goals_scored(), 12)
        self.assertEqual(self.d2.goals_scored(), 6)
        self.assertNotEqual(self.d2.goals_scored(), 0)
        self.assertEqual(self.m1.goals_scored(), 25)
        self.assertNotEqual(self.m1.goals_scored(), 5)
        self.assertEqual(self.m2.goals_scored(), 10)
        self.assertNotEqual(self.m2.goals_scored(), 5)
        self.assertEqual(self.m4.goals_scored(), 0)
        self.assertNotEqual(self.m4.goals_scored(), 5)
        self.assertEqual(self.f1.goals_scored(), 15)
        self.assertNotEqual(self.f1.goals_scored(),0)
        self.assertEqual(self.f2.goals_scored(), 5)
        self.assertNotEqual(self.f2.goals_scored(), 0)
        self.assertEqual(self.f3.goals_scored(), 0)
        self.assertNotEqual(self.f3.goals_scored(), 5)

    def test_assists(self):
        self.assertEqual(self.g1.assists(), 9)
        self.assertNotEqual(self.g1.assists(), 6)
        self.assertEqual(self.g2.assists(), 3)
        self.assertNotEqual(self.g2.assists(), 0)
        self.assertEqual(self.g4.assists(), 0)
        self.assertNotEqual(self.g4.assists(), 3)
        self.assertEqual(self.d1.assists(), 9)
        self.assertNotEqual(self.d1.assists(), 6)
        self.assertEqual(self.d2.assists(), 3)
        self.assertNotEqual(self.d2.assists(), 0)
        self.assertEqual(self.d4.assists(), 0)
        self.assertNotEqual(self.d4.assists(), 3)
        self.assertEqual(self.m1.assists(), 9)
        self.assertNotEqual(self.m1.assists(), 6)
        self.assertEqual(self.m2.assists(), 3)
        self.assertNotEqual(self.m2.assists(), 0)
        self.assertEqual(self.m4.assists(), 0)
        self.assertNotEqual(self.m4.assists(), 3)
        self.assertEqual(self.f1.assists(), 9)
        self.assertNotEqual(self.f1.assists(), 6)
        self.assertEqual(self.f2.assists(), 3)
        self.assertNotEqual(self.f2.assists(), 0)
        self.assertEqual(self.f3.assists(), 0)
        self.assertNotEqual(self.f3.assists(), 3)

    def test_clean_sheet(self):
        self.assertEqual(self.g1.clean_sheet(), 0)
        self.assertNotEqual(self.g1.clean_sheet(), 5)
        self.assertEqual(self.g2.clean_sheet(), 5)
        self.assertNotEqual(self.g2.clean_sheet(), 0)
        self.assertEqual(self.g3.clean_sheet(), 0)
        self.assertNotEqual(self.g3.clean_sheet(), 5)
        self.assertEqual(self.g4.clean_sheet(), 0)
        self.assertNotEqual(self.g4.clean_sheet(), 5)        
        self.assertEqual(self.d1.clean_sheet(), 0)
        self.assertNotEqual(self.d1.clean_sheet(), 5)
        self.assertEqual(self.d2.clean_sheet(), 5)
        self.assertNotEqual(self.d2.clean_sheet(), 0)
        self.assertEqual(self.d3.clean_sheet(), 0)
        self.assertNotEqual(self.d3.clean_sheet(), 5)
        self.assertEqual(self.d4.clean_sheet(), 0)
        self.assertNotEqual(self.d4.clean_sheet(), 5)        
        self.assertEqual(self.m1.clean_sheet(), 0)
        self.assertNotEqual(self.m1.clean_sheet(), 1)
        self.assertEqual(self.m2.clean_sheet(), 1)
        self.assertNotEqual(self.m2.clean_sheet(), 0)
        self.assertEqual(self.m3.clean_sheet(), 0)
        self.assertNotEqual(self.m3.clean_sheet(), 1)
        self.assertEqual(self.m4.clean_sheet(), 0)
        self.assertNotEqual(self.m4.clean_sheet(), 1)        
        self.assertEqual(self.f1.clean_sheet(), 0)
        self.assertNotEqual(self.f1.clean_sheet(), 1)
        self.assertEqual(self.f2.clean_sheet(), 0)
        self.assertNotEqual(self.f2.clean_sheet(), 1)
        self.assertEqual(self.f3.clean_sheet(), 0)
        self.assertNotEqual(self.f3.clean_sheet(), 1)        

    def test_penalty_saves(self):
        self.assertEqual(self.g1.penalty_save(), 10)
        self.assertNotEqual(self.g1.penalty_save(), 0)
        self.assertEqual(self.g2.penalty_save(), 5)
        self.assertNotEqual(self.g2.penalty_save(), 0)
        self.assertEqual(self.g4.penalty_save(), 0)
        self.assertNotEqual(self.g4.penalty_save(), 5)
        self.assertEqual(self.d1.penalty_save(), 10)
        self.assertNotEqual(self.d1.penalty_save(), 0)
        self.assertEqual(self.d2.penalty_save(), 5)
        self.assertNotEqual(self.d2.penalty_save(), 0)
        self.assertEqual(self.d4.penalty_save(), 0)
        self.assertNotEqual(self.d4.penalty_save(), 5)
        self.assertEqual(self.m1.penalty_save(), 10)
        self.assertNotEqual(self.m1.penalty_save(), 0)
        self.assertEqual(self.m2.penalty_save(), 5)
        self.assertNotEqual(self.m2.penalty_save(), 0)
        self.assertEqual(self.m4.penalty_save(), 0)
        self.assertNotEqual(self.m4.penalty_save(), 5)
        self.assertEqual(self.f1.penalty_save(), 10)
        self.assertNotEqual(self.f1.penalty_save(), 0)
        self.assertEqual(self.f2.penalty_save(), 5)
        self.assertNotEqual(self.f2.penalty_save(), 0)
        self.assertEqual(self.f3.penalty_save(), 0)
        self.assertNotEqual(self.f3.penalty_save(), 5)

    def test_penalty_earned(self):
        self.assertEqual(self.m1.penalty_earned(), 4)
        self.assertNotEqual(self.m1.penalty_earned(), 0)
        self.assertEqual(self.m2.penalty_earned(), 2)
        self.assertNotEqual(self.m2.penalty_earned(), 0)
        self.assertEqual(self.m3.penalty_earned(), 0)
        self.assertNotEqual(self.m3.penalty_earned(), 2)
        self.assertEqual(self.f1.penalty_earned(), 4)
        self.assertNotEqual(self.f1.penalty_earned(), 0)
        self.assertEqual(self.f2.penalty_earned(), 2)
        self.assertNotEqual(self.f2.penalty_earned(), 0)
        self.assertEqual(self.f3.penalty_earned(), 0)
        self.assertNotEqual(self.f3.penalty_earned(), 2)

    def test_penalty_missed(self):
        self.assertEqual(self.m1.penalty_missed(), -4)
        self.assertNotEqual(self.m1.penalty_missed(), 0)
        self.assertEqual(self.m2.penalty_missed(), -2)
        self.assertNotEqual(self.m2.penalty_missed(), 0)
        self.assertEqual(self.m3.penalty_missed(), 0)
        self.assertNotEqual(self.m3.penalty_missed(), -2)
        self.assertEqual(self.f1.penalty_missed(), -4)
        self.assertNotEqual(self.f1.penalty_missed(), 0)
        self.assertEqual(self.f2.penalty_missed(), -2)
        self.assertNotEqual(self.f2.penalty_missed(), 0)
        self.assertEqual(self.f3.penalty_missed(), 0)
        self.assertNotEqual(self.f3.penalty_missed(), -2)

    def test_goal_against(self):
        self.assertEqual(self.g1.goal_against(), -2)
        self.assertNotEqual(self.g1.goal_against(), 0)
        self.assertEqual(self.g2.goal_against(), -1)
        self.assertNotEqual(self.g2.goal_against(), 0)
        self.assertEqual(self.g3.goal_against(), 0)
        self.assertNotEqual(self.g3.goal_against(), -1)
        self.assertEqual(self.g4.goal_against(), 0)
        self.assertNotEqual(self.g4.goal_against(), -1)

        self.assertEqual(self.d1.goal_against(), -4)
        self.assertNotEqual(self.d1.goal_against(), 0)
        self.assertEqual(self.d2.goal_against(), -3)
        self.assertNotEqual(self.d2.goal_against(), 0)
        self.assertEqual(self.d3.goal_against(), -2)
        self.assertNotEqual(self.d3.goal_against(), -1)
        self.assertEqual(self.d4.goal_against(), -1)
        self.assertNotEqual(self.d4.goal_against(), 0)
        self.assertEqual(self.m3.goal_against(), 0)
        self.assertNotEqual(self.m3.goal_against(), -1)
        self.assertEqual(self.m4.goal_against(), 0)
        self.assertNotEqual(self.m4.goal_against(), -1)
        self.assertEqual(self.f2.goal_against(), 0)
        self.assertNotEqual(self.f2.goal_against(), -1)
        self.assertEqual(self.f3.goal_against(), 0)
        self.assertNotEqual(self.f3.goal_against(), -1)

    def test_saves(self):
        self.assertEqual(self.g1.saves(), 2)
        self.assertNotEqual(self.g1.saves(), 0)
        self.assertEqual(self.g2.saves(), 1)
        self.assertNotEqual(self.g2.saves(), 0)
        self.assertEqual(self.g3.saves(), 0)
        self.assertNotEqual(self.g3.saves(), 1)
        self.assertEqual(self.g4.saves(), 0)
        self.assertNotEqual(self.g4.saves(), 2)
        self.assertEqual(self.d1.saves(), 0)
        self.assertNotEqual(self.d1.saves(), 1)
        self.assertEqual(self.d2.saves(), 1)
        self.assertNotEqual(self.d2.saves(), 0)
        self.assertEqual(self.d3.saves(), 2)
        self.assertNotEqual(self.d3.saves(), 1)
        self.assertEqual(self.d4.saves(), 1)
        self.assertNotEqual(self.d4.saves(), 2)

    def test_yellows(self):
        self.assertEqual(self.g1.yellow_cards(), -2)
        self.assertNotEqual(self.g1.yellow_cards(), 0)
        self.assertEqual(self.g2.yellow_cards(), -1)
        self.assertNotEqual(self.g2.yellow_cards(), 0)
        self.assertEqual(self.g3.yellow_cards(), 0)
        self.assertNotEqual(self.g3.yellow_cards(), -1)
        self.assertEqual(self.g4.yellow_cards(), 0)
        self.assertNotEqual(self.g4.yellow_cards(), -1)

    def test_reds(self):
        self.assertEqual(self.g1.red_cards(), -3)
        self.assertNotEqual(self.g1.red_cards(), 0)
        self.assertEqual(self.g2.red_cards(), 0)
        self.assertNotEqual(self.g2.red_cards(), -3)
        self.assertEqual(self.g3.red_cards(), -3)
        self.assertNotEqual(self.g3.red_cards(), 0)
        self.assertEqual(self.g4.red_cards(), 0)
        self.assertNotEqual(self.g4.red_cards(), -3)

    def test_own_goals(self):
        self.assertEqual(self.g1.own_goal(), -4)
        self.assertNotEqual(self.g1.own_goal(), 0)
        self.assertEqual(self.g2.own_goal(), -2)
        self.assertNotEqual(self.g2.own_goal(), 0)
        self.assertEqual(self.g3.own_goal(), -6)
        self.assertNotEqual(self.g3.own_goal(), 0)
        self.assertEqual(self.g4.own_goal(), 0)
        self.assertNotEqual(self.g4.own_goal(), -2)

    def test_tackles(self):
        self.assertEqual(self.g1.tackles(), 0)
        self.assertNotEqual(self.g1.tackles(), 1)
        self.assertEqual(self.g2.tackles(), 0)
        self.assertNotEqual(self.g2.tackles(), 1)
        self.assertEqual(self.g3.tackles(), 1)
        self.assertNotEqual(self.g3.tackles(), 0)
        self.assertEqual(self.g4.tackles(), 1)
        self.assertNotEqual(self.g4.tackles(), 0)
        self.assertEqual(self.d1.tackles(), 2)
        self.assertNotEqual(self.d1.tackles(), 1)
        self.assertEqual(self.d2.tackles(), 2)
        self.assertNotEqual(self.d2.tackles(), 1)
        self.assertEqual(self.d3.tackles(), 3)
        self.assertNotEqual(self.d3.tackles(), 2)
        self.assertEqual(self.d4.tackles(), 3)
        self.assertNotEqual(self.d4.tackles(), 2)
        self.assertEqual(self.m1.tackles(), 4)
        self.assertNotEqual(self.m1.tackles(), 0)
        self.assertEqual(self.m2.tackles(), 4)
        self.assertNotEqual(self.m2.tackles(), 1)
        self.assertEqual(self.m3.tackles(), 5)
        self.assertNotEqual(self.m3.tackles(), 2)
        self.assertEqual(self.m4.tackles(), 5)
        self.assertNotEqual(self.m4.tackles(), 2)
        self.assertEqual(self.f1.tackles(), 6)
        self.assertNotEqual(self.f1.tackles(), 0)
        self.assertEqual(self.f2.tackles(), 6)
        self.assertNotEqual(self.f2.tackles(), 1)
        self.assertEqual(self.f3.tackles(), 7)
        self.assertNotEqual(self.f3.tackles(), 5)

    def test_passes(self):
        self.assertEqual(self.g1.passes(), 0)
        self.assertNotEqual(self.g1.passes(), 1)
        self.assertEqual(self.g2.passes(), 0)
        self.assertNotEqual(self.g2.passes(), 1)
        self.assertEqual(self.g3.passes(), 1)
        self.assertNotEqual(self.g3.passes(), 0)
        self.assertEqual(self.g4.passes(), 1)
        self.assertNotEqual(self.g4.passes(), 0)
        self.assertEqual(self.d1.passes(), 2)
        self.assertNotEqual(self.d1.passes(), 1)
        self.assertEqual(self.d2.passes(), 2)
        self.assertNotEqual(self.d2.passes(), 1)
        self.assertEqual(self.d3.passes(), 2)
        self.assertNotEqual(self.d3.passes(), 1)
        self.assertEqual(self.d4.passes(), 3)
        self.assertNotEqual(self.d4.passes(), 2)
        self.assertEqual(self.m1.passes(), 3)
        self.assertNotEqual(self.m1.passes(), 0)
        self.assertEqual(self.m2.passes(), 4)
        self.assertNotEqual(self.m2.passes(), 1)
        self.assertEqual(self.m3.passes(), 0)
        self.assertNotEqual(self.m3.passes(), 2)
        self.assertEqual(self.m4.passes(), 0)
        self.assertNotEqual(self.m4.passes(), 2)
        self.assertEqual(self.f1.passes(), 0)
        self.assertNotEqual(self.f1.passes(), 1)
        self.assertEqual(self.f2.passes(), 4)
        self.assertNotEqual(self.f2.passes(), 1)
        self.assertEqual(self.f3.passes(), 5)
        self.assertNotEqual(self.f3.passes(), 4)


    def test_key_passes(self):
        self.assertEqual(self.g1.key_passes(), 0)
        self.assertNotEqual(self.g1.key_passes(), 1)
        self.assertEqual(self.g2.key_passes(), 0)
        self.assertNotEqual(self.g2.key_passes(), 1)
        self.assertEqual(self.g3.key_passes(), 1)
        self.assertNotEqual(self.g3.key_passes(), 0)
        self.assertEqual(self.g4.key_passes(), 1)
        self.assertNotEqual(self.g4.key_passes(), 0)
        self.assertEqual(self.d1.key_passes(), 2)
        self.assertNotEqual(self.d1.key_passes(), 1)
        self.assertEqual(self.d2.key_passes(), 2)
        self.assertNotEqual(self.d2.key_passes(), 1)
        self.assertEqual(self.d3.key_passes(), 3)
        self.assertNotEqual(self.d3.key_passes(), 1)
        self.assertEqual(self.d4.key_passes(), 3)
        self.assertNotEqual(self.d4.key_passes(), 2)
        self.assertEqual(self.m1.key_passes(), 4)
        self.assertNotEqual(self.m1.key_passes(), 0)
        self.assertEqual(self.m2.key_passes(), 5)
        self.assertNotEqual(self.m2.key_passes(), 1)
        self.assertEqual(self.m3.key_passes(), 5)
        self.assertNotEqual(self.m3.key_passes(), 2)
        self.assertEqual(self.m4.key_passes(), 0)
        self.assertNotEqual(self.m4.key_passes(), 2)
        self.assertEqual(self.f1.key_passes(), 0)
        self.assertNotEqual(self.f1.key_passes(), 1)
        self.assertEqual(self.f2.key_passes(), 0)
        self.assertNotEqual(self.f2.key_passes(), 1)
        self.assertEqual(self.f3.key_passes(), 0)
        self.assertNotEqual(self.f3.key_passes(), 4)

    def test_crosses(self):
        self.assertEqual(self.g1.crosses(), 0)
        self.assertNotEqual(self.g1.crosses(), 1)
        self.assertEqual(self.g2.crosses(), 0)
        self.assertNotEqual(self.g2.crosses(), 1)
        self.assertEqual(self.g3.crosses(), 1)
        self.assertNotEqual(self.g3.crosses(), 2)
        self.assertEqual(self.g4.crosses(), 1)
        self.assertNotEqual(self.g4.crosses(), 2)
        self.assertEqual(self.d1.crosses(), 2)
        self.assertNotEqual(self.d1.crosses(), 1)
        self.assertEqual(self.d2.crosses(), 2)
        self.assertNotEqual(self.d2.crosses(), 1)
        self.assertEqual(self.d3.crosses(), 3)
        self.assertNotEqual(self.d3.crosses(), 2)
        self.assertEqual(self.d4.crosses(), 3)
        self.assertNotEqual(self.d4.crosses(), 2)
        self.assertEqual(self.m1.crosses(), 4)
        self.assertNotEqual(self.m1.crosses(), 1)
        self.assertEqual(self.m2.crosses(), 5)
        self.assertNotEqual(self.m2.crosses(), 1)
        self.assertEqual(self.m3.crosses(), 5)
        self.assertNotEqual(self.m3.crosses(), 2)
        self.assertEqual(self.m4.crosses(), 5)
        self.assertNotEqual(self.m4.crosses(), 2)
        self.assertEqual(self.f1.crosses(), 6)
        self.assertNotEqual(self.f1.crosses(), 1)
        self.assertEqual(self.f2.crosses(), 6)
        self.assertNotEqual(self.f2.crosses(), 1)
        self.assertEqual(self.f3.crosses(), 7)
        self.assertNotEqual(self.f3.crosses(), 2)

    def test_big_chance(self):
        self.assertEqual(self.g1.big_chance(), 0)
        self.assertNotEqual(self.g1.big_chance(), 1)
        self.assertEqual(self.g2.big_chance(), 1)
        self.assertNotEqual(self.g2.big_chance(), 2)
        self.assertEqual(self.g3.big_chance(), 3)
        self.assertNotEqual(self.g3.big_chance(), 1)
        self.assertEqual(self.g4.big_chance(), 2)
        self.assertNotEqual(self.g4.big_chance(), 1)
        self.assertEqual(self.d1.big_chance(), 4)
        self.assertNotEqual(self.d1.big_chance(), 1)
        self.assertEqual(self.d2.big_chance(), 5)
        self.assertNotEqual(self.d2.big_chance(), 2)
        self.assertEqual(self.d3.big_chance(), 6)
        self.assertNotEqual(self.d3.big_chance(), 1)
        self.assertEqual(self.d4.big_chance(), 7)
        self.assertNotEqual(self.d4.big_chance(), 1)
        self.assertEqual(self.m1.big_chance(), 8)
        self.assertNotEqual(self.m1.big_chance(), 1)

    def test_clearances(self):
        self.assertEqual(self.g1.clearances(), 0)
        self.assertNotEqual(self.g1.clearances(), 1)
        self.assertEqual(self.g2.clearances(), 0)
        self.assertNotEqual(self.g2.clearances(), 1)
        self.assertEqual(self.g3.clearances(), 1)
        self.assertNotEqual(self.g3.clearances(), 0)
        self.assertEqual(self.g4.clearances(), 1)
        self.assertNotEqual(self.g4.clearances(), 0)
        self.assertEqual(self.d1.clearances(), 2)
        self.assertNotEqual(self.d1.clearances(), 1)
        self.assertEqual(self.d2.clearances(), 2)
        self.assertNotEqual(self.d2.clearances(), 1)
        self.assertEqual(self.d3.clearances(), 3)
        self.assertNotEqual(self.d3.clearances(), 2)
        self.assertEqual(self.d4.clearances(), 3)
        self.assertNotEqual(self.d4.clearances(), 2)
        self.assertEqual(self.m1.clearances(), 4)
        self.assertNotEqual(self.m1.clearances(), 0)
        self.assertEqual(self.m2.clearances(), 4)
        self.assertNotEqual(self.m2.clearances(), 1)
        self.assertEqual(self.m3.clearances(), 5)
        self.assertNotEqual(self.m3.clearances(), 2)
        self.assertEqual(self.m4.clearances(), 5)
        self.assertNotEqual(self.m4.clearances(), 2)
        self.assertEqual(self.f1.clearances(), 0)
        self.assertNotEqual(self.f1.clearances(), 1)
        self.assertEqual(self.f2.clearances(), 0)
        self.assertNotEqual(self.f2.clearances(), 2)
        self.assertEqual(self.f3.clearances(), 0)
        self.assertNotEqual(self.f3.clearances(), 5)

    def test_blocks(self):
        self.assertEqual(self.g1.blocks(), 2)
        self.assertNotEqual(self.g1.blocks(), 3)
        self.assertEqual(self.g2.blocks(), 1)
        self.assertNotEqual(self.g2.blocks(), 2)
        self.assertEqual(self.g3.blocks(), 2)
        self.assertNotEqual(self.g3.blocks(), 0)
        self.assertEqual(self.g4.blocks(), 0)
        self.assertNotEqual(self.g4.blocks(), 1)
        self.assertEqual(self.d1.blocks(), 0)
        self.assertNotEqual(self.d1.blocks(), 1)
        self.assertEqual(self.d2.blocks(), 4)
        self.assertNotEqual(self.d2.blocks(), 1)
        self.assertEqual(self.d3.blocks(), 4)
        self.assertNotEqual(self.d3.blocks(), 2)
        self.assertEqual(self.d4.blocks(), 6)
        self.assertNotEqual(self.d4.blocks(), 2)
        self.assertEqual(self.m1.blocks(), 6)
        self.assertNotEqual(self.m1.blocks(), 0)
        self.assertEqual(self.m2.blocks(), 3)
        self.assertNotEqual(self.m2.blocks(), 1)
        self.assertEqual(self.m3.blocks(), 3)
        self.assertNotEqual(self.m3.blocks(), 2)
        self.assertEqual(self.m4.blocks(), 0)
        self.assertNotEqual(self.m4.blocks(), 2)
        self.assertEqual(self.f1.blocks(), 0)
        self.assertNotEqual(self.f1.blocks(), 3)
        self.assertEqual(self.f2.blocks(), 0)
        self.assertNotEqual(self.f2.blocks(), 4)
        self.assertEqual(self.f3.blocks(), 0)
        self.assertNotEqual(self.f3.blocks(), 5)

    def test_interceptions(self):
        self.assertEqual(self.g1.interceptions(), 1)
        self.assertNotEqual(self.g1.interceptions(), 0)
        self.assertEqual(self.g2.interceptions(), 0)
        self.assertNotEqual(self.g2.interceptions(), 1)
        self.assertEqual(self.g3.interceptions(), 0)
        self.assertNotEqual(self.g3.interceptions(), 1)
        self.assertEqual(self.g4.interceptions(), 1)
        self.assertNotEqual(self.g4.interceptions(), 0)
        self.assertEqual(self.d1.interceptions(), 2)
        self.assertNotEqual(self.d1.interceptions(), 1)
        self.assertEqual(self.d2.interceptions(), 2)
        self.assertNotEqual(self.d2.interceptions(), 1)
        self.assertEqual(self.d3.interceptions(), 3)
        self.assertNotEqual(self.d3.interceptions(), 2)
        self.assertEqual(self.d4.interceptions(), 0)
        self.assertNotEqual(self.d4.interceptions(), 2)
        self.assertEqual(self.m1.interceptions(), 0)
        self.assertNotEqual(self.m1.interceptions(), 1)
        self.assertEqual(self.m2.interceptions(), 0)
        self.assertNotEqual(self.m2.interceptions(), 1)
        self.assertEqual(self.m3.interceptions(), 0)
        self.assertNotEqual(self.m3.interceptions(), 2)
        self.assertEqual(self.m4.interceptions(), 0)
        self.assertNotEqual(self.m4.interceptions(), 3)
        self.assertEqual(self.f1.interceptions(), 0)
        self.assertNotEqual(self.f1.interceptions(), 4)
        self.assertEqual(self.f2.interceptions(), 0)
        self.assertNotEqual(self.f2.interceptions(), 5)
        self.assertEqual(self.f3.interceptions(), 0)
        self.assertNotEqual(self.f3.interceptions(), 6)

    def test_recovered_balls(self):
        self.assertEqual(self.g1.recovered_balls(), 0)
        self.assertNotEqual(self.g1.recovered_balls(), 1)
        self.assertEqual(self.g2.recovered_balls(), 0)
        self.assertNotEqual(self.g2.recovered_balls(), 2)
        self.assertEqual(self.g3.recovered_balls(), 1)
        self.assertNotEqual(self.g3.recovered_balls(), 2)
        self.assertEqual(self.g4.recovered_balls(), 1)
        self.assertNotEqual(self.g4.recovered_balls(), 0)
        self.assertEqual(self.d1.recovered_balls(), 2)
        self.assertNotEqual(self.d1.recovered_balls(), 1)
        self.assertEqual(self.d2.recovered_balls(), 2)
        self.assertNotEqual(self.d2.recovered_balls(), 1)
        self.assertEqual(self.d3.recovered_balls(), 1)
        self.assertNotEqual(self.d3.recovered_balls(), 2)
        self.assertEqual(self.d4.recovered_balls(), 3)
        self.assertNotEqual(self.d4.recovered_balls(), 2)
        self.assertEqual(self.m1.recovered_balls(), 3)
        self.assertNotEqual(self.m1.recovered_balls(), 1)
        self.assertEqual(self.m2.recovered_balls(), 4)
        self.assertNotEqual(self.m2.recovered_balls(), 1)
        self.assertEqual(self.m3.recovered_balls(), 4)
        self.assertNotEqual(self.m3.recovered_balls(), 2)
        self.assertEqual(self.m4.recovered_balls(), 0)
        self.assertNotEqual(self.m4.recovered_balls(), 3)
        self.assertEqual(self.f1.recovered_balls(), 0)
        self.assertNotEqual(self.f1.recovered_balls(), 4)
        self.assertEqual(self.f2.recovered_balls(), 0)
        self.assertNotEqual(self.f2.recovered_balls(), 5)
        self.assertEqual(self.f3.recovered_balls(), 0)
        self.assertNotEqual(self.f3.recovered_balls(), 6)

    def test_error_leading_to_goal(self):
        self.assertEqual(self.g1.error_leading_to_goal(), 0)
        self.assertNotEqual(self.g1.error_leading_to_goal(), -1)
        self.assertEqual(self.g2.error_leading_to_goal(), -1)
        self.assertNotEqual(self.g2.error_leading_to_goal(), 1)
        self.assertEqual(self.g3.error_leading_to_goal(), -2)
        self.assertNotEqual(self.g3.error_leading_to_goal(), -1)
        self.assertEqual(self.g4.error_leading_to_goal(), -3)
        self.assertNotEqual(self.g4.error_leading_to_goal(), -1)
        self.assertEqual(self.m1.error_leading_to_goal(), 0)
        self.assertNotEqual(self.m1.error_leading_to_goal(), -2)
        self.assertEqual(self.m2.error_leading_to_goal(), 0)
        self.assertNotEqual(self.m2.error_leading_to_goal(), 2)

    def test_own_goal_assist(self):
        self.assertEqual(self.g1.own_goal_assist(), 1)
        self.assertNotEqual(self.g1.own_goal_assist(), 0)
        self.assertEqual(self.g2.own_goal_assist(), 0)
        self.assertNotEqual(self.g2.own_goal_assist(), 1)
        self.assertEqual(self.g3.own_goal_assist(), 2)
        self.assertNotEqual(self.g3.own_goal_assist(), 1)
        self.assertEqual(self.g4.own_goal_assist(), 3)
        self.assertNotEqual(self.g4.own_goal_assist(), 2)
        self.assertEqual(self.d1.own_goal_assist(), 4)
        self.assertNotEqual(self.d1.own_goal_assist(), 2)
        self.assertEqual(self.d2.own_goal_assist(), 5)
        self.assertNotEqual(self.d2.own_goal_assist(), 3)
        self.assertEqual(self.d3.own_goal_assist(), 0)
        self.assertNotEqual(self.d3.own_goal_assist(), 4)
        self.assertEqual(self.d4.own_goal_assist(), 0)
        self.assertNotEqual(self.d4.own_goal_assist(), 2)

    def test_shots(self):
        self.assertEqual(self.g1.shots(), 0)
        self.assertNotEqual(self.g1.shots(), 1)
        self.assertEqual(self.g2.shots(), 0)
        self.assertNotEqual(self.g2.shots(), 1)
        self.assertEqual(self.g3.shots(), 1)
        self.assertNotEqual(self.g3.shots(), 2)
        self.assertEqual(self.g4.shots(), 1)
        self.assertNotEqual(self.g4.shots(), 2)
        self.assertEqual(self.d1.shots(), 2)
        self.assertNotEqual(self.d1.shots(), 1)
        self.assertEqual(self.d2.shots(), 2)
        self.assertNotEqual(self.d2.shots(), 1)
        self.assertEqual(self.d3.shots(), 3)
        self.assertNotEqual(self.d3.shots(), 2)
        self.assertEqual(self.d4.shots(), 3)
        self.assertNotEqual(self.d4.shots(), 2)
        self.assertEqual(self.m1.shots(), 4)
        self.assertNotEqual(self.m1.shots(), 1)
        self.assertEqual(self.m2.shots(), 4)
        self.assertNotEqual(self.m2.shots(), 1)
        self.assertEqual(self.m3.shots(), 5)
        self.assertNotEqual(self.m3.shots(), 2)
        self.assertEqual(self.m4.shots(), 5)
        self.assertNotEqual(self.m4.shots(), 3)
        self.assertEqual(self.f1.shots(), 6)
        self.assertNotEqual(self.f1.shots(), 4)
        self.assertEqual(self.f2.shots(), 0)
        self.assertNotEqual(self.f2.shots(), 5)
        self.assertEqual(self.f3.shots(), 0)
        self.assertNotEqual(self.f3.shots(), 6)

    def test_was_fouled(self):
        self.assertEqual(self.g1.was_fouled(), 0)
        self.assertNotEqual(self.g1.was_fouled(), 1)
        self.assertEqual(self.g2.was_fouled(), 0)
        self.assertNotEqual(self.g2.was_fouled(), 1)
        self.assertEqual(self.g3.was_fouled(), 1)
        self.assertNotEqual(self.g3.was_fouled(), 2)
        self.assertEqual(self.g4.was_fouled(), 1)
        self.assertNotEqual(self.g4.was_fouled(), 0)
        self.assertEqual(self.d1.was_fouled(), 2)
        self.assertNotEqual(self.d1.was_fouled(), 1)
        self.assertEqual(self.d2.was_fouled(), 2)
        self.assertNotEqual(self.d2.was_fouled(), 1)
        self.assertEqual(self.d3.was_fouled(), 3)
        self.assertNotEqual(self.d3.was_fouled(), 2)
        self.assertEqual(self.d4.was_fouled(), 3)
        self.assertNotEqual(self.d4.was_fouled(), 2)
        self.assertEqual(self.m1.was_fouled(), 4)
        self.assertNotEqual(self.m1.was_fouled(), 1)
        self.assertEqual(self.m2.was_fouled(), 4)
        self.assertNotEqual(self.m2.was_fouled(), 2)
        self.assertEqual(self.m3.was_fouled(), 5)
        self.assertNotEqual(self.m3.was_fouled(), 2)
        self.assertEqual(self.m4.was_fouled(), 5)
        self.assertNotEqual(self.m4.was_fouled(), 3)
        self.assertEqual(self.f1.was_fouled(), 6)
        self.assertNotEqual(self.f1.was_fouled(), 4)
        self.assertEqual(self.f2.was_fouled(), 0)
        self.assertNotEqual(self.f2.was_fouled(), 5)
        self.assertEqual(self.f3.was_fouled(), 0)
        self.assertNotEqual(self.f3.was_fouled(), 6)
