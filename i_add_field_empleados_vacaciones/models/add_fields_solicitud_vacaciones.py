from datetime import date
from odoo import models, fields, api,  _


class vacaciones(models.Model):
	_name = 'solicitud.vacaciones'
	_description = 'Solictud de Vacaciones'
	_inherit = ['mail.thread', 'mail.activity.mixin']


	# @api.model
	# def _default_empleado_id(self):
	# 	return self.env['res.users'].search([('name', '=', self.env.uid)], limit=1)
	
	#empleado_id = fields.Many2one('hr.employee',track_visibility="always", string='Empleado', default=_default_empleado_id)
	name = fields.Char('Periódo',default='Periódo 2021', required=True)
	empleado_id = fields.Many2one('hr.employee',track_visibility="always", string="Empleado", required=True)
	usuario_responsable=fields.Many2one("hr.employee", string="Responsable", required=True)
	user_id = fields.Many2one('res.users', string='Usuario', required=True)
	fecha_inicio = fields.Date(string="Fecha de Inicio", track_visibility="always", required=True)
	fecha_fin = fields.Date(string="Fecha Final", track_visibility="always", required=True)
	departamento_id = fields.Many2one('hr.department', string="Departamento")
	numero_dias_solicitaso =fields.Integer(string="Días solicitados",  track_visibility="always", required=True)
	numero_dias_restantes = fields.Integer(string="Días restantes", track_visibility="always")
	dias_vacaciones = fields.Integer(string="Días de Vacaciones", related = 'empleado_id.vacaciones_dias', store = True)
	
	state = fields.Selection([
										('nuevo', 'Nuevo'),
										('en proceso', 'En Proceso'),
										('aprobado', 'Aprobado'),
										('cancelado', 'Cancelado')],
										default='nuevo', string="Estado",track_visibility="always")

	solicitud_tipo =fields.Selection([('vacaciones', 'Vacaciones'), ('incapacidad', 'Incapacidad'),('permiso', 'Permiso'), ('reposicion', 'Reposición'),('otro', 'Otro')], string="Tipo de Solicitud", track_visibility="always")


	@api.multi
	def solictud_aprovada(self):
		self.write({'state': 'aprobado'})


	@api.onchange('numero_dias_solicitaso','solicitud_tipo')
	def dia_vacaiones_restantes(self):
		if self.solicitud_tipo == 'vacaciones':
			self.numero_dias_restantes = self.dias_vacaciones - self.numero_dias_solicitaso


	# @api.onchange('típo_solicitud')
	# def tipo_vacaciones(self):
	# 	if típo_solicitud == 'vacaciones'
	# 		dias_vacaciones = dias_vacaciones = fields.Integer(related = 'empleado_id.vacaciones_dias')