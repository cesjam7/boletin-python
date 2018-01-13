# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'timestamp']
    # list_display_links = ['nombre']
    list_filer = ['timestamp']
    list_editable = ['nombre'] # No puede ser el primer campo de list_display a menos que definas que el link sea otro
    search_fields = ['email', 'nombre']
    class Meta:
        model = Registrado

admin.site.register(Registrado, AdminRegistrado)
