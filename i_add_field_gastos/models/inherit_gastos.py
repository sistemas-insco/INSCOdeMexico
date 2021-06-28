# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GastosUsuario(models.Model):
	_inherit = 'hr.expense'


	proveedor_id = fields.Many2one('res.partner', string='Proveedor')
	fecha_pago_id = fields.Date(string='Fecha de pago', track_visibility="always")
	purchase_order_id = fields.Many2one('purchase.order', string='Orden de Compra')
	sucursal_id = fields.Selection([('Insco de Mexico:', 'Insco de Mexico:'), ('Insco Guadalajara:', 'Insco Guadalajara:'), ('Insco Merida:', 'Insco Merida:'), ('Insco Bajio:', 'Insco Bajios:')],
        string='Sucursal')
	diferencia_id = fields.Monetary(string='Diferencia', track_visibility="always")