import io
import pathlib
import re

from flask import Flask, request, jsonify
from loguru import logger
from loko_extensions.business.decorators import extract_value_args

# from fastapi import Request, FastAPI, File
# from business.camelot_extraction import extract_from_camelot
from business.table_extraction import get_file_extension, extract_table

app = Flask("")

from utils.decorator_fastAPI import ExtractValueArgsFastapi
import camelot


# app = FastAPI()
#
# @app.post("/extract_table")
# @ExtractValueArgsFastapi(file=True)
# def extract_table(file, args):
#     file_path = pathlib.Path('file').write_bytes(io.BytesIO(file.decode()).getbuffer())
#     tables = camelot.read_pdf(file_path)
#     tables.export("file.json", f='json', compress=True)
#     return dict(msg="example")
#

@app.route("/extract_table", methods=["POST"])
@extract_value_args(_request=request, file=True)
def extract_table_ocr(file, args):
    logger.debug(f"file {file.__dict__}")
    logger.debug(f"args {args}")
    kwargs = dict()
    kwargs["process_background"] = args.pop("process_background")
    res = extract_table(file, kwargs)
    # fb = file.read()
    #
    # res = extract_from_camelot(fb, kwargs)
    logger.debug(f"resssssssssssss {res}")
    return jsonify(dict(content=res))

# @app.route("/", methods=["get"])
# def example():
#     return jsonify(dict(msg = "ciao"))
#
#
@app.route("/extract_table_serv", methods=["POST"])
# @extract_value_args(_request=request, file=True)
def extract_table_serv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    logger.debug(f"file {file.__dict__}")
    kwargs = dict()
    kwargs["process_background"] = None
    res = extract_table(file, kwargs)
    # fb = file.read()
    #
    # res = extract_from_camelot(fb, kwargs)
    logger.debug(f"resssssssssssss {res}")
    return jsonify(dict(content=res))


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


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
