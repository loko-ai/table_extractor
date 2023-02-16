import io
import pathlib
import re

import camelot
import fitz
from loguru import logger

from config.AppConfig import TEMP_FILENAME

f_ext = ".pdf"
def extract_from_camelot(file, kwargs):
    file_bytes = io.BytesIO(file).getbuffer()
    file_path = pathlib.Path(TEMP_FILENAME+f_ext).write_bytes(file_bytes)
    logger.debug(f"FILE PATH{file_path}")
    tables = camelot.read_pdf(TEMP_FILENAME+f_ext, **kwargs)
    logger.debug(f"filepath {file_path}, tables: {tables.__dict__}")
    res = []
    for page, pdf_table in enumerate(tables):
        page_dict = tables[page].df.to_dict()
        # res["page" + str(page)] = page_dict
        res.append(page_dict)
        logger.debug(f"extr::: \n \n{page_dict}")
        logger.debug(f"performance::: \n \n{tables[page].parsing_report}")
    return res
