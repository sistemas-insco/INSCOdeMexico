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
########################################################################+
from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'

    def get_complet_description(self):
        full_description = False
        if self.product_id and self.product_id.product_tmpl_id.description_sale:
            full_description = self.product_id.product_tmpl_id.name + ' ' + self.product_id.product_tmpl_id.description_sale
            return full_description or self.name
        else:
            return self.product_id.name

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attention_of = fields.Char(
        string='Attention of'
    )
    fecha_solicitud = fields.Date(
        string='Fecha de la solcitud',track_visibility="always"
    )
