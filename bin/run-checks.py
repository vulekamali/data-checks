import os
import sys

from pprint import pformat

from data_checks.check_datapackage import run_checks


def run_report(filepath):
    print("===== Checking {} =====".format(filepath))
<<<<<<< HEAD
    report = run_checks(filepath)
=======
    report = validate(filepath, row_limit=10**12, order_fields=True, error_limit=100)
>>>>>>> WIP using order_fields option
    log_report(report)
    return report['error-count'] + len(report['warnings'])

def log_report(report):
    # Borrowed from goodtables.cli
    tables = report.pop('tables')
    warnings = report['warnings']
    print('DATASET')
    print('='*7)
    print(pformat(report))
    if warnings:
        print('-'*9)
    for warning in warnings:
        print('Warning: %s' % warning)
    for table_number, table in enumerate(tables, start=1):
        print('\nTABLE [%s]' % table_number)
        print('='*9)
        errors = table.pop('errors')
        print(pformat(table))
        if errors:
            print('-'*9)
        for error in errors:
            template = '[{row-number},{column-number}] [{code}] {message}'
            substitutions = {
                'row-number': error.get('row-number', '-'),
                'column-number': error.get('column-number', '-'),
                'code': error.get('code', '-'),
                'message': error.get('message', '-'),
            }
            message = template.format(**substitutions)
            print(message)

errors_or_warnings = 0
dataset_count = 0

datapackage_dir = sys.argv[1] if len(sys.argv) > 1 else  "./datapackages"

for dirpath, dirnames, filenames in os.walk(datapackage_dir):
    for filename in filenames:
        if filename == "datapackage.json":
            filepath = os.path.join(dirpath, filename)
            errors_or_warnings += run_report(filepath)
            dataset_count += 1

print("\nFound and checked {} datasets.".format(dataset_count))

if errors_or_warnings:
    print("ERRORS OR WARNINGS EXIST: see above")
    exit(1)
else:
    if dataset_count:
        print("All datasets are ok")
