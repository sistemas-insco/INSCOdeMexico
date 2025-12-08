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


class ProductTemplate(models.Model):
    _inherit = 'product.template'


    #@api.one
    def _set_tags(self):
        if len(self.product_variant_ids) == 1:
            self.product_variant_ids.process = self.process

    @api.depends('product_variant_ids', 'product_variant_ids.process')
    def _compute_tags(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.process = template.product_variant_ids.process
        for template in (self - unique_variants):
            template.process = ''

    process = fields.Char(
        string='Process',
        compute='_compute_tags',
        inverse='_set_tags',
        store=True
    )

class ProductProduct(models.Model):
    _inherit = 'product.product'

    process = fields.Char(
        string='Process',
        index=True
    )

