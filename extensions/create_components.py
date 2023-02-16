from loko_extensions.model.components import Input, Output, Dynamic, AsyncSelect, Component, save_extensions, Select, \
    Events
from loko_extensions.model.components import Arg

pdf_service = "extract_table"
process_background = Arg(type="boolean", label="Process Background Lines", name="process_background", value=False)

args_list = [process_background]

table_ocr_components = Component(name="TableExtractor", inputs=[Input("pdf", service=pdf_service)], group='OCR', args=args_list, icon="RiTableFill")

save_extensions([table_ocr_components])
