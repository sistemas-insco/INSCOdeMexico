from odoo import models, fields, api
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_payment_term_id = fields.Many2one(
        'account.payment.term',
        tracking=True
    )