# -*- coding: utf-8 -*-
#import datetime
from odoo import models, fields, api, _


class customComputer(models.Model):
	_name = "team.computer"
	_description = "Equipo"
	_inherit = ['mail.thread', 'mail.activity.mixin']


	
	name= fields.Char(string='N° Inventario', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
	num_inventario_area = fields.Char(string="N° Inventario del área")
	modelo = fields.Char(string='Modelo',tracking = True)
	marca = fields.Char(string='Marca')
	numero_serie = fields.Char(string='Número de Serie')
	direccion_mac = fields.Char(string='Dirección MAC')
	direccion_ip = fields.Char(string='Dirección IP')
	kay_office = fields.Text(string='Office Kay')
	kay_windows = fields.Text(string='Windows Kay')
	usuario_pc = fields.Char(string='Usuario')
	password_pc = fields.Text(string='Password')
	descripcion = fields.Text(string='Descripción')
	notas_entrega = fields.Text(string='Notas de entrega de equipo')
	fecha_assignment = fields.Date(string='Fecha de asignación', tracking=True)
	empleado_id = fields.Many2one('hr.employee', string='Empleado',tracking=True)
	departamento_id = fields.Many2one(string='Departamento', related = 'empleado_id.department_id', store = True)
	# departamento_id = fields.Many2one('hr.department', string='Departamento')
	image = fields.Binary(string="Equipo Imagen")
	active = fields.Boolean('Active', default=True, tracking=True)


	estado = fields.Selection(					[('En opereacion', 'En operación'),
												('fuera de uso', 'Fuera de uso'),
												('renta', 'Renta')],
												string='Estado del equipo', tracking=True)


	sucursal_id = fields.Selection(				[('insco de Mexico', 'INSCO de México'),
												('insco Guadalajara', 'INSCO Guadalajara'),
												('insco Merida', 'INSCO Mérida'),
												('Insco Bajio:', 'INSCO Bajío')],
												string='Sucursal')


	sistemas_operativo = fields.Selection(		[('otro', 'Otro'),
												('Windows 98', 'Windows 98'),
												('Windows XP', 'Windows XP'),
												('Windows 7', 'Windows 7'),
												('Windows 8.1', 'Windows 8.1'),
												('Windows 10', 'Windows 10'),
												('Windows 11', 'Windows 11'),
												('Windows 12', 'Windows 12')],
												string='Sistema operativo',tracking=True)


	office_tipo = fields.Selection(				[('n/a', 'n/a'),
												('Office 2010', 'Office 2010'),
												('Office 2013', 'Office 2013'),
												('Office 2016', 'Office 2016'),
												('Office 2019', 'Office 2019'),
												('Office 2020', 'Office 2020'),
												('Office 2021', 'Office 2021'),
												('Office 2022', 'Office 2022'),
												('Office 365', 'Office 365')],
												string='Tipo de Office')


	tipo_equipo = fields.Selection(				[('AP', 'AP'),('DVR', 'DVR'),
												 ('Conmutador', 'Conmutador'),
												 ('Impresora', 'Impresora'),
												 ('Servidor', 'Servidor'),
												 ('Laptop', 'Laptop'),
												 ('PC de escritorio', 'PC de escritorio'),
												 ('Telefono IP', 'Teléfono IP'),
												 ('Telefono Celular', 'Teléfono Celular'),
												 ('Router', 'Router'),
												 ('Switch', 'Switch'),
												 ('Monitor', 'Monitor'),
												 ('Proyector', 'Proyector'),
												 ('Dispocitivo', 'Dispositivo')],
												 string='Tipo de Equipo')







	@api.model
	def create(self,vals):
			if vals.get('name', _('New')) == _('New'):
				vals['name'] = self.env['ir.sequence'].next_by_code('team.computer.sequence') or _('New')
			result= super(customComputer, self).create(vals)
			return result