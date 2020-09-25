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
MIDFIELD4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 21, 21]
FORWARD1 =  [90, 3, 3, 1, 2, 2, 2, 3, 2, 2, 1, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 24]
FORWARD2 =  [57, 1, 1, 1, 1, 1, 1, 5, 1, 1, 0, 0, 27, 145, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
FORWARD3 =  [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 28, 155, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0]

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


    # def test_yellows(self):
    #     self.assertEqual(sc.yellow_cards(0), 0)
    #     self.assertEqual(sc.yellow_cards(1), -1)
    #     self.assertEqual(sc.yellow_cards(2), -2)

    # def test_reds(self):
    #     self.assertEqual(sc.red_cards(0), 0)
    #     self.assertEqual(sc.red_cards(1), -3)

    # def test_own_goals(self):
    #     self.assertEqual(sc.own_goal(0), 0)
    #     self.assertEqual(sc.own_goal(1), -2)
    #     self.assertEqual(sc.own_goal(3), -6)

    # def test_tackles(self):
    #     self.assertEqual(sc.tackles(0), 0)
    #     self.assertEqual(sc.tackles(1), 0)
    #     self.assertEqual(sc.tackles(3), 0)
    #     self.assertEqual(sc.tackles(4), 1)
    #     self.assertEqual(sc.tackles(7), 1)
    #     self.assertEqual(sc.tackles(8), 2)
    #     self.assertEqual(sc.tackles(11), 2)
    #     self.assertEqual(sc.tackles(12), 3)

    # def test_passes(self):
    #     self.assertEqual(sc.passes(0), 0)
    #     self.assertEqual(sc.passes(20), 0)
    #     self.assertEqual(sc.passes(35), 1)
    #     self.assertEqual(sc.passes(55), 1)
    #     self.assertEqual(sc.passes(70), 2)
    #     self.assertEqual(sc.passes(75), 2)
    #     self.assertEqual(sc.passes(110), 3)

    # def test_key_passes(self):
    #     self.assertEqual(sc.key_passes(0), 0)
    #     self.assertEqual(sc.key_passes(1), 0)
    #     self.assertEqual(sc.key_passes(2), 0)
    #     self.assertEqual(sc.key_passes(3), 1)
    #     self.assertEqual(sc.key_passes(4), 1)
    #     self.assertEqual(sc.key_passes(6), 2)
    #     self.assertEqual(sc.key_passes(8), 2)
    #     self.assertEqual(sc.key_passes(9), 3)

    # def test_crosses(self):
    #     self.assertEqual(sc.crosses(0), 0)
    #     self.assertEqual(sc.crosses(1), 0)
    #     self.assertEqual(sc.crosses(2), 0)
    #     self.assertEqual(sc.crosses(3), 1)
    #     self.assertEqual(sc.crosses(4), 1)
    #     self.assertEqual(sc.crosses(6), 2)
    #     self.assertEqual(sc.crosses(8), 2)
    #     self.assertEqual(sc.crosses(9), 3)

    # def test_big_chance(self):
    #     self.assertEqual(sc.big_chance(0), 0)
    #     self.assertEqual(sc.big_chance(1), 1)
    #     self.assertEqual(sc.big_chance(2), 2)
    #     self.assertEqual(sc.big_chance(4), 4)
    #     self.assertEqual(sc.big_chance(5), 5)

    # def test_clearances(self):
    #     self.assertEqual(sc.clearances(0), 0)
    #     self.assertEqual(sc.clearances(1), 0)
    #     self.assertEqual(sc.clearances(4), 1)
    #     self.assertEqual(sc.clearances(5), 1)
    #     self.assertEqual(sc.clearances(12), 3)

    # def test_blocks(self):
    #     self.assertEqual(sc.blocks(0), 0)
    #     self.assertEqual(sc.blocks(1), 0)
    #     self.assertEqual(sc.blocks(2), 1)
    #     self.assertEqual(sc.blocks(3), 1)
    #     self.assertEqual(sc.blocks(4), 2)
    #     self.assertEqual(sc.blocks(8), 4)

    # def test_interceptions(self):
    #     self.assertEqual(sc.interceptions(0), 0)
    #     self.assertEqual(sc.interceptions(1), 0)
    #     self.assertEqual(sc.interceptions(2), 0)
    #     self.assertEqual(sc.interceptions(3), 0)
    #     self.assertEqual(sc.interceptions(4), 1)
    #     self.assertEqual(sc.interceptions(7), 1)
    #     self.assertEqual(sc.interceptions(8), 2)
    #     self.assertEqual(sc.interceptions(12), 3)

    # def test_recovered_balls(self):
    #     self.assertEqual(sc.recovered_balls(0), 0)
    #     self.assertEqual(sc.recovered_balls(5), 0)
    #     self.assertEqual(sc.recovered_balls(6), 1)
    #     self.assertEqual(sc.recovered_balls(7), 1)
    #     self.assertEqual(sc.recovered_balls(12), 2)

    # def test_error_leading_to_goal(self):
    #     self.assertEqual(sc.error_leading_to_goal(0), 0)
    #     self.assertEqual(sc.error_leading_to_goal(1), -1)
    #     self.assertEqual(sc.error_leading_to_goal(2), -2)
    #     self.assertEqual(sc.error_leading_to_goal(3), -3)
    #     self.assertNotEqual(sc.error_leading_to_goal(4), 2)

    # def test_own_goal_assist(self):
    #     self.assertEqual(sc.own_goal_assist(0), 0)
    #     self.assertEqual(sc.own_goal_assist(1), 1)
    #     self.assertEqual(sc.own_goal_assist(2), 2)
    #     self.assertEqual(sc.own_goal_assist(3), 3)
    #     self.assertNotEqual(sc.own_goal_assist(2), 3)

    # def test_shots(self):
    #     self.assertEqual(sc.shots(0), 0)
    #     self.assertEqual(sc.shots(1), 0)
    #     self.assertEqual(sc.shots(3), 0)
    #     self.assertEqual(sc.shots(4), 1)
    #     self.assertEqual(sc.shots(6), 1)
    #     self.assertEqual(sc.shots(8), 2)
    #     self.assertEqual(sc.shots(9), 2)
    #     self.assertNotEqual(sc.shots(3), 2)

    # def test_was_fouled(self):
    #     self.assertEqual(sc.was_fouled(0), 0)
    #     self.assertEqual(sc.was_fouled(1), 0)
    #     self.assertEqual(sc.was_fouled(3), 0)
    #     self.assertEqual(sc.was_fouled(4), 1)
    #     self.assertEqual(sc.was_fouled(6), 1)
    #     self.assertEqual(sc.was_fouled(8), 2)
    #     self.assertEqual(sc.was_fouled(9), 2)
    #     self.assertNotEqual(sc.was_fouled(3), 2)
