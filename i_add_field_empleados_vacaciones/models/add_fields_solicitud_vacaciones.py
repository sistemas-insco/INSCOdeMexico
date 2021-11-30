from datetime import date
from odoo import models, fields, api,exceptions, _


class vacaciones(models.Model):
	_name = 'solicitud.vacaciones'
	_description = 'Solicitud'
	_inherit = ['mail.thread', 'mail.activity.mixin']



	name = fields.Char('Periódo',default='Periódo', track_visibility="always",required=True)
	empleado_id = fields.Many2one('hr.employee',track_visibility="always", string="Empleado", required=True)
	usuario_responsable=fields.Many2one(string="Responsable", related = 'empleado_id.parent_id')
	user_id = fields.Many2one('res.users', string='Usuario', index=True, track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user)
	fecha_inicio = fields.Date(string="Fecha de Inicio", track_visibility="always", required=True)
	fecha_fin = fields.Date(string="Fecha Final", track_visibility="always", required=True)
	departamento_id = fields.Many2one(string='Departamento', related = 'empleado_id.department_id', store = True)
	numero_dias_solicitaso =fields.Integer(string="Días solicitados",  track_visibility="always", required=True, readonly=True, states={'nuevo': [('readonly', False)], 'por aprobar': [('readonly', False)]})
	dias_vacaciones = fields.Integer(string="Días de Vacaciones", related = 'empleado_id.vacaciones_dias')
	descripcion_solicitud = fields.Text(string="Descripción")
	active = fields.Boolean('Active', default=True, tracking=True)
	
	state = fields.Selection([
										('nuevo', 'Nuevo'),
										('por aprobar', 'Por aprobar'),
										('aprobado', 'Aprobado'),
										('cancelado', 'Cancelado')],
										default='nuevo', string="Estado",track_visibility="always",copy=False)

	solicitud_tipo =fields.Selection([
												('vacaciones', 'Vacaciones'),
												('incapacidad', 'Incapacidad'),
												('permiso', 'Permiso'),
												('reposicion', 'Reposición'),
												('dia por dia', 'Dia por dia'),
												('otro', 'Otro')],
												string="Tipo de Solicitud", track_visibility="always", readonly=True, states={'nuevo': [('readonly', False)], 'por aprobar': [('readonly', False)]})



	@api.constrains('numero_dias_solicitaso')
	def _validacion_numero_dias_solicitados(self):
		if self.numero_dias_solicitaso <= 0:
			raise exceptions.ValidationError('El número de días solicitados no puede ser menor o igual a 0 ')

		if self.solicitud_tipo == 'vacaciones':
			if self.numero_dias_solicitaso > self.dias_vacaciones or self.dias_vacaciones == 0:
				raise exceptions.ValidationError('El número de días solicitados es mayor a los días disponibles o no tienes días de vacaciones')





	#@api.multi
	def solictud_aprovada(self):
		if self.user_has_groups('i_add_field_empleados_vacaciones.group_vacaiones_manager'):
				self.write({'state': 'aprobado'})
		if self.solicitud_tipo == 'vacaciones':
			if self.numero_dias_solicitaso > self.dias_vacaciones:
				raise exceptions.ValidationError('El número de días solicitados es mayor a los días disponibles o no tienes días de vacaciones')
			else:
				self.empleado_id.vacaciones_dias = self.dias_vacaciones - self.numero_dias_solicitaso



	# @api.onchange('solicitud_tipo')
	# def dia_vacaiones_restantes(self):
	# 	if self.solicitud_tipo == 'vacaciones':
	# 		if self.numero_dias_solicitaso > self.dias_vacaciones or self.dias_vacaciones == 0:
	# 			raise exceptions.ValidationError('El número de días solicitados es mayor a los días disponibles o no tienes días de vacaciones')




	#@api.multi
	def solictud_cancelada(self):
		if self.user_has_groups('i_add_field_empleados_vacaciones.group_vacaiones_manager'):
				self.write({'state': 'cancelado'})

	

	def action_solicitud_send(self):
			self.ensure_one()
			template_id = self.env.ref('i_add_field_empleados_vacaciones.solicitud_card_email_template').id
			#template_id = self._find_mail_template()
			lang = self.env.context.get('lang')
			template = self.env['mail.template'].browse(template_id)
			if template.lang:
				lang = template._render_template(template.lang, 'solicitud.vacaciones', self.ids[0])
			ctx = {
				'default_model': 'solicitud.vacaciones',
				'default_res_id': self.ids[0],
				'default_use_template': bool(template_id),
				'default_template_id': template_id,
				'default_composition_mode': 'comment',
				'mark_so_as_sent': True,
				# 'custom_layout': "mail.mail_notification_paynow",
				'proforma': self.env.context.get('proforma', False),
				'force_email': True,
				'model_description': self.with_context(lang=lang).name,
			}
			if self.state == 'nuevo':
				self.write({'state': 'por aprobar'})
			return {
				'type': 'ir.actions.act_window',
				'view_mode': 'form',
				'res_model': 'mail.compose.message',
				'views': [(False, 'form')],
				'view_id': False,
				'target': 'new',
				'context': ctx,
			}


