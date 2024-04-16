import tabula

pdf_path = "/Users/adriantudoran/Downloads/Extras_BCR.pdf"

dfs = tabula.read_pdf(pdf_path, pages="all", stream=True)
print(dfs[0])

print(len(dfs))