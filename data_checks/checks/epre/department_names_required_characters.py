import string

from goodtables import validate, check, Error, registry


@check('department-names-required-characters', type='custom', context='body')
class DepartmentNamesRequiredCharacters(object):
    """
    Department names must contain [A-Z] and [a-z]
    (capitalised and non-capitalised).
    """

    def __init__(self, **options):
        pass

    def check_row(self, cells):
        """
        Get the row's department names and check that they contain
        [A-Z] and [a-z] characters.
        """

        def is_new_financial_year_value(cell):
            return cell.get("header") == "department" and cell.get(
                "value") == self.new_year

        def is_department_without_a_z_and_A_Z(cell):
            return cell.get("header") == "department" and not (
                any(c in cell.get("value") for c in string.ascii_lowercase) and
                any(c in cell.get("value") for c in string.ascii_uppercase)
            )

        departments = list(
            filter(is_department_without_a_z_and_A_Z, cells))

        errors = [Error(code='department-names-required-characters',
                        message=f'Value "{cell.get("value")}" in column department must contain [A-Z] and [a-z] (capitalised and non-capitalised) characters on row {cell.get("row-number")}',
                        cell=cell,
                        ) for cell in departments]

        return errors

    def check_table(self):
        pass
