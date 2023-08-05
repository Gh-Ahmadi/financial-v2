import treepoem
image = treepoem.generate_barcode(
    barcode_type="qrcode",  # One of the BWIPP supported codes.
    data="localhost:8000/cut/B102",
)
image.convert("1").save("barcode.png")
