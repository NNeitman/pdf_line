class OperationRequest(object):
    input_pdf_uris = None
    output_pdf_uris = None

    def __init__(self, input_pdf_uris=[], output_pdf_uris=[]):
        self.input_pdf_uris = input_pdf_uris
        self.output_pdf_uris = output_pdf_uris


class PDFTransformation(OperationRequest):
    pass


class OperationResult(object):
    resulting_uris = []

    def __init__(self, resulting_uris):
        self.resulting_uris = resulting_uris
