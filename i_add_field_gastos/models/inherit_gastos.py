# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GastosUsuario(models.Model):
	_inherit = 'hr.expense'


	proveedor_id = fields.Many2one('res.partner', string='Proveedor')
	fecha_pago_id = fields.Date(string='Fecha de pago', tracking=True)
	# purchase_order_id = fields.Many2one('purchase.order', string='Orden de Compra')
	sucursal_id = fields.Selection([('Insco de Mexico:', 'Insco de Mexico:'), ('Insco Guadalajara:', 'Insco Guadalajara:'), ('Insco Merida:', 'Insco Merida:'), ('Insco Bajio:', 'Insco Bajio:')],
        string='Sucursal')
	diferencia_id = fields.Monetary(string='Diferencia', tracking=True)
	departamento_id = fields.Many2one(string='Departamento', related='employee_id.department_id')
	forma_pago = fields.Selection([('Transferencia:', 'Transferencia:'), ('Efectivo:', 'Efectivo:'), ('Tarjeta:', 'Tarjeta:')],
        string='Forma de pago')
	num_tarjeta_gasolina = fields.Char(string='N° Tarjeta Gasolina', help='Escribe los 4 ultimos digitos de tu tarjeta')
	num_tarjeta_business = fields.Char(string='N° Tarjeta business', help='Escribe los 4 ultimos digitos de tu tarjeta')