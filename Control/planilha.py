from openpyxl import Workbook
from openpyxl.drawing.image import Image
from gerador_qr import salvamento
wb = Workbook()
ws = wb.active

img = Image(salvamento)

ws.add_image(img, "A1")

wb.save("planilha.xlsx")