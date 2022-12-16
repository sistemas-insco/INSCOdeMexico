# -*- coding: utf-8 -*-

from odoo import models, fields, api


class 	fleetvehicle(models.Model):
	_inherit = 'fleet.vehicle'

	# Exterior del carro
	luces_flete = fields.Char('Luces',tracking = True)
	antena_flete = fields.Char('Antena', tracking = True)
	espejo1_flete = fields.Char('Espejo lateral derecho', tracking = True)
	espejo2_flete = fields.Char('Espejo lateral izquierdo', tracking = True)
	crsitales_flete = fields.Char('Cristales', tracking = True)
	emblema_flete = fields.Char('Emblema', tracking = True)
	llantas_flete = fields.Char('Numero de llantas', tracking = True)
	tapones_flete = fields.Char('Numero de tapones', tracking = True)
	tapon_flete = fields.Char('Tapon de gasolina', tracking = True)
	claxon_flete = fields.Char('Bocina de claxon', tracking = True)
	
	# Interior del carro
	tablero_flete = fields.Char('Instrumentos del tablero', tracking = True)
	calefaccion_flete = fields.Char('Calefacción', tracking = True)
	limp_parabrisas_flete = fields.Char('Limpia parabrisas', tracking = True)
	radio_flete = fields.Char('Radio', tracking = True)
	bocinas_flete = fields.Char('Bocinas', tracking = True)
	Encendedor_flete = fields.Char('Encendedor', tracking = True)
	retrovisor_flete = fields.Char('Espejo retrovisor', tracking = True)
	ceniceros_flete = fields.Char('Ceniceros', tracking = True)
	cinturo_seguridad_flete = fields.Char('Cinturones de seguridad', tracking = True)
	botones_flete = fields.Char('Botones interioires', tracking = True)
	manijas_flete = fields.Char('Manijas de interiories', tracking = True)
	# Acesorios 
	tapetes_flete = fields.Char('Tapetes', tracking = True)
	vestidura_flete = fields.Char('Vestidura', tracking = True)
	gato_flete = fields.Char('Maneral y gato', tracking = True)
	llave_flete = fields.Char('LLaves de ruedas', tracking = True)
	herramientas_flete = fields.Char('Estuche de herramientas', tracking = True)
	reflejantes_flete = fields.Char('Reflejantes', tracking = True)
	llanta_ref_flete = fields.Char('LLanta de refacción', tracking = True)
	extinguidor_flete = fields.Char('Extinguidor', tracking = True)

	# Documentacion
	tajeta_flete = fields.Char('Tarjeta de circulación', tracking = True)
	seguro_flete = fields.Char('Papeles de seguro', tracking = True)
	verificacion_flete = fields.Char('Comprobante de verificación', tracking = True)
	
	# Datos iniciales y finales 
	Odometro_Finals_flete = fields.Char('Odómetro Final', tracking = True)
	Gasolina_Inicial_flete = fields.Char('Gasolina Inicial', tracking = True)
	Gasolina_Final_flete = fields.Char('Gasolina Final', tracking = True)
	Observaciones_flete = fields.Char('Observaciones', tracking = True)
	date1_field = fields.Date('Fecha de Entrega', tracking = True)
	date2_field = fields.Date('Fecha de recepcion',tracking = True)
	destino_field = fields.Char('Destino',tracking = True)

	#Condiciones del Motor
	anticongelante_flete = fields.Char('Refrigerante',tracking = True)
	liq_frenos_flete = fields.Char('Liquido de frenos',tracking = True)
	aceite_motor_flete =fields.Char('Aceite del motor',tracking = True)

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
