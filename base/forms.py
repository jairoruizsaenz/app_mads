from django.forms import ModelForm
from .models import *
from django import forms


class SolicitudCreateForm(ModelForm):
    class Meta:
        model = Solicitud
        # fields = '__all__'
        fields = ['expediente_unico', 'titulo', 'anho', 'descripcion', 'expediente', 'estado', 'etapa', 'actuacion', 'sector', 'num_radicado_2', 'fecha_radicado', 'solicitante', 'nombre_proyecto', 'tipo_sustraccion', 'hectareas_solicitadas', 'normatividad', 'reserva_forestal', 'departamento', 'municipio']
    
    def __init__(self, *args, **kwargs):
        super(SolicitudCreateForm, self).__init__(*args, **kwargs)
        self.fields['expediente_unico'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['titulo'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['anho'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['expediente'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['estado'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['etapa'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['actuacion'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['sector'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['num_radicado_2'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['fecha_radicado'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['solicitante'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['nombre_proyecto'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['tipo_sustraccion'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['hectareas_solicitadas'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['normatividad'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['reserva_forestal'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['departamento'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['municipio'].widget.attrs.update({'class': 'form-select form-select-sm'})

        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = "off"


class SolicitudUpdateForm(ModelForm):
    class Meta:
        model = Solicitud
        # fields = '__all__'
        fields = ['expediente_unico', 'titulo', 'anho', 'descripcion', 'expediente', 'estado', 'etapa', 'actuacion', 'sector', 'num_radicado_2', 'fecha_radicado', 'solicitante', 'nombre_proyecto', 'tipo_sustraccion', 'hectareas_solicitadas', 'normatividad', 'reserva_forestal', 'departamento', 'municipio']
    
    def __init__(self, *args, **kwargs):
        super(SolicitudUpdateForm, self).__init__(*args, **kwargs)
        self.fields['expediente_unico'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['titulo'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['anho'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['expediente'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['estado'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['etapa'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['actuacion'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['sector'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['num_radicado_2'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['fecha_radicado'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['solicitante'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['nombre_proyecto'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['tipo_sustraccion'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['hectareas_solicitadas'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['normatividad'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['reserva_forestal'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['departamento'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['municipio'].widget.attrs.update({'class': 'form-select form-select-sm'})

        for field in self.fields:
            self.fields[field].widget.attrs['autocomplete'] = "off"