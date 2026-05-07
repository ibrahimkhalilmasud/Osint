from pathlib import Path

from jinja2 import Template
from reportlab.pdfgen import canvas

from ..models import ReportPayload


HTML_TEMPLATE = Template(
    """
<!doctype html>
<html>
  <head><title>OSINT Report {{ report.investigation_id }}</title></head>
  <body>
    <h1>OSINT Report</h1>
    <p>Investigation ID: {{ report.investigation_id }}</p>
    <p>Confidence: {{ report.confidence_score }}</p>
    <h2>Grouped entities</h2>
    <ul>
    {% for key, values in report.grouped_entities.items() %}
      <li>{{ key }}: {{ values | join(', ') }}</li>
    {% endfor %}
    </ul>
  </body>
</html>
"""
)


def persist_report_artifacts(report: ReportPayload) -> dict[str, str]:
    out_dir = Path("reports/generated")
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / f"{report.investigation_id}.html"
    pdf_path = out_dir / f"{report.investigation_id}.pdf"

    html_path.write_text(HTML_TEMPLATE.render(report=report.model_dump(mode="json")), encoding="utf-8")

    pdf = canvas.Canvas(str(pdf_path))
    pdf.drawString(72, 800, f"OSINT Report: {report.investigation_id}")
    pdf.drawString(72, 780, f"Confidence: {report.confidence_score}")
    pdf.save()

    return {
        "json": str(out_dir / f"{report.investigation_id}.json"),
        "html": str(html_path),
        "pdf": str(pdf_path),
    }
