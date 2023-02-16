import fitz
from loguru import logger

from config.AppConfig import MACHINE_READABLE_TH


def is_machine_readable(file):
    doc = fitz.open(".pdf", file)
    text = []
    for page in doc:
        p_text = page.get_text()
        text.append(p_text)
    text = "".join(text)
    logger.debug(f"text::: {len(text)}")
    if len(text) > MACHINE_READABLE_TH:
        return True, doc
    else:
        return False, None
