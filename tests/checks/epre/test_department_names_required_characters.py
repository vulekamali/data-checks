import unittest

from goodtables import cells, checks, validate, Error
import goodtables.cells

from data_checks.checks.epre.department_names_required_characters import DepartmentNamesRequiredCharacters


class TestDepartmentNamesRequiredCharacters(unittest.TestCase):
    def setUp(self):
        self.check = DepartmentNamesRequiredCharacters()

    def test_contains_only_lowercase_characters(self):
        cells = [
            goodtables.cells.create_cell(
                'department', 'only lowercase', 'department', row_number=1),
            goodtables.cells.create_cell(
                'department', 'only lowercase', 'department', row_number=2)
        ]

        errors = self.check.check_row(cells)

        self.assertEqual(len(errors), 2)
        self.assertEqual(errors[0].row_number, 1)
        self.assertEqual(
            errors[0].code, 'department-names-required-characters')

    def test_contains_only_uppercase_characters(self):
        cells = [
            goodtables.cells.create_cell(
                'department', 'ONLY UPPERCASE', 'department', row_number=4)
        ]

        errors = self.check.check_row(cells)

        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].row_number, 4)
        self.assertEqual(
            errors[0].code, 'department-names-required-characters')

    def test_contains_only_non_alphabetical_characters(self):
        cells = [
            goodtables.cells.create_cell(
                'department', '12345!@)#(*', 'department', row_number=4),
        ]

        errors = self.check.check_row(cells)

        self.assertEqual(len(errors), 1)
        self.assertEqual(
            errors[0].code, 'department-names-required-characters')

    def test_contains_lowercase_and_uppercase_characters(self):
        cells = [
            goodtables.cells.create_cell(
                'department', 'Cooperative Governance And Traditional Affairs', 'department', row_number=1),
            goodtables.cells.create_cell(
                'department', 'Social Development', 'department', row_number=2)
        ]

        errors = self.check.check_row(cells)

        self.assertEqual(len(
            errors), 0, 'Department names that contain both lowercase and uppercase characters should not create an error')


if __name__ == '__main__':
    unittest.main()
