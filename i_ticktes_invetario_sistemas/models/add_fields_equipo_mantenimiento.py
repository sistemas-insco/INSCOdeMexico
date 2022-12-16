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





	@api.model
	def create(self, vals):
			if vals.get('name', _('New')) == _('New'):
				vals['name'] = self.env['ir.sequence'].next_by_code('team.computer_tiket.sequence') or _('New')
			result= super(tiketComputer, self).create(vals)
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
		self.ensure_one()
		template_id = self.env.ref('i_ticktes_invetario_sistemas.tikcet_card_email_template').id
		#template_id = self._find_mail_template()
		lang = self.env.context.get('lang')
		template = self.env['mail.template'].browse(template_id)
		if template.lang:
			lang = template._render_template(template.lang, 'team.computer_tiket', self.ids[0])
		ctx = {
			'default_model': 'team.computer_tiket',
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
		if self.estado_tipo == 'nuevo':
			self.write({'estado_tipo': 'enviado'})
		return {
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(False, 'form')],
			'view_id': False,
			'target': 'new',
			'context': ctx,
        }