# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2019 Wedoo - https://wedoo.tech
# All Rights Reserved.
#
# Developer(s): Alan Guzmán
#               (age@wedoo.tech)
########################################################################
#
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
import base64

CFDI_XSLT_CADENA_TFD = 'l10n_mx_edi/data/xslt/3.3/cadenaoriginal_TFD_1_1.xslt'


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    observations = fields.Text(
        string='Observations'
    )
    sello_cfdi = fields.Char(
        compute="_compute_cfdi_values",
        store=True
    )
    sello_sat = fields.Char(
        compute="_compute_cfdi_values",
        store=True
    )
    cfdi_cadena = fields.Char(
        compute='_compute_cfdi_values',
        store=True
    )
    payment_method = fields.Char(
        compute="_compute_cfdi_values",
        store=True
    )

    serial_number = fields.Char(compute='_compute_cfdi_values',
        store=True)

    @api.model
    def _get_l10n_mx_edi_cadena(self):
        self.ensure_one()
        # get the xslt path
        xslt_path = CFDI_XSLT_CADENA_TFD
        # get the cfdi as eTree
        try:
            cfdi = base64.decodestring(self.l10n_mx_edi_cfdi)
            cfdi = self.l10n_mx_edi_get_xml_etree(cfdi)
            cfdi = self.l10n_mx_edi_get_tfd_etree(cfdi)
            return self.l10n_mx_edi_generate_cadena(xslt_path, cfdi)
        except Exception as e:
            print(e)
        # return the cadena

    #@api.multi
    """
    @api.depends('l10n_mx_edi_cfdi_name')
    def _compute_cfdi_values(self):
        #'''Fill the invoice fields from the cfdi values.
        #'''
        for record  in self:
            attachment_id = record .l10n_mx_edi_retrieve_last_attachment()
            if not attachment_id:
                continue
            # At this moment, the attachment contains the file size in its 'datas' field because
            # to save some memory, the attachment will store its data on the physical disk.
            # To avoid this problem, we read the 'datas' directly on the disk.
            datas = attachment_id._file_read(attachment_id.store_fname)
            record .l10n_mx_edi_cfdi = datas
            cfdi = base64.b64decode(datas).replace( # se acambio de base64.decodestring  a  base64.b64encode#
                b'xmlns:schemaLocation', b'xsi:schemaLocation')
            tree = record .l10n_mx_edi_get_xml_etree(cfdi)
            # if already signed, extract uuid
            tfd_node = record .l10n_mx_edi_get_tfd_etree(tree)

            if tfd_node is not None:
                record .l10n_mx_edi_cfdi_uuid = tfd_node.get('UUID')
                record .sello_sat = tfd_node.get('SelloSAT', '')
                record .l10n_mx_edi_cfdi_amount = tree.get('Total', tree.get('total'))
                record .l10n_mx_edi_cfdi_supplier_rfc = tree.Emisor.get('Rfc', tree.Emisor.get('rfc'))
                record .l10n_mx_edi_cfdi_customer_rfc = tree.Receptor.get('Rfc', tree.Receptor.get('rfc'))

                certificate = tree.get('noCertificado', tree.get('NoCertificado'))
                record .l10n_mx_edi_cfdi_certificate_id = self.env['l10n_mx_edi.certificate'].sudo().search([('serial_number', '=', 'certificate')], limit=1)
                record .sello_cfdi = tree.get('sello', tree.get('Sello', 'No identificado'))
                cfdi_cadena = record ._get_l10n_mx_edi_cadena()
                record .cfdi_cadena = cfdi_cadena if cfdi_cadena else ''
                record .payment_method = tree.get('MetodoPago', '')
    """

    @api.depends('l10n_mx_edi_cfdi_name')
    def _compute_cfdi_values(self):
        res = super(AccountInvoice, self)._compute_cfdi_values()
        for record in self:
            attachment_id = record.l10n_mx_edi_retrieve_last_attachment()
            if not attachment_id:
                continue
            # At this moment, the attachment contains the file size in its 'datas' field because
            # to save some memory, the attachment will store its data on the physical disk.
            # To avoid this problem, we read the 'datas' directly on the disk.
            datas = attachment_id._file_read(attachment_id.store_fname)
            record.l10n_mx_edi_cfdi = datas
            cfdi = base64.b64decode(datas).replace(  # se acambio de base64.decodestring  a  base64.b64encode#
                b'xmlns:schemaLocation', b'xsi:schemaLocation')
            tree = record.l10n_mx_edi_get_xml_etree(cfdi)
            # if already signed, extract uuid
            tfd_node = record.l10n_mx_edi_get_tfd_etree(tree)
            if tfd_node is not None:
                record.l10n_mx_edi_cfdi_uuid = tfd_node.get('UUID')
                record.sello_sat = tfd_node.get('SelloSAT', '')
                record.l10n_mx_edi_cfdi_amount = tree.get('Total', tree.get('total'))
                record.l10n_mx_edi_cfdi_supplier_rfc = tree.Emisor.get('Rfc', tree.Emisor.get('rfc'))
                record.l10n_mx_edi_cfdi_customer_rfc = tree.Receptor.get('Rfc', tree.Receptor.get('rfc'))

                certificate = tree.get('noCertificado', tree.get('NoCertificado'))
                #record.l10n_mx_edi_cfdi_certificate_id = self.env['l10n_mx_edi.certificate'].sudo().search(                
                #    [('serial_number', '=', 'certificate')], limit=1)
                record.serial_number = certificate
                record.sello_cfdi = tree.get('sello', tree.get('Sello', 'No identificado'))
                cfdi_cadena = record._get_l10n_mx_edi_cadena()
                record.cfdi_cadena = cfdi_cadena if cfdi_cadena else ''
                record.payment_method = tree.get('MetodoPago', '')
        return res
