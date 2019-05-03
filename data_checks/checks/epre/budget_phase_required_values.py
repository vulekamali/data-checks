from goodtables import check

from data_checks.checks.base import BaseRequiredColumnValueCheck


@check("budget-phase-required-values", type="custom", context="body")
class BudgetPhaseRequiredValues(BaseRequiredColumnValueCheck):
    """
    Check that there is at least one row where Budget Phase has
    each of the following values:
        - 'Audited Outcome',
        - 'Adjusted appropriation',
        - 'Main appropriation',
        - 'Medium Term Estimates'.
    """

    error_code = "budget-phase-required-values"

    column_header = "BudgetPhase"

    required_values = [
        "Audited Outcome",
        "Adjusted appropriation",
        "Main appropriation",
        "Medium Term Estimates",
    ]
