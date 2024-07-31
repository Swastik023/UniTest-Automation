import pandas as pd
from fpdf import FPDF

def generate_csv_report(data, output_path):
    data.to_csv(output_path, index=False)

def generate_pdf_report(data, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for row in data.itertuples():
        pdf.cell(200, 10, txt=str(row), ln=True)
    pdf.output(output_path)

if __name__ == "__main__":
    data = pd.read_csv('data/processed_data/processed_utm_data.csv')
    generate_csv_report(data, 'reports/csv/utm_report.csv')
    generate_pdf_report(data, 'reports/pdf/utm_report.pdf')
