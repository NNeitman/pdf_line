import pytest
from ..pdf_line.utils.operation import OperationRequest


def test_can_construct_operation_request():
    OperationRequest()
    assert 1 == 1
