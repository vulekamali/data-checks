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

    def __init__(self, **options):
        self.__required_values = set([
            'Audited Outcome',
            'Adjusted appropriation',
            'Main appropriation',
            'Medium Term Estimates',
        ])

    def check_row(self, cells):
        errors = []

        budget_phase_values = list(filter(
            lambda cell: cell.get('field') == 'budget_phase', cells))

        # Eliminate budget_values that were found
        for budget_phase_value in budget_phase_values:
            self.__required_values.discard(budget_phase_value.get('value'))

        return errors

    def check_table(self):
        errors = []

        for required_value in self.__required_values:
            error = Error('budget-phase-required-values',
                          message=f'Table does not contain the "{required_value}"' \
                          'value in the budget_phase column at least once')
            errors.append(error)

        return errors
