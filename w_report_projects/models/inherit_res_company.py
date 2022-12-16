# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Alan Guzmán
#               (age@tech.com)
########################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'


    #Campos de reporte de Entrega de items

    codification_equipment_delivery_1 = fields.Char(
        string='Codigo de formatos de calidad',
        default='FA.G.01.02.05'
    )
    codification_equipment_delivery_2 = fields.Char(
        string='Procedimiento de recoleccion y entrega',
        default='PA.G.02.06'
    )
    codification_equipment_delivery_3 = fields.Char(
        string='Formato de entrega',
        default='FA.G.02.04.06'
    )

# Campos de orden de servicio 

    codification_equipment_delivery_4 = fields.Char(
        string='Formato oredn de servicio',
        default='FA.G.02.03.05'
    )

# Campos de recepcion de items
    codification_equipment_delivery_5 = fields.Char(
        string='Codido de formato de calidad',
        default='FA.G.01.02.05'
    )
    codification_equipment_delivery_6 = fields.Char(
        string='Precedimiento de atencion de servicio',
        default='FA.G.01.02.05'
    )
    codification_equipment_delivery_7 = fields.Char(
        string='Formato de recepcion',
        default='PA.G.02.06'
    )

    codification_equipment_delivery_8 = fields.Char(
        string='Codification equipment reception report 8',
        default='PA.G.02.02.06'
    )

    codification_equipment_delivery_9 = fields.Char(
        string='Codificacion de salida de inventario',
        default='PA.G.02.02.06'
    )
