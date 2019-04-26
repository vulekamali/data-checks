import unittest
from goodtables import validate, check, Error
import goodtables.cells
from data_checks.checks.epre.budget_phase_required_values \
    import BudgetPhaseRequiredValues


class TestBudgetPhaseRequiredValues(unittest.TestCase):
    def setUp(self):
        self.required_values = [
            'Audited Outcome',
            'Adjusted appropriation',
            'Main appropriation',
            'Medium Term Estimates',
        ]
        self.check = BudgetPhaseRequiredValues()

    def test_contains_one_of_each_required_value(self):
        cells = [
            goodtables.cells.create_cell('budget_phase', value, 'budget_phase')
            for value in self.required_values
        ]

        errors = self.check.check_row(cells)
        errors += self.check.check_table()

        self.assertEqual(len(errors), 0, """No errors should be returned for cells
                         that contain each of the required budget_phase values""")

    def test_contains_duplicates_of_each_required_value(self):
        cells = [
            goodtables.cells.create_cell('budget_phase', value, 'budget_phase')
            for value in self.required_values * 2
        ]

        errors = self.check.check_row(cells)
        errors += self.check.check_table()

        self.assertEqual(len(errors), 0, """No errors should be returned
                         for cells that contain each of the required
                         budget_phase values""")

    def test_contains_some_required_values(self):
        required_values_present = 2

        cells = [
            goodtables.cells.create_cell('budget_phase', value, 'budget_phase')
            for value in self.required_values[0:required_values_present]
        ]

        errors = self.check.check_row(cells)
        errors += self.check.check_table()

        self.assertEqual(len(errors),
                         len(self.required_values) - required_values_present,
                         """No errors should be returned for cells that
                         contain each of the required budget_phase values""")

    def test_contains_no_required_values(self):
        cells = [
            goodtables.cells.create_cell(
                'budget_phase', 'not a required value', 'budget_phase')
        ]

        errors = self.check.check_row(cells)
        errors += self.check.check_table()

        self.assertEqual(len(errors), len(self.required_values),
                         """One error for each of the required
                         values should be returned if the dataset
                         contains none of the required values.""")


if __name__ == '__main__':
    unittest.main()
