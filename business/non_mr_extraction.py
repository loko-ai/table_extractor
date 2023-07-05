# import table_ocr.util
# import table_ocr.extract_tables
# import table_ocr.extract_cells
# import table_ocr.ocr_image
# import table_ocr.ocr_to_csv
from fastapi import HTTPException
from img2table.document import PDF, Image
from img2table.ocr import TesseractOCR
from loguru import logger


# TODO: Opzione che utilizza table_ocr. Tenere o buttare?
# def extraxt_table_from_non_mr_img(image_filepath):
#     # image_filepath = download_image_to_tempdir(url)
#     image_tables = table_ocr.extract_tables.main([image_filepath])
#     logger.debug(f"Extracted the following tables from the image{image_filepath}:\n image_tables")
#     for image, tables in image_tables:
#         logger.debug(f"Processing tables for {image}.")
#         for table in tables:
#             logger.debug(f"Processing table {table}.")
#             cells = table_ocr.extract_cells.main(table)
#             ocr = [
#                 table_ocr.ocr_image.main(cell, None)
#                 for cell in cells
#             ]
#             logger.debug("Extracted {} cells from {}".format(len(ocr), table))
#             logger.debug("Cells:")
#             for c, o in zip(cells[:3], ocr[:3]):
#                 with open(o) as ocr_file:
#                     # Tesseract puts line feeds at end of text.
#                     # Stript it out.
#                     text = ocr_file.read().strip()
#                     logger.debug("{}: {}".format(c, text))
#             # If we have more than 3 cells (likely), print an ellipses
#             # to show that we are truncating output for the demo.
#             if len(cells) > 3:
#                 logger.debug("...")
#             logger.debug(f"OCR::: {text}")
#             logger.debug(f"OCR2222::: {ocr}")
#             return table_ocr.ocr_to_csv.text_files_to_csv(ocr)


def extraxt_table_from_non_mr_img(doc_filepath, ext_type="pdf", non_mr_kwargs=None):
    logger.debug("Extracting table from non mr img/pdf")
    ocr = TesseractOCR(**non_mr_kwargs["ocr_kwargs"])
    logger.debug(f"Extension type {ext_type}, Doc file path {doc_filepath}")
    if ext_type == ".pdf":
        logger.debug("opening pdf...")
        doc = PDF(src=doc_filepath, pdf_text_extraction=False)
    else:
        logger.debug("opening image...")
        # Instantiation of the image
        doc = Image(src=doc_filepath)
    logger.debug(f"going to extract from doc::: {doc} ")


    # Table identification
    doc_tables = doc.extract_tables(ocr=ocr, **non_mr_kwargs["extraction_kwargs"])
    logger.debug(f"extracted doc tables types and content {type(doc_tables), doc_tables}")
    if isinstance(doc_tables, list):
        res = [table.df.to_dict(orient="records") for table in doc_tables]
    elif isinstance(doc_tables, dict):
        res = {idx:[table.df.to_dict(orient="records") for table in table_list] for idx, table_list in doc_tables.items()}
    else:
        msg = "ERROR!!! The extracted table has a type not yet supported!"
        logger.error(msg)
        raise Exception(msg)
        # raise HTTPException(detail=msg, status_code=400)
    logger.debug("ciaon")
    return res
