# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError


class tiketComputer(models.Model):
	_name = "team.computer_tiket"
	_description = "Ticket"
	_inherit = ['mail.thread', 'mail.activity.mixin']


	name= fields.Char(string='N° Ticket', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
	descripcion_falla = fields.Text(string='Descripción de la falla', tracking = True)
	descripcion_conclucion = fields.Text(string='Conclusión de la falla', tracking = True)
	fecha_mantenimiento = fields.Datetime(string='Fecha de mantenimiento', tracking = True)
	equipo_id = fields.Many2one("team.computer",string="Equipo")
	departamento_id = fields.Many2one('hr.department', string='Departamento',tracking = True)
	user_id = fields.Many2one('res.users', string='Usuario', index=True, tracking = True, default=lambda self: self.env.user)
	comentarios_calificacion = fields.Text(string='Comentarios', tracking = True)
	active = fields.Boolean('Active', default=True, tracking=True)

	calificacion = fields.Selection(		[('no hay calificacion', 'no hay calificación'),
											('muy insatisfecho', 'muy insatisfecho'),
											('no satisfecho', 'no satisfecho'),
											('satisfecho', 'satisfecho')],
											default='no hay calificacion',string='Calificación', tracking = True)


	estado_tipo =fields.Selection(			[('nuevo', 'Nuevo'),
											('enviado', 'Enviado'),
											('abierto', 'Abierto'),
											('cerrado', 'Cerrado')], 
											string="Estado",default='nuevo', copy=False, tracking = True)


	tipo_servicio = fields.Selection(		[('Preventivo', 'Preventivo'), 
											('Correctivo', 'Correctivo'),
											('solicitud de equipo', 'Solicitud de Equipo'),], 
											string='Tipo de Mantenimiento', tracking = True)





	# @api.model
	# def create(self, vals):
	# 		if vals.get('name', _('New')) == _('New'):
	# 			vals['name'] = self.env['ir.sequence'].next_by_code('team.computer_tiket.sequence') or _('New')
	# 		result= super(tiketComputer, self).create(vals)
	# 		return result

	@api.model_create_multi
	def create(self, vals_list):
		for vals in vals_list:
			if vals.get('name', _('New')) == _('New'):
				vals['name'] = self.env['ir.sequence'].next_by_code('team.computer_tiket.sequence') or _('New')
		result = super(tiketComputer, self).create(vals_list)
		return result


	def solictud_abierto(self):
			self.write({'estado_tipo': 'abierto'})

	def solictud_cerrado(self):
			self.write({'estado_tipo': 'cerrado'})

	# def solictud_cerrado_todos(self):
	# 	for record in self:
	# 		record.write({'estado_tipo': 'cerrado'})


#action_quotation_send
#action_quotation_sent

	def action_ticket_send(self):
    #Abre el asistente de envío de correo para tickets del área de sistemas
		self.ensure_one()

		lang = self.env.context.get('lang')
		template = self.env.ref('i_ticktes_invetario_sistemas.tikcet_card_email_template',raise_if_not_found=False)

		ctx = {
			'default_model': 'team.computer_tiket',
			'default_res_ids': self.ids,  # en v18 sí se usa plural
			'default_composition_mode': 'comment',
			'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
			'email_notification_allow_footer': True,
			'proforma': self.env.context.get('proforma', False),
			}

    # --- Para registro único ---
		ctx.update({
			'force_email': True,
			'model_description': self.with_context(lang=lang).name or 'Ticket',})

    # --- Cargar plantilla si existe ---
		if template:
			ctx.update({
				'default_template_id': template.id,
				'mark_so_as_sent': True,
			})
			if template.lang:
				lang = template._render_lang(self.ids)[self.id]

    # --- Cambiar estado si está en nuevo ---
		if self.estado_tipo == 'nuevo':
			self.write({'estado_tipo': 'enviado'})

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