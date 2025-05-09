import pandas as pd
from fpdf import FPDF

# Step 1: Read Data
df = pd.read_csv("data.csv")

# Step 2: Analyze Data
summary = df.groupby("Department")[["Salary", "Experience"]].mean().reset_index()
summary.columns = ["Department", "Average Salary", "Average Experience"]

# Step 3: Generate PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "REPORT OF MY FILE", ln=True, align="C")

pdf.set_font("Times", size=12)
pdf.ln(20)

# Table Headers
pdf.cell(70, 10, "Department", border=1)
pdf.cell(60, 10, "Average Salary", border=1)
pdf.cell(60, 10, "Average Experience", border=1, ln=True)

# Table Content
for index, row in summary.iterrows():
    pdf.cell(70, 10, row["Department"], border=1)
    pdf.cell(60, 10, f"Rs.{row['Average Salary']:.2f}", border=1)
    pdf.cell(60, 10, f"{row['Average Experience']:.1f} yrs", border=1, ln=True)

# Save PDF
pdf.output("task2_output.pdf")
