from datetime import date
from odoo import models, fields, api


class VacacionesId(models.Model):
	_inherit = 'hr.employee'



	fecha_ingreso = fields.Date(string="Fecha ingreso", track_visibility="always", groups="hr.group_hr_user")
	vacaciones_dias = fields.Integer(string="Dias de Vacaciones",default='6', track_visibility="always", groups="hr.group_hr_user")

	polo_cruzada = fields.Char(string ='Polo Cruzada',help='(TODOS)', groups="hr.group_hr_user")
	camisa_manga_larga = fields.Char(string ='Camisa manga larga',help='(TODOS)', groups="hr.group_hr_user")
	camisola_circuito = fields.Char(string ='Camisola circuito',help='(LABS Y LOGÍSTICA)', groups="hr.group_hr_user")
	bata_de_asistencia = fields.Char(string ='Bata de asistencia',help='(MANTENIMIENTO)', groups="hr.group_hr_user")
	chamarra = fields.Char(string ='Chamarra',help='(TODOS)', groups="hr.group_hr_user")
	pantalon_ejecutivo = fields.Char(string ='Pantalón ejecutivo',help='(ADMINISTRATIVOS)', groups="hr.group_hr_user")
	pantalon_cargo = fields.Char(string ='Pantalón Cargo',help='(LABORATORIOS, LOGÍSTICA, y MANTENIMIENTO)', groups="hr.group_hr_user")
	botas_calzado_seguridad = fields.Char(string ='Botas y/o Calzado de Seguridad',help='(TODOS)', groups="hr.group_hr_user")

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
										default='1', track_visibility="always",string='Años de antiguedad',groups="hr.group_hr_user")
	


	# @api.onchange('años_antiguedad')
	# def dias_vacaciones_retantes(self):
	# 	self.dias_vacaciones_restantes = vacaciones_dias


	@api.onchange('años_antiguedad')
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