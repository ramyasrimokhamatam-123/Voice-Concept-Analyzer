from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(transcript, similarity, filler_ratio, score, level):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    pdf_path = "reports/Voice_Analysis_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Voice Based Concept Understanding Analyser</b>", styles["Title"]))
    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Transcript:</b> {transcript}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Semantic Similarity:</b> {similarity:.2f}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Filler Word Ratio:</b> {filler_ratio:.2%}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Final Score:</b> {score}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Understanding Level:</b> {level}", styles["BodyText"]))

    doc.build(story)

    return pdf_path