from pdfrw import PdfReader
from ..utils.operation import (
    OperationRequest,
    OperationResult,
    OperationTelemetryContext,
)


def combine_documents(pdf_request: OperationRequest) -> OperationResult:
    with OperationTelemetryContext() as telem:
        pass

    return


def split_documents(pdf_request: OperationRequest) -> OperationResult:

    return
