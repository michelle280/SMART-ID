from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

def render_to_pdf(template_src,context_dict={}):
    template = get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pisa_status = pisa.CreatePDF(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="aplication/pdf")  
    return None