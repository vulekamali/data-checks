import unittest

from data_checks.check_datapackage import run_checks


class TestCheckDatapackage(unittest.TestCase):
    def setUp(self):
        pass

    def test_perfect_datapackage(self):
        file_path = 'tests/datapackages/2018-19/epre/perfect_datapackage.json'
        report = run_checks(file_path)
        self.assertEqual(
            report['error-count'], 0, f'Report should not contain any errors for {file_path} datapackage')

    def test_missing_faulty_datapackage(self):
        file_path = 'tests/datapackages/2018-19/epre/faulty_datapackage.json'
        report = run_checks(file_path)
        error_codes = [error['code'] for error in report['tables'][0]['errors']]
        self.assertIn('budget-phase-required-values', error_codes,
         f'Report should contain an error for a missing required value for the {file_path} datapackage')
        self.assertIn('budget-phase-for-new-financial-year', error_codes,
         f'Report should contain an error for an incorrect budget_phase value for the new financial year')
        self.assertEqual(
            report['error-count'], 2, f'Report should contain exactly two errors')


if __name__ == '__main__':
    unittest.main()
