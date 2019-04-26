from importlib import import_module
import os

from goodtables import validate


def run_checks(filepath):
    # Get the dataset's type and year
    path, filename = os.path.split(filepath)
    path, dataset_type = os.path.split(path)
    path, dataset_year = os.path.split(path)

    checks = ['structure', 'schema']

    # Get the custom checks for the dataset type
    try:
        checks += import_module(f'.checks.{dataset_type}',
                                'data_checks').checks
    except ModuleNotFoundError:
        pass
    except AttributeError:
        pass

    # Run the validation checks
    report = validate(filepath, checks=checks, row_limit=10**12)
    return report
