import io
import pathlib
import re

import gradio as gr
from loguru import logger
from loko_extensions.business.decorators import extract_value_args

from fastapi import Request, FastAPI, File

# from business.gradio_interface import DEMO
from business.table_extraction import get_file_extension, extract_table


from utils.decorator_fastAPI import ExtractValueArgsFastapi


app = FastAPI()


@app.post("/extract_table")
@ExtractValueArgsFastapi(file=True)
def extract_table_ocr(file, args):
    logger.debug(f"file {file.filename}")
    logger.debug(f"args {args}")
    logger.debug(f"body:: {type(file)}")

    type_of_doc = args.pop("type_of_doc")
    camelot_kwargs = dict()
    camelot_kwargs["process_background"] = args.get("process_background", False)
    camelot_kwargs["flavor"] = args.get("flavor", "lattice")
    camelot_kwargs["line_scale"] = int(args.get("line_scale", 15))
    camelot_kwargs["split_text"] = args.get("split_text", False)
    logger.debug(f"=================== CAMELOT {camelot_kwargs}")
    non_mr_kwargs = dict()
    non_mr_kwargs["ocr_kwargs"] = dict()
    non_mr_kwargs["ocr_kwargs"]["lang"] = args.get("lang", "ita")
    non_mr_kwargs["extraction_kwargs"] = dict()
    non_mr_kwargs["extraction_kwargs"]["implicit_rows"] = args.get("implicit_rows", True)
    non_mr_kwargs["extraction_kwargs"]["borderless_tables"] = args.get("borderless_tables", False)

    res = extract_table(file, type_of_doc, camelot_kwargs, non_mr_kwargs)

    logger.debug(f"resssssssssssss {res}")
    return dict(content=res)


#
# @app.route("/extract_table_serv", methods=["POST"])
# # @extract_value_args(_request=request, file=True)
# def extract_table_serv():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400
#
#     file = request.files['file']
#     logger.debug(f"file {file.__dict__}")
#
#     # fb = file.read()
#     #
#     # res = extract_from_camelot(fb, kwargs)
#     logger.debug(f"resssssssssssss {res}")
#     return jsonify(dict(content=res))


# @app.route("/extract_table2", methods=["POST"])
# # @extract_value_args(_request=request, file=True)
# def test3(file):
#     print("qui")
#     file = request.files['file']
#     fb = file.read()
#     file_bytes = io.BytesIO(fb).getbuffer()
#     file_path = pathlib.Path('file.pdf').write_bytes(file_bytes)
#     logger.debug(f"FILE PATH{file_path}")
#     tables = camelot.read_pdf("file.pdf")
#     logger.debug(f"filepath {file_path}, tables: {tables.__dict__}")
#     # tables.export("file.json", f='json', compress=True)
#     temp = tables[0].df
#     tt = temp.to_dict()
#     #     return dict(msg="example")
#     # file = request.files['file']
#     # fname = file.filename
#     # print("You have uploaded a file called:",fname)
#     # return jsonify(dict(msg=f"Hello extensions, you have uploaded the file:!"))
#     return jsonify(tt)




# CUSTOM_PATH = "/TableExtractorGui/"

# app = gr.mount_gradio_app(app, DEMO, path=CUSTOM_PATH)
