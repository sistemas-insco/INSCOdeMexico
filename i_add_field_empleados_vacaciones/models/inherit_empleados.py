from datetime import date
from odoo import models, fields, api


class VacacionesId(models.Model):
	_inherit = 'hr.employee'



	fecha_ingreso = fields.Date(string="Fecha ingreso", tracking=True, groups="hr.group_hr_user")
	vacaciones_dias = fields.Integer(string="Dias de Vacaciones",default='6', tracking=True, groups="hr.group_hr_user")

	polo_cruzada = fields.Char(string ='Polo Cruzada',help='(TODOS)', groups="hr.group_hr_user")
	camisa_manga_larga = fields.Char(string ='Camisa manga larga',help='(TODOS)', groups="hr.group_hr_user")
	camisola_circuito = fields.Char(string ='Camisola circuito',help='(LABS Y LOGÍSTICA)', groups="hr.group_hr_user")
	bata_de_asistencia = fields.Char(string ='Bata de asistencia',help='(MANTENIMIENTO)', groups="hr.group_hr_user")
	chamarra = fields.Char(string ='Chamarra',help='(TODOS)', groups="hr.group_hr_user")
	pantalon_ejecutivo = fields.Char(string ='Pantalón ejecutivo',help='(ADMINISTRATIVOS)', groups="hr.group_hr_user")
	pantalon_cargo = fields.Char(string ='Pantalón Cargo',help='(LABORATORIOS, LOGÍSTICA, y MANTENIMIENTO)', groups="hr.group_hr_user")
	botas_calzado_seguridad = fields.Char(string ='Botas y/o Calzado de Seguridad',help='(TODOS)', groups="hr.group_hr_user")

	anios_antiguedad = fields.Selection([
										('1', '1'),
										('2', '2'),
										('3', '3'),
										('4', '4'),
										('5', '5'),
										('6', 'De 6 a 10 años'),
										('7', 'De 11 a 15 años'),
										('8', 'De 16 a 20 años'),
										('9', 'De 21 a 25 años'),
										('10', 'De 26 a 30 años'),
										('11', 'De 31 a 35 años')],
										default='1', tracking=True,string='Años de antiguedad',groups="hr.group_hr_user")



	@api.onchange('anios_antiguedad')
	def _asignacion_dias_vacaciones(self):
		if self.anios_antiguedad == '1':
			self.vacaciones_dias= 12
		if self.anios_antiguedad == '2':
			self.vacaciones_dias= 14
		if self.anios_antiguedad == '3':
			self.vacaciones_dias= 16
		if self.anios_antiguedad == '4':
			self.vacaciones_dias= 18
		if self.anios_antiguedad == '5':
			self.vacaciones_dias= 20
		if self.anios_antiguedad == '6': #('6', 'De 6 a 10 años')
			self.vacaciones_dias= 22
		if self.anios_antiguedad == '7': #('7', 'De 11 a 15 años')
			self.vacaciones_dias= 24
		if self.anios_antiguedad == '8': #('8', 'De 16 a 20 años')
			self.vacaciones_dias= 26
		if self.anios_antiguedad == '9': #('9', 'De 21 a 25 años')
			self.vacaciones_dias= 28
		if self.anios_antiguedad == '10': #('10', 'De 26 a 30 años')
			self.vacaciones_dias= 30
		if self.anios_antiguedad == '11': #('11', 'De 31 a 35 años')
			self.vacaciones_dias= 32