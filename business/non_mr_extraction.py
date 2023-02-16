import table_ocr.util
import table_ocr.extract_tables
import table_ocr.extract_cells
import table_ocr.ocr_image
import table_ocr.ocr_to_csv
from loguru import logger


def extraxt_table_from_non_mr_img(image_filepath):
    # image_filepath = download_image_to_tempdir(url)
    image_tables = table_ocr.extract_tables.main([image_filepath])
    logger.debug(f"Extracted the following tables from the image{image_filepath}:\n image_tables")
    for image, tables in image_tables:
        logger.debug(f"Processing tables for {image}.")
        for table in tables:
            logger.debug(f"Processing table {table}.")
            cells = table_ocr.extract_cells.main(table)
            ocr = [
                table_ocr.ocr_image.main(cell, None)
                for cell in cells
            ]
            logger.debug("Extracted {} cells from {}".format(len(ocr), table))
            logger.debug("Cells:")
            for c, o in zip(cells[:3], ocr[:3]):
                with open(o) as ocr_file:
                    # Tesseract puts line feeds at end of text.
                    # Stript it out.
                    text = ocr_file.read().strip()
                    logger.debug("{}: {}".format(c, text))
            # If we have more than 3 cells (likely), print an ellipses
            # to show that we are truncating output for the demo.
            if len(cells) > 3:
                logger.debug("...")
            return table_ocr.ocr_to_csv.text_files_to_csv(ocr)
