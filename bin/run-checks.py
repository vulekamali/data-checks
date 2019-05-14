import os
import sys
import traceback

from pprint import pformat

from data_checks.check_datapackage import run_checks


def run_report(filepath):
    print("\n===== Checking {} =====".format(filepath))
    try:
        report = run_checks(filepath)
    except Exception as e:
        print("===== Goodtables checks resulted in an error =====")
        traceback.print_exc(file=sys.stdout)
        if isinstance(e, KeyError) and str(e) == "'field'":
            print(
                "\n===== It looks like the dataset might contain unexpected columns. ====="
            )
        return 1
    print("===== Validation Report =====")
    log_report(report)
    return report["error-count"] + len(report["warnings"])


def log_report(report):
    # Borrowed from goodtables.cli
    tables = report.pop("tables")
    warnings = report["warnings"]
    print("DATASET")
    print("=" * 7)
    print(pformat(report))
    if warnings:
        print("-" * 9)
    for warning in warnings:
        print("Warning: %s" % warning)
    for table_number, table in enumerate(tables, start=1):
        print("\nTABLE [%s]" % table_number)
        print("=" * 9)
        errors = table.pop("errors")
        print(pformat(table))
        if errors:
            table_border = "-" * 67
            error_format = "| {row:^3} | {column:^6} | {code:^38} | {message} |"
            print("\nERRORS")
            print("=" * 6)
            print(table_border)
            print(
                error_format.format(
                    row="Row", column="Column", code="Code", message="Message"
                )
            )
            print(table_border)
        for error in errors:
            substitutions = {
                "row": error.get("row-number", "-"),
                "column": error.get("column-number", "-"),
                "code": error.get("code", "-"),
                "message": error.get("message", "-"),
            }
            message = error_format.format(**substitutions)
            print(message)
        if errors:
            print(table_border)


errors_or_warnings = 0
dataset_count = 0

datapackage_dir = sys.argv[1] if len(sys.argv) > 1 else "./datapackages"

for dirpath, dirnames, filenames in os.walk(datapackage_dir):
    for filename in filenames:
        if filename == "datapackage.json":
            filepath = os.path.join(dirpath, filename)
            errors_or_warnings += run_report(filepath)
            dataset_count += 1

print("\nFound and checked {} dataset(s).".format(dataset_count))

if errors_or_warnings:
    print("ERRORS OR WARNINGS EXIST: see above")
    exit(1)
else:
    if dataset_count:
        print("All datasets are ok")
