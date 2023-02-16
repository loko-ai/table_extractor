import camelot
tables = camelot.read_pdf('../data/foo.pdf')
# tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
# tables[0].parsing_report
#
#
# tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
ex = tables[0].df # get a pandas DataFrame!
for page, pdf_table in enumerate(tables):
    page_dict = tables[page].df.to_dict()
    print(page_dict)