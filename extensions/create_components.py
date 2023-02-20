from loko_extensions.model.components import Input, Output, Dynamic, AsyncSelect, Component, save_extensions, Select, \
    Events
from loko_extensions.model.components import Arg

pdf_service = "extract_table"
doc_type = Select(label="Type of Document", name="type_of_doc",
                  options=["Auto-Detect", "Machine-Readable", "Non Machine-Readable"], value="Auto-Detect")

language = Dynamic(label="Document Language", name="lang", dynamicType="select", options=["ita", "eng"], value="ita",
                   parent="type_of_doc",
                   condition='{parent}=="Non Machine-Readable"', helper="Choose the language that the OCR needs to use")

borderless_tables = Dynamic(label="Detect Borderless Tables", name="borderless_tables", dynamicType="boolean", parent="type_of_doc",
                   condition='{parent}=="Non Machine-Readable"', value=False)

implicit_rows = Dynamic(label="Split implicit rows", name="implicit_rows", dynamicType="boolean", parent="type_of_doc",
                   condition='{parent}=="Non Machine-Readable"', value=True)


flavor = Dynamic(label="Parsing Method", name="flavor", dynamicType="select", options=["stream", "lattice"],
                 value="lattice", parent="type_of_doc", condition='{parent}=="Machine-Readable"',
                 helper='Select "lattice" if you want a deterministic parser, it works good on doc with demarcated lines between cells and can detect multiple tables in a single page. Select the option "stream" if your docs have whitespaces to simulate table structure.')

process_background = Dynamic(label="Process Background Lines", name="process_background", dynamicType="boolean",
                             parent="type_of_doc",
                             condition='{parent}=="Machine-Readable"',
                             description='Whether to detect line segments not in foreground. It will be taken into consideration only if "lattice" is selected as parser.',
                             value=False)

line_scale = Dynamic(label="Line Scale", name="line_scale", dynamicType="number", parent="type_of_doc",
                     condition='{parent}=="Machine-Readable"', value=15,
                     helper='Increase the value to detect smaller lines. Large value (>150) will lead to detect text as lines. It only works if "lattice" is selected as parser.')

split_text = Dynamic(label="Split Text", name="split_text", dynamicType="boolean", parent="type_of_doc",
                     condition='{parent}=="Machine-Readable"', value=False,
                     description="Choose whether to split the text that spans across multiple cells.")



args_list = [doc_type, language, borderless_tables, implicit_rows, flavor, process_background, line_scale, split_text]

table_ocr_components = Component(name="TableExtractor", inputs=[Input("pdf", service=pdf_service)], group='OCR',
                                 args=args_list, icon="RiTableFill")

save_extensions([table_ocr_components])
