import string

from goodtables import validate, check, Error, registry


@check('department-names-required-characters', type='custom', context='body')
class DepartmentNamesRequiredCharacters(object):
    """
    Department names must contain [A-Z] and [a-z]
    (capitalised and non-capitalised).
    """

    def __init__(self, department_column="Department", **options):
        self.__department_column = department_column

    def check_row(self, cells):
        """
        Get the row's department names and check that they contain
        [A-Z] and [a-z] characters.
        """

        def is_department_without_a_z_and_A_Z(cell):
            """
            Check if a cell has the department header and doesn't contain
            both lowercase and uppercase letters.
            """
            return cell.get("header") == self.__department_column and not (
                any(c in cell.get("value") for c in string.ascii_lowercase) and
                any(c in cell.get("value") for c in string.ascii_uppercase)
            )

        # Filter the department names for those without both lowercase and
        # uppercase letters.
        departments = list(filter(is_department_without_a_z_and_A_Z, cells))

        errors = [Error(code='department-names-required-characters',
                        message=(f'Value "{cell.get("value")}" in column '
                                 f'{self.__department_column} must contain [A-Z] and [a-z] '
                                 '(capitalised and non-capitalised) characters '
                                 f'on row {cell.get("row-number")}'),
                        cell=cell,
                        ) for cell in departments]

        return errors

    def check_table(self):
        pass
