# -*- coding: utf-8 -*-
#import datetime
from odoo import models, fields, api, _


# Clases para complemetar lasbitacoras

class customItemMarca(models.Model):
    _name = "item.marca"
    _description = "Item-Marca"


    name= fields.Char(string='Marca', required=True, copy=False, readonly=True, index=True)


class customItemModelo(models.Model):
    _name = "item.modelo"
    _description = "Item-Modelo"

    name= fields.Char(string='Modelo', required=True, copy=False, readonly=True, index=True)

class customItemClasificacion(models.Model):
    _name = "item.clasificacion"
    _description = "clasificacion-equipo"


    name= fields.Char(string='Clasificacion', required=True, copy=False, readonly=True, index=True)
    tiempo_asignado=fields.Integer(string='TIEMPO ASIGNADO EN DIAS')