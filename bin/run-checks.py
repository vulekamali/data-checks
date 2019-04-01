import os
from goodtables import validate
from pprint import pformat


def run_checks(filepath):
    print("===== Checking {} =====".format(filepath))
    report = validate(filepath)
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



def _print_report(report):
    def secho(*args, **kwargs):
        click.secho(file=output, *args, **kwargs)

    if json:
        return secho(json_module.dumps(report, indent=4))

    color = 'green' if report['valid'] else 'red'
    tables = report.pop('tables')
    warnings = report.pop('warnings')
    secho('DATASET', bold=True)
    secho('='*7, bold=True)
    secho(pformat(report), fg=color, bold=True)
    if warnings:
        secho('-'*9, bold=True)
    for warning in warnings:
        secho('Warning: %s' % warning, fg='yellow')
    for table_number, table in enumerate(tables, start=1):
        secho('\nTABLE [%s]' % table_number, bold=True)
        secho('='*9, bold=True)
        color = 'green' if table['valid'] else 'red'
        errors = table.pop('errors')
        secho(pformat(table), fg=color, bold=True)
        if errors:
            secho('-'*9, bold=True)
        for error in errors:
            template = '[{row-number},{column-number}] [{code}] {message}'
            substitutions = {
                'row-number': error.get('row-number', '-'),
                'column-number': error.get('column-number', '-'),
                'code': error.get('code', '-'),
                'message': error.get('message', '-'),
            }
            message = template.format(**substitutions)
            secho(message)


for dirpath, dirnames, filenames in os.walk("."):
    errors_or_warnings = 0
    dataset_count = 0
    for filename in filenames:
        if filename == "datapackage.json":
            filepath = os.path.join(dirpath, filename)
            errors_or_warnings += run_checks(filepath)
            dataset_count += 1

    print("\nFound and checked {} datasets.".format(dataset_count))
    if errors_or_warnings:
        print("ERRORS OR WARNINGS EXIST: see above")
        exit(1)
    else:
        if dataset_count:
            print("All datasets are ok")
