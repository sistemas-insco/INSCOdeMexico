from odoo import models, fields, api


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'



    state1_id = fields.Many2one(
    	string='Entidad Federativa', related='partner_id.state_id', readonly=True)