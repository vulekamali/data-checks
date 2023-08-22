from goodtables import check

from data_checks.checks.base import BaseRowCheck


@check("budget-phase-for-new-financial-year", type="custom", context="body")
class BudgetPhaseForNewFinancialYear(BaseRowCheck):
    """
    Budget Phase column for rows where Financial Year is the dataset's
    new financial year must be "Main appropriation" - that is - if the
    dataset is EPRE 2018-19, rows where Financial Year is 2018, Budget
    Phase must be Main Appropriation.
    """

    error_code = "budget-phase-for-new-financial-year"
    error_message = (
        "{actual_budget_phase} in column {budget_phase_column}"
        ' must be "{expected_budget_phase}"'
        ' when column {financial_year_column} is "{new_year}"'
        " on row {row_number}"
    )

    def __init__(self, new_year, expected_budget_phase="Main appropriation",
        budget_phase_column="BudgetPhase",
        financial_year_column="FinancialYear", **options):
        super().__init__(**options)
        self.new_year = new_year
        self.expected_budget_phase = expected_budget_phase
        self.budget_phase_column = budget_phase_column
        self.financial_year_column = financial_year_column

    def should_check_row(self, row_data: dict) -> bool:
        return self.new_year == row_data[self.financial_year_column]

    def check_row_data(self, row_data: dict) -> bool:
        return self.expected_budget_phase == row_data.get(self.budget_phase_column)

    def get_row_error_message_substitutions(self, row_data: dict) -> dict:
        budget_phase = row_data.get("budget_phase")
        actual_budget_phase = f'"{budget_phase}"' if budget_phase else "Empty value"
        return {
            **super().get_row_error_message_substitutions(row_data),
            "actual_budget_phase": actual_budget_phase,
            "expected_budget_phase": self.expected_budget_phase,
            "new_year": self.new_year,
            "budget_phase_column": self.budget_phase_column,
            "financial_year_column": self.financial_year_column,
        }
