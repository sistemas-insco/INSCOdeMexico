from datetime import date
from odoo import models, fields, api,exceptions, _


class vacaciones(models.Model):
	_name = 'solicitud.vacaciones'
	_description = 'Solicitud'
	_inherit = ['mail.thread', 'mail.activity.mixin']



	name = fields.Char('Periódo',default='Periódo', tracking=True,required=True)
	empleado_id = fields.Many2one('hr.employee',tracking=True, string="Empleado", required=True)
	usuario_responsable=fields.Many2one(string="Responsable", related = 'empleado_id.parent_id')
	user_id = fields.Many2one('res.users', string='Usuario', index=True, tracking=True, default=lambda self: self.env.user)
	fecha_inicio = fields.Date(string="Fecha de Inicio", tracking=True, required=True)
	fecha_fin = fields.Date(string="Fecha Final", tracking=True, required=True)
	departamento_id = fields.Many2one(string='Departamento', related = 'empleado_id.department_id', store = True)
	numero_dias_solicitaso =fields.Integer(string="Días solicitados",  tracking=True, required=True)
	dias_vacaciones = fields.Integer(string="Días de Vacaciones", related = 'empleado_id.vacaciones_dias')
	descripcion_solicitud = fields.Text(string="Descripción")
	active = fields.Boolean('Active', default=True, tracking=True)
	
	state = fields.Selection([
										('nuevo', 'Nuevo'),
										('por aprobar', 'Por aprobar'),
										('aprobado', 'Aprobado'),
										('cancelado', 'Cancelado')],
										default='nuevo', string="Estado",tracking=True,copy=False)

	solicitud_tipo =fields.Selection([
												('vacaciones', 'Vacaciones'),
												('incapacidad', 'Incapacidad'),
												('permiso', 'Permiso'),
												('reposicion', 'Reposición'),
												('dia por dia', 'Dia por dia'),
												('otro', 'Otro')],
												string="Tipo de Solicitud", tracking=True)



	@api.constrains('numero_dias_solicitaso')
	def _validacion_numero_dias_solicitados(self):
		if self.numero_dias_solicitaso <= 0:
			raise exceptions.ValidationError('El número de días solicitados no puede ser menor o igual a 0 ')

		if self.solicitud_tipo == 'vacaciones':
			if self.numero_dias_solicitaso > self.dias_vacaciones or self.dias_vacaciones == 0:
				raise exceptions.ValidationError('El número de días solicitados es mayor a los días disponibles o no tienes días de vacaciones')





	#@api.multi
	# def solictud_aprovada(self):
	# 	if self.user_has_groups('i_add_field_empleados_vacaciones.group_vacaiones_manager'):
	# 			self.write({'state': 'aprobado'})
	# 	if self.solicitud_tipo == 'vacaciones':
	# 		if self.numero_dias_solicitaso > self.dias_vacaciones:
	# 			raise exceptions.ValidationError('El número de días solicitados es mayor a los días disponibles o no tienes días de vacaciones')
	# 		else:
	# 			self.empleado_id.vacaciones_dias = self.dias_vacaciones - self.numero_dias_solicitaso


	def solictud_aprovada(self):
	    # Validar permisos
		if not self.env.user.has_group('i_add_field_empleados_vacaciones.group_vacaiones_manager'):
			raise exceptions.AccessError("No tienes permisos para aprobar esta solicitud.")

	    # Validación de días si es solicitud de vacaciones
		if self.solicitud_tipo == 'vacaciones':
			if self.numero_dias_solicitaso > self.dias_vacaciones:
				raise exceptions.ValidationError("El número de días solicitados es mayor a los días disponibles o no tienes días de vacaciones.")
			else:
				self.empleado_id.vacaciones_dias = self.dias_vacaciones - self.numero_dias_solicitaso
	    # Cambiar estado solo si la validación pasó
		self.write({'state': 'aprobado'})

	    # Registrar acción en el chatter (opcional)
		self.message_post(body=f"Solicitud aprobada por {self.env.user.name}")




	#@api.multi
	# def solictud_cancelada(self):
	# 	if self.user_has_groups('i_add_field_empleados_vacaciones.group_vacaiones_manager'):
	# 			self.write({'state': 'cancelado'})

	def solictud_cancelada(self):
	        # Validar permisos
			if not self.env.user.has_group('i_add_field_empleados_vacaciones.group_vacaiones_manager'):
				raise exceptions.AccessError("No tienes permisos para cancelar esta solicitud.")

	        # Cambiar estado
			self.write({'state': 'cancelado'})




	def action_solicitud_send(self):
    #Abre el asistente para enviar correo con la plantilla de solicitud de vacaciones
		self.ensure_one()

		lang = self.env.context.get('lang')
		template = self.env.ref('i_add_field_empleados_vacaciones.solicitud_card_email_template',raise_if_not_found=False)

		ctx = {
			'default_model': 'solicitud.vacaciones',
			'default_res_ids': self.ids,  # en v18 sí se usa plural
			'default_composition_mode': 'comment',
			'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
			'email_notification_allow_footer': True,
			'proforma': self.env.context.get('proforma', False),
			}

    # --- Para registro único ---
		ctx.update({
			'force_email': True,
			'model_description': self.with_context(lang=lang).name or 'Solicitud',})

    # --- Cargar plantilla si existe ---
		if template:
			ctx.update({
				'default_template_id': template.id,
				'mark_so_as_sent': True,
			})
			if template.lang:
				lang = template._render_lang(self.ids)[self.id]

    # --- Cambiar estado si está en nuevo ---
		if self.state == 'nuevo':
			self.write({'state': 'por aprobar'})

		action = {
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(False, 'form')],
			'view_id': False,
			'target': 'new',
			'context': ctx,
		}

    # Si la empresa no tiene layout configurado (igual que sale.order)
		if (
			self.env.context.get('check_document_layout')
			and not self.env.context.get('discard_logo_check')
			and self.env.is_admin()
			and not self.env.company.external_report_layout_id
		):
			layout_action = self.env['ir.actions.report']._action_configure_external_report_layout(action)
			action.pop('close_on_report_download', None)
			layout_action['context']['dialog_size'] = 'extra-large'
			return layout_action

		return action


