from goodtables import check

from data_checks.checks.base import BaseColumnValueCheck


def has_lower(s: str) -> bool:
    return any(c.islower() for c in s)


def has_upper(s: str) -> bool:
    return any(c.isupper() for c in s)


@check("department-names-required-characters", type="custom", context="body")
class DepartmentNamesRequiredCharacters(BaseColumnValueCheck):
    """
    Department names must contain [A-Z] and [a-z]
    (capitalised and non-capitalised).
    """

    error_code = "department-names-required-characters"
    error_message = (
        'Value "{value}" in column {header}'
        " must contain [A-Z] and [a-z] (capitalised and non-capitalised) characters"
        " on row {row_number}"
    )

    column_header = "department"

    def check_cell_value(self, value: str) -> bool:
        return has_lower(value) and has_upper(value)
