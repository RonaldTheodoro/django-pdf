import os
from io import BytesIO
from random import randint

import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
from django.template.loader import get_template


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        file = open('myfile.pdf', 'wb')
        pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), file)
        file.close()
        if not pdf.err:
            return HttpResponse(
                response.getvalue(),
                content_type='application/pdf'
            )
        else:
            return HttpResponse('Error rendering PDF', status=400)

    @staticmethod
    def render_to_file(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        first_name = params['request'].user.first_name
        file_name = f'{first_name}-{randint(1, 1000000)}.pdf'
        file_path = os.path.join(
            os.path.abspath(os.path.dirname('__file__'), 'store', file_name)
        )
        with open(file_name, 'wb') as pdf:
            pisa.pisaDocument(BytesIO(html.encode('UTF-8')), pdf)
        return [file_name, file_path]