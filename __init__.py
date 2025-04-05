from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import sys

# Function to generate large page content


def generate_large_page_content(canvas, page_number):
    """
    Create content for a single page with a large amount of text and images.
    """
    width, height = letter

    # Add text to the page
    canvas.setFont("Helvetica", 12)
    canvas.drawString(
        50, height - 50, f"Page {page_number}: This is content for page {page_number}")

    # Add repeated text to increase content size
    for i in range(100):
        canvas.drawString(50, height - 80 - (i * 15),
                          f"This is repeated text line {i + 1} for page {page_number}.")

    # Add a dummy large rectangle (as a placeholder for large content)
    canvas.setFillColorRGB(0.9, 0.9, 0.9)
    canvas.rect(50, 50, width - 100, height / 3, fill=1, stroke=0)

# Main function


def main():
    try:
        # Parse command line arguments for size
        if len(sys.argv) != 2:
            print("Usage: python __init__.py <size_in_mb>")
            target_size_mb = 1
        else:
            target_size_mb = float(sys.argv[1])
    except ValueError:
        print("Error: Size must be a number.")
        sys.exit(1)

    # Output PDF file name
    output_file = f"./tmp/generated_pdf_{target_size_mb}_mb.pdf"

    # Create an in-memory buffer for the PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Loop to create multiple pages until the estimated size is reached
    page_number = 1
    while True:
        generate_large_page_content(c, page_number)
        c.showPage()
        page_number += 1

        # Check the buffer size
        if page_number == 1000 * target_size_mb:  # Check every 10 pages for efficiency
            break

    # Finalize and save the PDF to disk
    c.save()
    with open(output_file, "wb") as f:
        f.write(buffer.getvalue())

    print(
        f"PDF file of approximately {target_size_mb}MB has been generated: generated_pdf.pdf")


if __name__ == "__main__":
    main()
