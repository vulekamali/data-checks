from goodtables import validate, check, Error, registry


@check('budget-phase-for-new-financial-year', type='custom', context='body')
class BudgetPhaseForNewFinancialYear(object):
    """
    Budget Phase column for rows where Financial Year is the dataset's
    new financial year must be "Main appropriation" - that is - if the
    dataset is EPRE 2018-19, rows where Financial Year is 2018, Budget
    Phase must be Main Appropriation.
    """

    def __init__(self, new_year, expected_budget_phase="Main appropriation",
                 **options):
        self.new_year = new_year
        self.expected_budget_phase = expected_budget_phase

    def check_row(self, cells):
        """
        Get the row's budget_phase values and remove them from the
        required values that still need to be found.
        """

        def is_new_financial_year_value(cell):
            return cell.get("header") == "financial_year" and cell.get(
                "value") == self.new_year

        def is_expected_budget_phase_value(cell):
            return cell.get("header") == "budget_phase" and cell.get(
                "value") == self.expected_budget_phase

        errors = []

        new_year_values = list(filter(is_new_financial_year_value, cells))

        budget_phase_values = list(
            filter(is_expected_budget_phase_value, cells))

        # If at least one of the financial_year values are the new year
        # then there must be one budget_phase value which is the expected
        # budget phase
        if new_year_values and not budget_phase_values:
            error = Error('budget-phase-for-new-financial-year',
                          message=f'Value "{new_year_values[0].get("value")}" in column budget_phase must be '
                          f' must be "{self.expected_budget_phase}" when column budget_year '
                          f'is "{self.new_year}" on row {new_year_values[0].get("row-number")}',
                          row_number=new_year_values[0].get("row-number"),
                          )
            errors.append(error)

        return errors

    def check_table(self):
        pass
