from PyPDF2 import PdfWriter, PdfReader
import io
# import treepoem
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


existing_pdf = PdfReader(
    open("blank.pdf", "rb"))
output = PdfWriter()

pdfmetrics.registerFont(TTFont('Fira', 'FiraCode.ttf'))

for i in range(10):
    j=i+1
    print(f"Page {j}\t", end='')
    packet1 = io.BytesIO()
    can1 = canvas.Canvas(packet1, pagesize=A4)
    can1.setFont('Fira', size=12)
    can1.drawCentredString(33.7, 803, "T")
    can1.drawCentredString(54.1, 803, "0")
    can1.drawCentredString(74.5, 803, "1")
    can1.drawCentredString(94.9, 803, f"{i}")

    # image = treepoem.generate_barcode(
    #     barcode_type="qrcode",  # One of the BWIPP supported codes.
    #     data=f"192.168.1.7:8000/cut/B10{i}",
    # )
    # image.convert("1").save("barcode.png")
    # can1.drawImage('barcode.png', 20, 704.68,
    #                width=31, height=31, mask='auto')

    can1.save()
    packet1.seek(0)
    new_pdf1 = PdfReader(packet1)

    page1 = existing_pdf.pages[i]
    page1.merge_page(new_pdf1.pages[0])
    output.add_page(page1)
    print("finished.\n", end='')

output_stream = open("cut-out.pdf", "wb")
output.write(output_stream)
output_stream.close()
