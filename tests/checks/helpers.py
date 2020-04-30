import unittest
from typing import List, Sequence

from goodtables import Error


class BaseCheckTestCase(unittest.TestCase):
    """
    Base class for custom check tests.
    """

    # Remove the maxDiff limit, for larger diffs.
    maxDiff = None

    def run_checks(self, check, rows: Sequence[Sequence[dict]]) -> List[Error]:
        """
        Collect errors like `goodtables.inspector.Inspector`.
        """
        rows_errors = [
            error for cells in rows for error in (check.check_row(cells) or [])
        ]
        table_errors = check.check_table() or []
        return sorted([*rows_errors, *table_errors])

    def assertCheckErrors(
        self, expected_errors: List[dict], errors: List[Error]
    ) -> None:
        """
        Assert the expected errors.
        """
        self.assertEqual(expected_errors, [dict(error) for error in errors])
