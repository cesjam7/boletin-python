# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "inicio.html", {})

def nosotros(request):
    return render(request, "nosotros.html", {})
