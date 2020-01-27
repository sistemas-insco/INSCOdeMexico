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
import re
import html2text


class ProjectTask(models.Model):
    _inherit = 'project.task'

    number_tags = fields.Integer(
        string='Number tags'
    )
    observations_report_equipment_reception = fields.Text(
        string='Observations report equipment reception',
        help='Observations for report reception equipment')

    conditions_report_service_order = fields.Text(
        string='Conditions report service order',
        help='Conditions for report service order'
    )
    date_reception = fields.Date(
        string='Date reception'
    )
    date_delivery = fields.Date(
        string='Date delivery'
    )
    brought_by = fields.Char(
        string='Brought by'
    )
    delivery_by = fields.Char(
        string='Delivery by'
    )
    especial_requiriments = fields.Text(
        string='Especial requiriment'
    )
    invoice_number = fields.Char(string='Invoice number')

    def get_street_partner(self):
        return "{}, {}, {}".format(
            self.partner_id.street_name or '',
            self.partner_id.street_number or '',
            self.partner_id.street_number2 or '')

    def get_address_partner(self):
        return {
            'colony': self.partner_id.l10n_mx_edi_colony or '',
            'city': self.partner_id.city or '',
            'zip': self.partner_id.zip or '',
            'street_name': self.partner_id.street_name or '',
            'number1': self.partner_id.street_number or '',
            'number2': self.partner_id.street_number2 or '',
            'vat': self.partner_id.vat or '',
            'phone': self.partner_id.phone or '',
            'state': self.partner_id.state_id.name if self.partner_id.state_id.name else '',
            'x_studio_contacto' : self.partner_id.x_studio_contacto}

    def get_street_shipping(self):
        return "{}, {}, {}".format(
            self.sale_line_id.order_id.partner_shipping_id.street_name or '',
            self.sale_line_id.order_id.partner_shipping_id.street_number or '',
            self.sale_line_id.order_id.partner_shipping_id.street_number2 or '')

    def get_certificate_addres(self):
        return {
            'name': self.sale_line_id.order_id.partner_shipping_id.name or '',
            'street': self.sale_line_id.order_id.partner_shipping_id.street_name or '',
            'colony': self.sale_line_id.order_id.partner_shipping_id.l10n_mx_edi_colony or '',
            'city': self.sale_line_id.order_id.partner_shipping_id.city or '',
            'zip': self.sale_line_id.order_id.partner_shipping_id.zip or '',
            'state': self.sale_line_id.order_id.partner_shipping_id.state_id.name or '',
            'email': self.sale_line_id.order_id.partner_shipping_id.email or '',
            'number': self.sale_line_id.order_id.partner_invoice_id.street_number or '',
            'number2': self.sale_line_id.order_id.partner_invoice_id.street_number2 or ''
        }

    def convert_description_pad(self, description):
        flags = re.IGNORECASE | re.MULTILINE
        html = re.sub(r'\[font\s*([^\]]+)\]', '<font \1>', description, flags=flags)
        html = re.sub(r'\[/font\s*\]', '</font>', html, flags=flags)
        return html

    def get_description_text(self):
        html = self.convert_description_pad(self.description)
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.ignore_emphasis = True
        return h.handle(html)