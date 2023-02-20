from img2table.document import Image
from img2table.ocr import TesseractOCR

# Instantiation of the image
img = Image(src="example-page.png")
img = Image(src="../data/background_lines_converted.png")
ocr = TesseractOCR(lang="eng")

# Table identification
img_tables = img.extract_tables(ocr=ocr, implicit_rows=False)

# Result of table identification
print(img_tables[0].df.to_dict(orient="records"))

img.to_xlsx(dest="dest.xlsx",
            ocr=ocr,
            implicit_rows=True,
            min_confidence=50)
#
# [ExtractedTable(title=None, bbox=(10, 8, 745, 314),shape=(6, 3)),
#  ExtractedTable(title=None, bbox=(936, 9, 1129, 111),shape=(2, 2))]