from datetime import datetime, time
from odoo import models, fields, api


class vacacionesId(models.Model):
	_inherit = 'hr.employee'


	vacaciones_dias = fields.Integer(string="Dias de Vacaciones", compute='_asignacion_dias_vacaciones',store=True, compute_sudo=False)
	fecha_ingreso = fields.Date(string="fecha ingreso", track_visibility="always")
	# edad = fields.Text(string='Edad', compute='_asignacion_dias_vacaciones2')

	años_antiguedad = fields.Selection([
										('1', '1'),
										('2', '2'),
										('3', '3'),
										('4', '4'),
										('de 5 a 9 años', 'De 5 a 9 años'),
										('de 10 a 14 años', 'De 10 a 14 años'),
										('de 15 a 19 años', 'De 15 a 19 años'),
										('de 20 a 24 años', 'De 20 a 24 años'),
										('de 25 a 29 años', 'De 25 a 29 años')],
										default='1', track_visibility="always",string='Años de antiguedad')
	


	@api.one
	@api.depends('años_antiguedad')
	def _asignacion_dias_vacaciones(self):
		if self.años_antiguedad == '1':
			self.vacaciones_dias= 6
		if self.años_antiguedad == '2':
			self.vacaciones_dias= 8
		if self.años_antiguedad == '3':
			self.vacaciones_dias= 10
		if self.años_antiguedad == '4':
			self.vacaciones_dias= 12
		if self.años_antiguedad == 'de 5 a 9 años':
			self.vacaciones_dias= 14
		if self.años_antiguedad == 'de 10 a 14 años':
			self.vacaciones_dias= 16
		if self.años_antiguedad == 'de 15 a 19 años':
			self.vacaciones_dias= 18
		if self.años_antiguedad == 'de 20 a 24 años':
			self.vacaciones_dias= 20
		if self.años_antiguedad == 'de 25 a 29 años':
			self.vacaciones_dias= 22

	# @api.one
	# @api.depends('fecha_ingreso')
	# def _asignacion_dias_vacaciones2(self):
	# 		dob = time.strptime(self.fecha_nacimiento,"%Y-%m-%d")
	# 		today = time.localtime()
	# 		edad_empleador = today.tm_year - dob.tm_year
	# 		if today.tm_mon < dob.tm_mon:
	# 			edad_empleador = edad_empleador - 1
	# 				self.edad = edad_empleador