import io
import pathlib
from pathlib import Path

from PIL import Image
from loguru import logger

from business.camelot_extraction import extract_from_camelot
from business.non_mr_extraction import extraxt_table_from_non_mr_img
from config.AppConfig import TEMP_FILENAME

from utils.pdf_utils import is_machine_readable


def get_file_extension(filename):
    path = Path(filename)
    f_extension = path.suffix.lower()
    return f_extension


def extract_table(file, type_of_doc, camelot_kwargs, non_mr_kwargs):
    f_ext = get_file_extension(filename=file.filename)
    fb = file.file.read()
    is_mr = False
    # is_mr = False if type_of_doc=="Non Machine-Readable"
    doc = None
    if f_ext == ".pdf" and type_of_doc != "Non Machine-Readable":
        is_mr, doc = is_machine_readable(fb)
    logger.debug(f"Is machine readable:: {is_mr}")
    if is_mr:
        logger.debug(f"Extracting from camelot")

        res = extract_from_camelot(fb, camelot_kwargs)
    else:
        logger.debug(f"Extracting from table_ocr")
        file_path = ""
        res = []
        if doc:
            logger.debug(f"PDF extraction with table_ocr")
            for i, page in enumerate(doc):
                img = page.get_pixmap(dpi=200)
                # img.save("img0_"+i+".jpg")
                data = img.tobytes("format")
                img = Image.open(io.BytesIO(data))
                file_path = pathlib.Path(TEMP_FILENAME + i + f_ext).write_bytes(img)
                res.append(extraxt_table_from_non_mr_img(file_path, ext_type=f_ext, non_mr_kwargs=non_mr_kwargs))
        else:
            logger.debug(f"Image extraction with table_ocr")
            file_bytes = io.BytesIO(fb).getbuffer()
            file_path = pathlib.Path(TEMP_FILENAME + f_ext).write_bytes(file_bytes)
            logger.debug(f"file path {file_path}")
            res = extraxt_table_from_non_mr_img(TEMP_FILENAME + f_ext, ext_type=f_ext, non_mr_kwargs=non_mr_kwargs)

        logger.debug(f"======================================\n res table ocr {res}")
    # print(file.name)
    # for file in file_handler(file):
    #     ext = get_format(file.name)
    #     converter = CONV_FACTORY.get(ext)()
    #     if ext == "pdf":
    #         res_tmp = converter(file, force_extraction, configs=configs)
    #     else:
    #         res_tmp = converter(file, configs=configs)
    #     res = merge(res, res_tmp) if res else res_tmp
    return res

#
# def extract_table():
#     file_bytes = io.BytesIO(file).getbuffer()
#     file_path = pathlib.Path('file.pdf').write_bytes(file_bytes)
#     logger.debug(f"FILE PATH{file_path}")
