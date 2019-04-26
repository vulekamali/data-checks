import unittest
from goodtables import validate, check, Error
import goodtables.cells
from data_checks.check_datapackage import run_checks


class TestCheckDatapackage(unittest.TestCase):
    def setUp(self):
        pass

    def test_perfect_datapackage(self):
        file_path = 'tests/datapackages/2018-19/epre/perfect_datapackage.json'
        report = run_checks(file_path)
        self.assertEqual(report['error-count'], 0, f'Report should not contain any errors for {file_path} datapackage')

    def test_missing_required_values_datapackage(self):
        file_path = 'tests/datapackages/2018-19/epre/missing_required_values_datapackage.json'
        report = run_checks(file_path)
        self.assertEqual(
            report['error-count'], 1, f'Report should contain an error for a missing required value for the {file_path} datapackage')


if __name__ == '__main__':
    unittest.main()
