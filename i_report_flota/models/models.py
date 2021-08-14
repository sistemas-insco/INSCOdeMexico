# -*- coding: utf-8 -*-

from odoo import models, fields, api


class 	fleetvehicle(models.Model):
	_inherit = 'fleet.vehicle'

	# Exterior del carro
	luces_flete = fields.Char('Luces', track_visibility="always")
	antena_flete = fields.Char('Antena', track_visibility="always")
	espejo1_flete = fields.Char('Espejo lateral derecho', track_visibility="always")
	espejo2_flete = fields.Char('Espejo lateral izquierdo', track_visibility="always")
	crsitales_flete = fields.Char('Cristales', track_visibility="always")
	emblema_flete = fields.Char('Emblema', track_visibility="always")
	llantas_flete = fields.Char('Numero de llantas', track_visibility="always")
	tapones_flete = fields.Char('Numero de tapones', track_visibility="always")
	tapon_flete = fields.Char('Tapon de gasolina', track_visibility="always")
	claxon_flete = fields.Char('Bocina de claxon', track_visibility="always")
	
	# Interior del carro
	tablero_flete = fields.Char('Instrumentos del tablero', track_visibility="always")
	calefaccion_flete = fields.Char('Calefacción', track_visibility="always")
	limp_parabrisas_flete = fields.Char('Limpia parabrisas', track_visibility="always")
	radio_flete = fields.Char('Radio', track_visibility="always")
	bocinas_flete = fields.Char('Bocinas', track_visibility="always")
	Encendedor_flete = fields.Char('Encendedor', track_visibility="always")
	retrovisor_flete = fields.Char('Espejo retrovisor', track_visibility="always")
	ceniceros_flete = fields.Char('Ceniceros', track_visibility="always")
	cinturo_seguridad_flete = fields.Char('Cinturones de seguridad', track_visibility="always")
	botones_flete = fields.Char('Botones interioires', track_visibility="always")
	manijas_flete = fields.Char('Manijas de interiories', track_visibility="always")
	# Acesorios 
	tapetes_flete = fields.Char('Tapetes', track_visibility="always")
	vestidura_flete = fields.Char('Vestidura', track_visibility="always")
	gato_flete = fields.Char('Maneral y gato', track_visibility="always")
	llave_flete = fields.Char('LLaves de ruedas', track_visibility="always")
	herramientas_flete = fields.Char('Estuche de herramientas', track_visibility="always")
	reflejantes_flete = fields.Char('Reflejantes', track_visibility="always")
	llanta_ref_flete = fields.Char('LLanta de refacción', track_visibility="always")
	extinguidor_flete = fields.Char('Extinguidor', track_visibility="always")

	# Documentacion
	tajeta_flete = fields.Char('Tarjeta de circulación', track_visibility="always")
	seguro_flete = fields.Char('Papeles de seguro', track_visibility="always")
	verificacion_flete = fields.Char('Comprobante de verificación', track_visibility="always")
	
	# Datos iniciales y finales 
	Odometro_Finals_flete = fields.Char('Odómetro Final', track_visibility="always")
	Gasolina_Inicial_flete = fields.Char('Gasolina Inicial', track_visibility="always")
	Gasolina_Final_flete = fields.Char('Gasolina Final', track_visibility="always")
	Observaciones_flete = fields.Char('Observaciones', track_visibility="always")
	date1_field = fields.Date('Fecha de Entrega', track_visibility="always")
	date2_field = fields.Date('Fecha de recepcion',track_visibility="always")
	destino_field = fields.Char('Destino',track_visibility="always")

	#Condiciones del Motor
	anticongelante_flete = fields.Char('Refrigerante',track_visibility="always")
	liq_frenos_flete = fields.Char('Liquido de frenos',track_visibility="always")
	aceite_motor_flete =fields.Char('Aceite del motor',track_visibility="always")

	#, track_visibility="always" Este parametro hace que el cambio del campo se registre en el histotico de odoo
	#lista1_flete = fields.Many2one('res.parner', string='lista de flota', index=True) sirve para traer una lista por ejemlpo la de los usuarios de odoo

	





# class i_report_flota(models.Model):
#     _name = 'i_report_flota.i_report_flota'
#     _description = 'i_report_flota.i_report_flota'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
