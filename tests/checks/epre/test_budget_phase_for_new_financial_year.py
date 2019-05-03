import unittest

import goodtables.cells

from data_checks.checks.epre.budget_phase_for_new_financial_year import (
    BudgetPhaseForNewFinancialYear,
)

from ..helpers import BaseCheckTestCase


class TestBudgetPhaseForNewFinancialYear(BaseCheckTestCase):
    new_year = 2018
    expected_budget_phase = "Main Appropriation"

    def setUp(self) -> None:
        super().setUp()
        self.check = BudgetPhaseForNewFinancialYear(
            self.new_year,
            self.expected_budget_phase,
            budget_phase_column="budget_phase",
            financial_year_column="financial_year",
        )

    def test_correct_expected_budget_phase(self):
        cells = [
            goodtables.cells.create_cell(
                "budget_phase", self.expected_budget_phase, "budget_phase", row_number=1
            ),
            goodtables.cells.create_cell(
                "financial_year", self.new_year, "financial_year", row_number=1
            ),
        ]
        errors = self.run_checks(self.check, [cells])
        self.assertCheckErrors([], errors)

    def test_incorrect_expected_budget_phase(self):
        cells = [
            goodtables.cells.create_cell(
                "budget_phase",
                "Not an expected budget phase",
                "budget_phase",
                row_number=1,
            ),
            goodtables.cells.create_cell(
                "financial_year", self.new_year, "financial_year", row_number=1
            ),
        ]
        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "budget-phase-for-new-financial-year",
                "row-number": 1,
                "column-number": None,
                "message": (
                    '"Not an expected budget phase" in column budget_phase must '
                    'be "Main Appropriation" when column financial_year is "2018" on row 1'
                ),
                "message-data": {
                    "actual_budget_phase": "Not an expected budget phase",
                    "budget_phase_column": "budget_phase",
                    "expected_budget_phase": "Main Appropriation",
                    "financial_year_column": "financial_year",
                    "new_year": 2018,
                },
            }
        ]
        self.assertCheckErrors(expected_errors, errors)

    def test_no_expected_budget_phase(self):
        cells = [
            goodtables.cells.create_cell(
                "financial_year", self.new_year, "financial_year", row_number=1
            )
        ]
        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "budget-phase-for-new-financial-year",
                "row-number": 1,
                "column-number": None,
                "message": 'Empty value in column budget_phase must be "Main Appropriation" '
                'when column financial_year is "2018" on row 1',
                "message-data": {
                    "actual_budget_phase": "Empty value",
                    "budget_phase_column": "budget_phase",
                    "expected_budget_phase": "Main Appropriation",
                    "financial_year_column": "financial_year",
                    "new_year": 2018,
                },
            }
        ]
        self.assertCheckErrors(expected_errors, errors)

    def test_unexpected_budget_phase_for_different_year(self):
        cells = [
            goodtables.cells.create_cell(
                "budget_phase",
                "Not an expected budget phase",
                "budget_phase",
                row_number=1,
            ),
            goodtables.cells.create_cell(
                "financial_year", self.new_year + 1, "financial_year", row_number=1
            ),
        ]
        errors = self.run_checks(self.check, [cells])
        self.assertCheckErrors([], errors)


if __name__ == "__main__":
    unittest.main()
