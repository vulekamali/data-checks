import unittest

import goodtables.cells

from data_checks.checks.epre.budget_phase_required_values import (
    BudgetPhaseRequiredValues,
)

from ..helpers import BaseCheckTestCase


class TestBudgetPhaseRequiredValues(BaseCheckTestCase):
    def setUp(self):
        super().setUp()
        self.required_values = [
            "Audited Outcome",
            "Adjusted appropriation",
            "Main appropriation",
            "Medium Term Estimates",
        ]
        self.check = BudgetPhaseRequiredValues(column_header="budget_phase")

    def test_contains_one_of_each_required_value(self):
        cells = [
            goodtables.cells.create_cell("budget_phase", value, "budget_phase")
            for value in self.required_values
        ]
        errors = self.run_checks(self.check, [cells])

        self.assertCheckErrors([], errors)

    def test_contains_duplicates_of_each_required_value(self):
        cells = [
            goodtables.cells.create_cell("budget_phase", value, "budget_phase")
            for value in self.required_values * 2
        ]
        errors = self.run_checks(self.check, [cells])

        self.assertCheckErrors([], errors)

    def test_contains_some_required_values(self):
        required_values_present = 2

        cells = [
            goodtables.cells.create_cell("budget_phase", value, "budget_phase")
            for value in self.required_values[0:required_values_present]
        ]
        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "budget-phase-required-values",
                "row-number": None,
                "column-number": None,
                "message": (
                    f'Table does not contain the "{value}" value'
                    " in the budget_phase column at least once"
                ),
                "message-data": {"header": "budget_phase", "missing_value": value},
            }
            for value in self.required_values[required_values_present:]
        ]
        self.assertCheckErrors(expected_errors, errors)

    def test_contains_no_required_values(self):
        cells = [
            goodtables.cells.create_cell(
                "budget_phase", "not a required value", "budget_phase"
            )
        ]
        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "budget-phase-required-values",
                "row-number": None,
                "column-number": None,
                "message": (
                    f'Table does not contain the "{value}" value'
                    " in the budget_phase column at least once"
                ),
                "message-data": {"header": "budget_phase", "missing_value": value},
            }
            for value in self.required_values
        ]
        self.assertCheckErrors(expected_errors, errors)


if __name__ == "__main__":
    unittest.main()
