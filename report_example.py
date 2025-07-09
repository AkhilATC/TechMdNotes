from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import pandas as pd

styles = getSampleStyleSheet()

def add_header(canvas, doc, facility_name):
    width, height = A4
    canvas.saveState()
    
    # Left logo
    canvas.drawImage("left_logo.png", 40, height - 60, width=50, height=50, preserveAspectRatio=True)
    
    # Right logo
    canvas.drawImage("right_logo.png", width - 90, height - 60, width=50, height=50, preserveAspectRatio=True)
    
    # Title
    canvas.setFont("Helvetica-Bold", 14)
    canvas.drawCentredString(width / 2.0, height - 40, f"Monthly Report - {facility_name}")
    
    canvas.restoreState()

def create_main_table(df):
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ]))
    return table

def create_pdf(facility_name, monthly_data_dict, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4, topMargin=100)
    
    story = []

    for month, df in monthly_data_dict.items():
        story.append(Paragraph(f"<b>{month}</b>", styles['Heading2']))
        story.append(create_main_table(df))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Sub-table or notes here", styles['Normal']))
        story.append(PageBreak())

    def header_fn(canvas_, doc_):
        add_header(canvas_, doc_, facility_name)

    doc.build(
        story,
        onFirstPage=header_fn,
        onLaterPages=header_fn
    )

# === MOCK DATA EXAMPLE ===

facility = "Facility A"
monthly_data = {
    f"Month {i+1}": pd.DataFrame({
        "Metric": ["Occupancy", "Visitors", "Power Usage"],
        "Value": [80 + i, 300 + i * 10, 1200 + i * 50]
    })
    for i in range(12)
}

create_pdf(facility, monthly_data, "facility_report.pdf")
