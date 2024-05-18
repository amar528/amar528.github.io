from unittest import TestCase
from leetcode75.queue.dota_2_senate_649 import Solution


class TestSolution(TestCase):
    def test_predict_party_victory_example1(self):
        senate = "RD"

        sol = Solution()
        result = sol.predictPartyVictory(senate)

        self.assertEqual("Radiant", result)

    def test_predict_party_victory_example2(self):
        senate = "RDD"

        sol = Solution()
        result = sol.predictPartyVictory(senate)

        self.assertEqual("Dire", result)

    def test_predict_party_victory_example3(self):
        senate = "DDR"

        sol = Solution()
        result = sol.predictPartyVictory(senate)

        self.assertEqual("Dire", result)

    def test_predict_party_victory_example4(self):
        senate = "RRR"

        sol = Solution()
        result = sol.predictPartyVictory(senate)

        self.assertEqual("Radiant", result)

    def test_predict_party_victory_example5(self):
        senate = "RDR"

        sol = Solution()
        result = sol.predictPartyVictory(senate)

        self.assertEqual("Radiant", result)

    def test_predict_party_victory_example6(self):
        senate = "DDRRR"

        sol = Solution()
        result = sol.predictPartyVictory(senate)

        self.assertEqual("Dire", result)
