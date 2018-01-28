from threading import Thread, activeCount

import requests
from django.utils import timezone
from django.views import generic

from .models import Product, Sale
from .render import Render


class Pdf(generic.View):
    
    def get(self, request):
        sales = Sale.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request,
        }
        return Render.render('pdf.html', params)
