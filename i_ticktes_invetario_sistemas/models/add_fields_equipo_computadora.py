# -*- coding: utf-8 -*-
#import datetime
from odoo import models, fields, api, _


class customComputer(models.Model):
	_name = "team.computer"
	_description = "Equipo"
	_inherit = ['mail.thread', 'mail.activity.mixin']


	
	name= fields.Char(string='N° Inventario', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
	num_inventario_area = fields.Char(string="N° Inventario del área")
	tipo_equipo = fields.Selection([('Laptop', 'Laptop'), ('PC de escritorio', 'PC de escritorio'), ('Telefono IP', 'Teléfono IP'),('Telefono Celular', 'Teléfono Celular'), ('Router', 'Router'), ('Switch', 'Switch'), ('Monitor', 'Monitor'), ('Dispocitivo', 'Dispositivo')],
        string='Tipo de Equipo')
	modelo = fields.Char(string='Modelo',track_visibility="always")
	marca = fields.Char(string='Marca')
	numero_serie = fields.Char(string='Número de Serie')
	direccion_mac = fields.Char(string='Dirección MAC')
	direccion_ip = fields.Char(string='Dirección IP')
	office_tipo = fields.Selection([('n/a', 'n/a'), ('Office 2010', 'Office 2010'), ('Office 2013', 'Office 2013'), ('Office 2016', 'Office 2016'), ('Office 2019', 'Office 2019'), ('Office 2019', 'Office 2019'), ('Office 365', 'Office 365')],
        string='Tipo de Office')
	kay_office = fields.Text(string='Office Kay',password="True")
	kay_windows = fields.Text(string='Windows Kay',password="True")
	sistemas_operativo = fields.Selection([('otro', 'Otro'),('Windows 98', 'Windows 98'),('Windows XP', 'Windows XP'), ('Windows 7', 'Windows 7'), ('Windows 8.1', 'Windows 8.1'), ('Windows 10', 'Windows 10'), ('Windows 11', 'Windows 11')],
        string='Sistema operativo',track_visibility="always")
	usuario_pc = fields.Char(string='Usuario')
	password_pc = fields.Text(string='Password')
	descripcion = fields.Text(string='Descripción')
	notas_entrega = fields.Text(string='Notas de entrega de equipo')
	fecha_assignment = fields.Date(string='Fecha de asignación', track_visibility="always")
	empleado_id = fields.Many2one('hr.employee', string='Empleado',track_visibility="always")
	departamento_id = fields.Many2one(string='Departamento', related = 'empleado_id.department_id', store = True)
	# departamento_id = fields.Many2one('hr.department', string='Departamento')
	sucursal_id = fields.Selection([('insco de Mexico', 'INSCO de México'), ('insco Guadalajara', 'INSCO Guadalajara'), ('insco Merida', 'INSCO Mérida'), ('Insco Bajio:', 'INSCO Bajío')],
        string='Sucursal')
	estado = fields.Selection([('En opereacion', 'En operación'), ('fuera de uso', 'Fuera de uso'), ('renta', 'Renta')],string='Estado del equipo', track_visibility="always")
	image = fields.Binary(string="Equipo Imagen")


	@api.model
	def create(self,vals):
			if vals.get('name', _('New')) == _('New'):
				vals['name'] = self.env['ir.sequence'].next_by_code('team.computer.sequence') or _('New')
			result= super(customComputer, self).create(vals)
			return result