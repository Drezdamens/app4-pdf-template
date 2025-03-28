import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="L")

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="R")
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("Output")