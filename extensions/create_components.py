from loko_extensions.model.components import Input, Output, Dynamic, AsyncSelect, Component, save_extensions, Select, \
    Events
from loko_extensions.model.components import Arg

pdf_service = "extract_table"
table_ocr = Component(name="TableExtractor", inputs=[Input("pdf", service= pdf_service)],  group='OCR')
save_extensions([table_ocr])
