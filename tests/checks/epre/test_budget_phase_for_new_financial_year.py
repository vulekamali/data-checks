import unittest

from goodtables import cells, checks, validate, Error
import goodtables.cells

from data_checks.checks.epre.budget_phase_for_new_financial_year \
    import BudgetPhaseForNewFinancialYear


class TestBudgetPhaseForNewFinancialYear(unittest.TestCase):
    def test_correct_expected_budget_phase(self):
        new_year = 2018
        expected_budget_phase = "Main Appropriation"
        check = BudgetPhaseForNewFinancialYear(new_year, expected_budget_phase)
        cells = [
            goodtables.cells.create_cell(
                'budget_phase', expected_budget_phase, 'budget_phase', row_number=1),
            goodtables.cells.create_cell(
                'financial_year', new_year, 'financial_year', row_number=1),
        ]

        errors = check.check_row(cells)

        self.assertEqual(len(errors), 0, ('No errors should be returned when '
                                          'the expected budget phase was given'))

    def test_incorrect_expected_budget_phase(self):
        new_year = 2018
        expected_budget_phase = "Main Appropriation"
        check = BudgetPhaseForNewFinancialYear(new_year, expected_budget_phase)
        cells = [
            goodtables.cells.create_cell(
                'budget_phase', 'Not an expected budget phase', 'budget_phase', row_number=1),
            goodtables.cells.create_cell(
                'financial_year', new_year, 'financial_year', row_number=1),
        ]

        errors = check.check_row(cells)

        self.assertEqual(len(errors), 1, ('An error should be returned when '
                                          'an unexpected budget phase was given'))

    def test_no_expected_budget_phase(self):
        new_year = 2018
        expected_budget_phase = "Main Appropriation"
        check = BudgetPhaseForNewFinancialYear(new_year, expected_budget_phase)
        cells = [
            goodtables.cells.create_cell(
                'financial_year', new_year, 'financial_year', row_number=1),
        ]

        errors = check.check_row(cells)

        self.assertEqual(len(errors), 1, ('An error should be returned when '
                                          'no budget phase was given'))

    def test_unexpected_budget_phase_for_different_year(self):
        new_year = 2018
        expected_budget_phase = "Main Appropriation"
        check = BudgetPhaseForNewFinancialYear(new_year, expected_budget_phase)
        cells = [
            goodtables.cells.create_cell(
                'budget_phase', 'Not an expected budget phase', 'budget_phase', row_number=1),
            goodtables.cells.create_cell(
                'financial_year', new_year + 1, 'financial_year', row_number=1),
        ]

        errors = check.check_row(cells)

        self.assertEqual(len(errors), 0, ('No errors should be returned when '
                                          'the financial year wasn\'t the new '
                                          'year'))


if __name__ == '__main__':
    unittest.main()
