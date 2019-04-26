# -*- coding: utf-8 -*-
from goodtables import validate, check, Error, registry


@check('budget-phase-required-values', type='custom', context='body')
class BudgetPhaseRequiredValues(object):
    """
    Check class that there is at least one row where Budget Phase has
    each of the following values:
        - 'Audited Outcome',
        - 'Adjusted appropriation',
        - 'Main appropriation',
        - 'Medium Term Estimates'.
    """

    required_values = [
        'Audited Outcome',
        'Adjusted appropriation',
        'Main appropriation',
        'Medium Term Estimates',
    ]

    def __init__(self, **options):
        self.__required_values_left = set(self.required_values)

    def check_row(self, cells):
        """
        Get the row's budget_phase values and remove them from the required values
        that still need to be found.
        """
        errors = []

        budget_phase_values = list(filter(
            lambda cell: cell.get('header') == 'budget_phase', cells))

        # Eliminate budget_values that were found
        for budget_phase_value in budget_phase_values:
            self.__required_values_left.discard(budget_phase_value.get('value'))

        return errors

    def check_table(self):
        """
        After all the rows have been checked, check if there are any required values
        left to be found and return an error for each of the values still to be found.
        """
        errors = []

        for required_value in self.__required_values_left:
            error = Error('budget-phase-required-values',
                          message=f'Table does not contain the "{required_value}" ' \
                          'value in the budget_phase column at least once')
            errors.append(error)

        return errors
