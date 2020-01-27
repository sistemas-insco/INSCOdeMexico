# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _


class SaleOrderReport(models.AbstractModel):
    _name = 'report.sale.report_saleorder'
    _description = 'Sale Order Report'

    def get_bank(self, company):
        banks = company.partner_id.bank_ids
        value = {
            'bank': _('BBVA BANCOMER National Currency check'),
            'account': _('00452636417 CABLE 012180004526364176')
        }
        if banks:
            name = banks[0].bank_id and banks[0].bank_id.name or ''
            number = banks[0].acc_number
            value.update({'bank': name, 'account': number})
        return value

    @api.model
    def _get_report_values(self, docids, data=None):
        # self.format_date(self.env['sale.order'].browse(docids[0]).date_order.strftime('%Y/%M/%d'))
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': self.env['sale.order'].browse(docids),
            'get_bank': self.get_bank,
        }
