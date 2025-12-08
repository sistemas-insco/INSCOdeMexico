# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _


class AccountInvoiceReport(models.AbstractModel):
    _name = 'report.account.report_invoice_with_payments'
    _description = 'Account Invoice Report'

    def get_pac_name(self, invoice):
        pacs = dict(self.env['res.company']._fields[
            'l10n_mx_edi_pac'].selection)
        return pacs.get(invoice.company_id.l10n_mx_edi_pac) or False

    def get_pac_rfc(self, invoice):
        pac_rfc = False
        if self.get_pac_name(invoice):
            pac_rfc = 'FIN1203015JA' if invoice.company_id.l10n_mx_edi_pac == 'finkok' else 'SFE0807172W8'
        return pac_rfc

    def get_addr(self, partner):
        return '%s %s %s, %s, %s, %s' % (
            partner.street or '',
            # partner.street_number or '',
            # partner.street_number2 or '',
            #partner.l10n_mx_edi_locality or '',
            partner.l10n_mx_edi_colony and
            'COL. %s' % partner.l10n_mx_edi_colony or '',
            partner.zip and
            'C.P. %s' % partner.zip or '',
            partner.city or '',
            partner.state_id and
            '%s' % partner.state_id.name or '',
            partner.country_id and partner.country_id.name or ''
        )



    def get_taxes(self, line):
        result = []
        if not line.tax_ids:
            return result

        taxes = line.tax_ids.compute_all(
            price_unit=line.price_unit,
            quantity=line.quantity,
            product=line.product_id,
            partner=line.move_id.partner_id,
            currency=line.move_id.currency_id
        )['taxes']

        for tax in taxes:
            result.append((tax['name'], tax['amount']))

        return result

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': self.env['account.move'].browse(docids),
            'get_addr': self.get_addr,
            'get_taxes': self.get_taxes,
            'get_pac_name': self.get_pac_name,
            'get_pac_rfc': self.get_pac_rfc,
        }

