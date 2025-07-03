from fpdf import FPDF

pdf = FPDF(format='A4')
pdf.add_page()
pdf.set_font("Arial", size=50)

page_width = pdf.w  # ~210 mm for A4
page_height = pdf.h  # ~297 mm

# Calculate vertical position (12.5vh)
y_pos = page_height * 12.5 / 100  # ≈ 37.125 mm

# Width of your column: 5% of page width
col_width = page_width * 10 / 100  # about 10.5 mm

# Calculate x to center the cell horizontally
x_pos = (page_width - col_width) / 2

# Set cursor position
pdf.set_xy(x_pos, y_pos)

# Print cell with small width, center aligned text inside
pdf.cell(w=col_width, h=10, txt="CS50 Shirtificate", ln=1, align='C')

# Add image (JPEG format)
pdf.image("shirtificate.png", x=20/2, y=page_height/4,
          w=page_width-20)  # adjust x, y, w (and h if needed)
pdf.set_font("Arial", size=20)

# Set cursor position
pdf.set_xy(x_pos, y_pos)
pdf.set_text_color(255, 255, 255)
# Print cell with small width, center aligned text inside
pdf.cell(w=col_width, h=200, txt="John Harvard took CS50", ln=1, align='C')

pdf.output("shirtificate.pdf")
