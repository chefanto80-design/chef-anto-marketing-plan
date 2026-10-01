"""Unit tests for tools/roi_calculator.py. Run: python3 -m unittest discover tests"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from roi_calculator import project  # noqa: E402


class TestROI(unittest.TestCase):
    def test_hand_worked_example(self):
        # 300 / 2.50 = 120 installs; 4% pay = 4.8 payers; 30% annual = 1.44, monthly = 3.36
        # revenue = (3.36*4.99*12 + 1.44*39) * 0.85 = (201.1968 + 56.16) * 0.85 = 218.75328
        r = project(300, 2.50, 0.04, 0.30, 0.15)
        self.assertAlmostEqual(r["installs"], 120)
        self.assertAlmostEqual(r["paying_users"], 4.8)
        self.assertAlmostEqual(r["first_year_revenue"], 218.75328, places=4)
        self.assertAlmostEqual(r["cost_per_paying_user"], 62.5)
        self.assertAlmostEqual(r["first_year_roi"], (218.75328 - 300) / 300, places=6)
        # monthly ARPU = 218.75328/12/4.8 = 3.79780; payback = 62.5/3.79780 = 16.457
        self.assertAlmostEqual(r["payback_months"], 16.457, places=2)

    def test_all_monthly_no_fee(self):
        r = project(100, 1.0, 0.10, 0.0, 0.0)  # 100 installs, 10 payers, all monthly
        self.assertAlmostEqual(r["first_year_revenue"], 10 * 4.99 * 12)

    def test_zero_paid_rate(self):
        r = project(100, 1.0, 0.0, 0.5)
        self.assertEqual(r["paying_users"], 0)
        self.assertEqual(r["first_year_revenue"], 0)
        self.assertEqual(r["payback_months"], float("inf"))

    def test_rejects_bad_inputs(self):
        with self.assertRaises(ValueError):
            project(100, 0, 0.1, 0.5)
        with self.assertRaises(ValueError):
            project(100, 1, 1.5, 0.5)


if __name__ == "__main__":
    unittest.main()
