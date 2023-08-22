"""
Helpers for declarative data checks.

These base classes implement common code for checking cell, row, and column constraints.
"""
import abc
from typing import Any, Collection, Dict, List, Optional, Sequence, Set

from goodtables import Error


class BaseCheck:
    """
    Base check, with error construction.
    """

    options: Dict[str, Any]

    error_code: str
    error_message: str

    def __init__(self, **options: Any) -> None:
        self.options = options

    def check_row(self, cells: Sequence[dict]) -> Optional[List[Error]]:
        """
        See `goodtables.inspector.Inspector`
        """

    def check_table(self) -> Optional[List[Error]]:
        """
        See `goodtables.inspector.Inspector`
        """

    def get_error(
        self,
        cell: Optional[dict] = None,
        row_number: Optional[int] = None,
        message_substitutions: Optional[dict] = None,
    ) -> Error:
        """
        Construct an `Error` for this check.
        """
        message = self.error_message
        error = Error(
            code=self.error_code,
            cell=cell,
            row_number=row_number,
            message=message,
            message_substitutions=message_substitutions,
        )

        # Check message validity:
        try:
            error.message
        except KeyError as e:
            raise ValueError(
                f"Missing error message substitution: {e} in {message!r}"
            ) from e

        return error


def _get_row_number(cells: Sequence[dict]) -> Optional[int]:
    # XXX: No handling of more than one row-number value, for now.
    for cell in cells:
        if cell.get("row-number"):
            return cell.get("row-number")
    else:
        return None


def _get_row_data(cells: Sequence[dict]) -> dict:
    row_data = {cell["header"]: cell["value"] for cell in cells}
    # Consistency check: bail out on conflicting cell headers, for now.
    assert len(row_data.keys()) == len(cells), cells
    return row_data


class BaseRowCheck(BaseCheck, abc.ABC):
    """
    Base check for row constraints.

    Subclasses must provide `check_row_data`.
    """

    def check_row(self, cells: Sequence[dict]) -> Optional[List[Error]]:
        row_data = _get_row_data(cells)
        if self.should_check_row(row_data) and not self.check_row_data(row_data):
            row_number = _get_row_number(cells)
            return [
                self.get_error(
                    row_number=row_number,
                    message_substitutions=self.get_row_error_message_substitutions(
                        row_data
                    ),
                )
            ]
        else:
            return None

    def should_check_row(self, row_data: dict) -> bool:
        """
        Override this to check only a subset of rows.
        """
        return True

    @abc.abstractmethod
    def check_row_data(self, row_data: dict) -> bool:
        """
        Return True if the row data is valid.
        """

    def get_row_error_message_substitutions(self, row_data: dict) -> dict:
        """
        Error context for the row.

        Extend this to provide additional context.
        """
        return {}


class BaseCellCheck(BaseCheck, abc.ABC):
    """
    Base check for cell value constraints.

    Subclasses must provide `check_cell_value`.
    """

    def check_row(self, cells: Sequence[dict]) -> Optional[List[Error]]:
        return [
            self.get_error(
                cell=cell,
                message_substitutions=self.get_cell_error_message_substitutions(cell),
            )
            for cell in cells
            if self.should_check_cell(cell)
            if not self.check_cell_value(cell["value"])
        ]

    def should_check_cell(self, cell: dict) -> bool:
        """
        Override this to check only a subset of cells.
        """
        return True

    @abc.abstractmethod
    def check_cell_value(self, value: str) -> bool:
        """
        Return True if the cell value is valid.
        """

    def get_cell_error_message_substitutions(self, cell: dict) -> dict:
        """
        Error context for the cell: `header` and `value`

        Extend this to provide context.
        """
        return {"header": cell["header"], "value": cell["value"]}


class BaseColumnValueCheck(BaseCellCheck):
    """
    Base check for named columns constraints.

    Subclasses must provide `column_header` and `check_cell_value`.
    """

    column_header: str

    def __init__(self, column_header: Optional[str] = None, **options: Any):
        super().__init__()
        if column_header is not None:
            self.column_header = column_header
        assert hasattr(self, "column_header"), f"missing column_header for {self}"

    def should_check_cell(self, cell: dict) -> bool:
        return self.column_header == cell["header"]


class BaseRequiredColumnValueCheck(BaseColumnValueCheck):
    """
    Base check: Column contains one or more required values.

    Subclasses must provide `column_header` and `required_values`.
    """

    error_message = (
        'Table does not contain the "{missing_value}" value'
        " in the {header} column at least once"
    )

    required_values: Collection[str]
    seen_values: Set[str]

    def __init__(self, **options: Any):
        super().__init__(**options)
        self.seen_values = set()

    def check_cell_value(self, value: str) -> bool:
        self.seen_values.add(value)
        return True

    def check_table(self) -> Optional[List[Error]]:
        # Iterate instead of using set arithmetic, to retain consistent reporting order.
        missing_values = [
            value for value in self.required_values if value not in self.seen_values
        ]
        return [
            self.get_error(
                message_substitutions={
                    "header": self.column_header,
                    "missing_value": missing_value,
                }
            )
            for missing_value in missing_values
        ]
