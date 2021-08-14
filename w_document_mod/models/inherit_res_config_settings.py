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
from odoo import api, fields, models
from odoo.tools.translate import _



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    terms_file = fields.Binary(
        string='File Content',
        attachment=True)
    filename_terms = fields.Char()

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        default_filename_terms = get_param(
            'w_document_mod.filename_terms')
        default_terms_file = get_param(
            'w_document_mod.terms_file')
        if not default_terms_file:
            default_terms_file = False
        res.update(
            terms_file=default_terms_file,
            filename_terms=default_filename_terms)
        return res

    #@api.multi
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        # we store the repr of the values, since the value of the parameter is a required string
        set_param('w_document_mod.terms_file', self.terms_file)
        set_param('w_document_mod.filename_terms', self.filename_terms)
        return res

