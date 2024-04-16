import tabula

pdf_path = "/Users/adriantudoran/Downloads/Extras_BCR.pdf"

dfs = tabula.read_pdf(pdf_path, pages="all", stream=True, output_format="json")
print(dfs[0])
