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
        assert len(errors) == 0

        errors = self.check.check_table()
        assert len(errors) == 0

    def test_contains_duplicates_of_each_required_value(self):
        cells = [
            goodtables.cells.create_cell('budget_phase', value, 'budget_phase')
            for value in self.required_values * 2
        ]
        errors = self.check.check_row(cells)
        assert len(errors) == 0

        errors = self.check.check_table()
        assert len(errors) == 0

    def test_contains_some_values(self):
        cells = [
            goodtables.cells.create_cell('budget_phase', value, 'budget_phase')
            for value in self.required_values[0:2]
        ]

        errors = self.check.check_row(cells)
        assert len(errors) == 0

        errors = self.check.check_table()
        assert len(errors) == 2


if __name__ == '__main__':
    unittest.main()
