from docx import Document
from docx.shared import Pt

# Create a new Document
document = Document()

# Define a function to add a heading and content


def add_heading(text, level=1):
    document.add_heading(text, level=level)


def add_paragraph(text, bold=False):
    p = document.add_paragraph()
    run = p.add_run(text)
    run.bold = bold


# Project Charter Title
add_heading("Project Charter", level=0)

# Section 1: Project Overview
add_heading("1. Project Overview", level=1)
document.add_paragraph("- Project Name:")
document.add_paragraph("- Project Sponsor:")
document.add_paragraph("- Project Manager:")
document.add_paragraph("- Date:")

# Section 2: Purpose and Justification
add_heading("2. Purpose and Justification", level=1)
document.add_paragraph("- Purpose:")
document.add_paragraph(
    "  Describe why this project is being undertaken and its overall objectives.")
document.add_paragraph("- Justification:")
document.add_paragraph(
    "  Explain the business need or problem that this project will address and the benefits expected to be realized.")

# Section 3: Project Objectives
add_heading("3. Project Objectives", level=1)
document.add_paragraph("- Primary Objectives:")
document.add_paragraph("  - Objective 1: [Brief description]")
document.add_paragraph("  - Objective 2: [Brief description]")
document.add_paragraph("  - Objective 3: [Brief description]")
document.add_paragraph("- Key Success Criteria:")
document.add_paragraph(
    "  Define how success will be measured (e.g., on-time delivery, budget adherence, quality benchmarks).")

# Section 4: Scope
add_heading("4. Scope", level=1)
document.add_paragraph("- In-Scope:")
document.add_paragraph(
    "  List the main deliverables, tasks, or outcomes that are part of the project.")
document.add_paragraph("- Out-of-Scope:")
document.add_paragraph(
    "  Clarify what is not included in this project to manage expectations.")

# Section 5: Stakeholders
add_heading("5. Stakeholders", level=1)
document.add_paragraph("- Key Stakeholders:")
document.add_paragraph("  - Sponsor:")
document.add_paragraph("  - Project Team:")
document.add_paragraph("  - Customers/Users:")
document.add_paragraph("  - Other Interested Parties:")
document.add_paragraph("- Roles and Responsibilities:")
document.add_paragraph(
    "  Outline each stakeholder’s role and their responsibilities within the project.")

# Section 6: Project Milestones and Timeline
add_heading("6. Project Milestones and Timeline", level=1)
document.add_paragraph("- Major Milestones:")
document.add_paragraph("  - Milestone 1: Description – Date")
document.add_paragraph("  - Milestone 2: Description – Date")
document.add_paragraph("  - Milestone 3: Description – Date")
document.add_paragraph("- Timeline:")
document.add_paragraph(
    "  Provide a high-level timeline or Gantt chart if available.")

# Section 7: Budget and Resources
add_heading("7. Budget and Resources", level=1)
document.add_paragraph("- Estimated Budget:")
document.add_paragraph(
    "  Include any available budget information or financial constraints.")
document.add_paragraph("- Resource Requirements:")
document.add_paragraph(
    "  Identify the resources needed (personnel, equipment, software, etc.).")

# Section 8: Risks and Assumptions
add_heading("8. Risks and Assumptions", level=1)
document.add_paragraph("- Risks:")
document.add_paragraph(
    "  List potential risks and challenges that could impact the project, along with proposed mitigation strategies.")
document.add_paragraph("- Assumptions:")
document.add_paragraph(
    "  State any assumptions made during the project planning.")

# Section 9: Approval
add_heading("9. Approval", level=1)
document.add_paragraph("- Sponsor Approval:")
document.add_paragraph("  Name and Signature")
document.add_paragraph("- Date:")

# Save the document
document.save("Project_Charter_Template.docx")
print("Word document 'Project_Charter_Template.docx' has been created!")
