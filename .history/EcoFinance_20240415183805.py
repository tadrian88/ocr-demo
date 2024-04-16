import tabula

pdf_path = "/Users/adriantudoran/Downloads/Extras_BCR.pdf"

dfs = tabula.read_pdf(pdf_path, pages="all", stream=True, output_format="json")

dfs = tabula.read_pdf(
    pdf_path,
    pages="all",
    lattice=True,
    pandas_options={"header": [0, 1]},
    area=[0, 0, 50, 100],
    relative_area=True,
    multiple_tables=False,
)

print(dfs[0])
