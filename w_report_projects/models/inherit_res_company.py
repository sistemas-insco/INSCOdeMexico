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

    codification_equipment_delivery_1 = fields.Char(
        string='Codification equipment report 1',
        default='FA.G.01.02.05'
    )
    codification_equipment_delivery_2 = fields.Char(
        string='Codification equipment report 2',
        default='PA.G.02.06'
    )
    codification_equipment_delivery_3 = fields.Char(
        string='Codification equipment report 3',
        default='FA.G.02.04.06'
    )
    codification_equipment_delivery_4 = fields.Char(
        string='Codification equipment report 4',
        default='FA.G.02.03.05'
    )
    codification_equipment_delivery_5 = fields.Char(
        string='Codification equipment reception report 5',
        default='FA.G.01.02.05'
    )
    codification_equipment_delivery_6 = fields.Char(
        string='Codification equipment reception report 6',
        default='FA.G.01.02.05'
    )
    codification_equipment_delivery_7 = fields.Char(
        string='Codification equipment reception report 7',
        default='PA.G.02.06'
    )
    codification_equipment_delivery_8 = fields.Char(
        string='Codification equipment reception report 8',
        default='PA.G.02.02.06'
    )