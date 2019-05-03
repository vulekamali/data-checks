from goodtables import validate

from .checks.get_checks_for_dataset import get_checks_for_dataset


def run_checks(filepath):
    """
    Find the custom checks for the datapackage at filepath and
    run both the custom checks and the default checks on the datapackage.
    """
    checks = ['structure', 'schema']

    checks += get_checks_for_dataset(filepath)

    # Run the validation checks
    report = validate(
        filepath,
        checks=checks,
        row_limit=-1,
        error_limit=20,
        order_fields=True
    )
    return report
