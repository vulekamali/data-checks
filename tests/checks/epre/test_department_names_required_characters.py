import unittest

import goodtables.cells

from data_checks.checks.epre.department_names_required_characters import (
    DepartmentNamesRequiredCharacters,
)

from ..helpers import BaseCheckTestCase


class TestDepartmentNamesRequiredCharacters(BaseCheckTestCase):
    def setUp(self):
        super().setUp()
        self.check = DepartmentNamesRequiredCharacters(column_header="department")

    def test_contains_only_lowercase_characters(self):
        cells = [
            goodtables.cells.create_cell(
                "department", "only lowercase", "department", row_number=1
            ),
            goodtables.cells.create_cell(
                "department", "only lowercase", "department", row_number=2
            ),
        ]
        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "department-names-required-characters",
                "row-number": 1,
                "column-number": None,
                "message": 'Value "only lowercase" in column department must contain [A-Z] '
                "and [a-z] (capitalised and non-capitalised) characters on row 1",
                "message-data": {"header": "department", "value": "only lowercase"},
            },
            {
                "code": "department-names-required-characters",
                "row-number": 2,
                "column-number": None,
                "message": 'Value "only lowercase" in column department must contain [A-Z] '
                "and [a-z] (capitalised and non-capitalised) characters on row 2",
                "message-data": {"header": "department", "value": "only lowercase"},
            },
        ]
        self.assertCheckErrors(expected_errors, errors)

    def test_contains_only_uppercase_characters(self):
        cells = [
            goodtables.cells.create_cell(
                "department", "ONLY UPPERCASE", "department", row_number=4
            )
        ]

        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "department-names-required-characters",
                "row-number": 4,
                "column-number": None,
                "message": 'Value "ONLY UPPERCASE" in column department must contain [A-Z] '
                "and [a-z] (capitalised and non-capitalised) characters on row 4",
                "message-data": {"header": "department", "value": "ONLY UPPERCASE"},
            }
        ]
        self.assertCheckErrors(expected_errors, errors)

    def test_contains_only_non_alphabetical_characters(self):
        cells = [
            goodtables.cells.create_cell(
                "department", "12345!@)#(*", "department", row_number=4
            )
        ]
        errors = self.run_checks(self.check, [cells])

        expected_errors = [
            {
                "code": "department-names-required-characters",
                "row-number": 4,
                "column-number": None,
                "message": 'Value "12345!@)#(*" in column department must contain [A-Z] and '
                "[a-z] (capitalised and non-capitalised) characters on row 4",
                "message-data": {"header": "department", "value": "12345!@)#(*"},
            }
        ]
        self.assertCheckErrors(expected_errors, errors)

    def test_contains_lowercase_and_uppercase_characters(self):
        cells = [
            goodtables.cells.create_cell(
                "department",
                "Cooperative Governance And Traditional Affairs",
                "department",
                row_number=1,
            ),
            goodtables.cells.create_cell(
                "department", "Social Development", "department", row_number=2
            ),
        ]
        errors = self.run_checks(self.check, [cells])
        self.assertCheckErrors([], errors)


if __name__ == "__main__":
    unittest.main()
