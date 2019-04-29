from importlib import import_module
import os

from . import epre


def get_checks_for_dataset(filepath):
    """
    Get the custom checks for the dataset at filepath.
    """
    checks = []
    dataset_type, dataset_year = get_dataset_info(filepath)
    if dataset_type == 'epre':
        checks += get_checks_for_epre_dataset(filepath,
                                              dataset_type, dataset_year)
    return checks


def get_checks_for_epre_dataset(filepath, dataset_type, dataset_year):
    first_year, _ = get_dataset_years(dataset_year)
    return [
        'budget-phase-required-values',
        {'budget-phase-for-new-financial-year': {'new_year': first_year}},
        'department-names-required-characters'
    ]


def get_dataset_info(filepath):
    """
    Get a dataset's year and type from its filepath.
    """
    path, filename = os.path.split(filepath)
    path, dataset_type = os.path.split(path)
    path, dataset_year = os.path.split(path)

    return dataset_type, dataset_year


def get_dataset_years(dataset_year):
    """
    Get the first and second year in a dataset year of the format 2018-19
    """
    first, second = dataset_year.split('-')
    second = first[:2] + second

    return first, second
