# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Alan Guzmán
#               (age@tech.com)
########################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
from odoo import models, fields, api
import re
import html2text
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'


#------------------Campos de los documentos de recepcion, orden de servicio y entrega-------------------# 
  
    number_tags = fields.Integer(
        string='Number tags'
    )
    observations_report_equipment_reception = fields.Text(
        string='Observations report equipment reception',
        help='Observations for report reception equipment',
        tracking=True)

    conditions_report_service_order = fields.Text(
        string='Conditions report service order',
        help='Conditions for report service order',
        tracking=True
    )
    date_reception = fields.Date(
        string='Date reception',
        help='Fecha en la que el equipo llega a las instalaciones de INSCO de México',
        tracking=True
    )
    date_service_order = fields.Date(
        string='Date service order',
         help='Fecha en la que se realiza la orden de servicio',
        tracking=True
    )
    date_delivery = fields.Date(
        string='Date delivery',
        help='Fecha en la que el equipo sale de INSCO de México o se realiza la entrega al cliente',
        tracking=True
    )
    fecha_revision_cotizacion = fields.Date(
        string='FECHA DE REVISIÓN DE COTIZACION',
        help='Fecha en la que se revisa la cotización sin errores ',
        tracking=True
    )
    dias_entre_fechas_recepsion_entrega = fields.Integer(
        string="NÚMERO DE DIAS ENTRE RECEPCIÓN Y ENTREGA", 
        help='Son los números de dias que el equipo esta en las instalaciones de INSCO',
        compute="_compute_num_dias_recepcion_entrega",
        store=False
    )
    dias_entre_fechas_recepsion_orden = fields.Integer(
        string="NÚMERO DE DIAS ENTRE RECEPCIÓN Y OS",
        help='Son los números de dias que el equipo esta en la recepción de INSCO',
        compute="_compute_num_dias_recepsion_orden",
        store=False
    )
    dias_entre_fechas_cotizacion_ingreso_lab = fields.Integer(
        string="NÚMERO DE DIAS ENTRE REVICION DE COT Y ENTREGA AL LAB",
        help='Son los números de dias que el equipo no tiene una cotizacion',
        compute="_compute_num_dias_cotizacion_ingreso_lab",
        store=False
    )

    brought_by = fields.Char(
        string='Brought by',
        help='Nombre de la persona quien hace la recepción del equipo',
        tracking=True
    )
    delivery_by = fields.Char(
        string='Delivery by',
        help='Nombre de la persona quien hace la entrega del equipo',
        tracking=True
    )
    especial_requiriments = fields.Text(
        string='Especial requiriment',
        help='Requisitos especiales que requiere el cliente para sus equipos o emisión de algún documento  ',
        tracking=True
    )
    invoice_number = fields.Char(
        string='Número de factura'
    )

    observations_report_equipment_delivery = fields.Text(
        string='Observations report equipment delivery',
        help='Observations for report delivery equipment',
        tracking=True
    )

    sucursal_lab = fields.Selection([
                                        ('M', 'Laboratorio Matriz'),
                                        ('G', 'Sucursal Guadalajara'),
                                        ('Y', 'Sucursal Mérida'),
                                        ('B', 'Sucursal Bajío')],
                                        default='M', string='SUCURSAL')

    fecha_envio_facturar = fields.Date(
        string="FECHA DE SOLICITUD DE FACTURA"
    )

#----------------------Campos generales de la bitacora de areas tecnicas--------------------#


    certificate_number = fields.Char(string='INFORME',
        tracking=True,
        help='Codificación de certificado o reporte',
        default='SIN INFORME'
    )

    date_ingreso_lab = fields.Date(
        string='FECHA DE RECEPCIÓN A LAB.',
        help='Fecha en la que el área de recepción hace la entrega de los equipos y el laboratorio los recibe',
        tracking=True
    )

    marca_equipo = fields.Many2one('item.marca',
        string='MARCA',
        help='Marca del equipo a calibrar'
    )

    numero_serie = fields.Char(
        string='SERIE',
        help='Serie del equipo a calibrar',
        tracking=True
    )

    modelo_euipo = fields.Many2one('item.modelo',
        string='MODELO',
        help='Modelo del equipo a calibrar'
    )

    number_piezas = fields.Integer(
        string='NÚMERO DE PIEZAS',
        help='Este campo es para el laboratorio de Masa ya que un juego pude tener barias pieza',
        default='1'
    )

    clasificacion_equipo = fields.Many2one('item.clasificacion',string="CLASIFICACIÓN",tracking=True,copy=True)

    # clasificacion_equipo = fields.Selection([
    #                                     ('E1', 'E1'),
    #                                     ('E2', 'E2'),
    #                                     ('F1', 'F1'),
    #                                     ('F2', 'F2'),
    #                                     ('M1', 'M1'),
    #                                     ('M2', 'M2'),
    #                                     ('M3', 'M3'),
    #                                     ('1', '1'),
    #                                     ('2', '2'),
    #                                     ('3', '3'),
    #                                     ('4', '4'),
    #                                     ('5', '5'),
    #                                     ('6', '6'),
    #                                     ('7', '7'),
    #                                     ('ONN', 'ONN'),
    #                                     ('I', 'I'),
    #                                     ('II', 'II'),
    #                                     ('III', 'III'),
    #                                     ('RTDS', 'RTDS'),
    #                                     ('ESTUDIOS', 'ESTUDIOS'),
    #                                     ('TLV', 'TLV'),
    #                                     ('TC', 'TC'),
    #                                     ('TLD', 'TLD'),
    #                                     ('PIP MON', 'PIP MON'),
    #                                     ('PIP MUL', 'PIP MUL'),
    #                                     ('VAISALA', 'VAISALA'),
    #                                     ('TERMOHIGRO', 'TERMOHIGRO'),
    #                                     ('HIGRO', 'HIGRO'),
    #                                     ('AVS', 'AVS'),
    #                                     ('VAL', 'VAL'),
    #                                     ('IME', 'IME'),
    #                                     ('BAÑO', 'BAÑO'),
    #                                     ('VERIGO', 'VERIGO'),
    #                                     ('REFRIGERADOR', 'REFRIGERADOR'),
    #                                     ('MUFLA', 'MUFLA'),
    #                                     ('CÁMARACLIM', 'CAMARA CLIM'),
    #                                     ('ALMACEN', 'ALMACEN'),
    #                                     ('AUTOCLAVE', 'AUTOCLAVE'),
    #                                     ('TRANSPORTE', 'TRANSPORTE'),
    #                                     ('BAÑOMARIA', 'BAÑO MARIA'),
    #                                     ('UREFRIG', 'U.REFRIG'),
    #                                     ('INCUBADORA', 'INCUBADORA'),
    #                                     ('CONGELADOR', 'CONGELADOR'),
    #                                     ('HORNO', 'HORNO'),
    #                                     ('OTRO', 'OTRO')],
    #                                     string="CLASIFICACIÓN",tracking=True,copy=True)

    numero_id = fields.Char(
        string='IDENTIFICACIÓN',
        help='Identificación del equipo a calibrar',
        tracking=True
    )

    date_limpieza = fields.Date(
        string='FECHA DE LIMPIEZA ',
        help='Fecha de limpieza si aplica para el equipo',
        tracking=True
    )

    date_det_vol_final = fields.Date(
        string='DET. VOL. FINAL',
        tracking=True
    )

    date_calibracion = fields.Date(
        string='FECHA DE CALIBRACIÓN',
        help='Fecha en la que se realizan las mediciones',
        tracking=True
    )

    date_entrega_lab_real = fields.Date(
        string='FECHA DE ENTREGA',
        help='Fecha en la que el laboratorio hace la entrega del equipo al área de recepción de equipos o carpeta en el caso de MED ',
        tracking=True
    )

    supervisor_lab = fields.Many2one('res.users',
        string='SUPERVISADO POR',
        help='Persona que realiza la supervisión de todo el proceso',
        #relation='project_task_supervisor_lab_rel',  # Nombre único para la relación
        tracking = True
    )
    
    calibrado_por_lab = fields.Many2one('res.users',
        string='CALIBRADO POR',
        help='Persona que deve firmar todos los documento relacionados con el informe',
        #relation='project_task_calibrado_por_lab_rel',  # Nombre único para la relación
        tracking = True
    )

    aprobado_por_lab = fields.Many2one('res.users',
        string='APROBADO POR',
        help='Persona que aprueba la calibración y todos los procesos relacionados',
        #relation='project_task_aprobado_por_lab_rel',  # Nombre único para la relación
        tracking = True
    )

    date_calibracion_opcional = fields.Char(
        string='FORMATO FECHA',
        tracking=True,
        help='Esta fecha se captura cuando el cliente pide un formato diferente al que utiliza INSCO'
    )

    date_entrega_lab = fields.Date(
        string='FECHA PROGRAMADA DE ENTREGA',
        compute='_compute_date_entrega_lab',
        help='Esta fecha se calcula sumándole los días TIEMPO ASIGNADO a la FECHA DE RECEPCIÓN A LAB ',
        store=False,
        tracking=True
    )

    dias_entre_fechas_ingreso_salida_lab = fields.Integer(
        string="TIEMPO DE ENTREGA",
        help="Número de días trascurridos entre la fecha de ingreso al laboratorio y salida del laboratorio",
        compute="_compute_num_dias_ingreso_salida_lab",
        store=False
    )


    estado_service_lab = fields.Selection([
                                        ('RECIBIDO', 'RECIBIDO'),
                                        ('ENCALIBRACION', 'EN CALIBRACIÓN'),                                   
                                        ('ENTREGA', 'ENTREGADO'),
                                        ('CANCELADO', 'CANCELADO'),
                                        ('PENDIENTE', 'PENDIENTE')],
                                        help='Es el estatus en el que se encuentra el equipo dentro del laboratorio',
                                        string='ESTATUS LAB',
    )

    urgencia_del_servicio = fields.Selection([
                                            ('ordinario', 'Ordinario'),
                                            ('urgente', 'Urgente')],
                                            help='Cómo ejecutará el servicio',
                                            string='Urgencia del servicio',
                                            default='ordinario',
    )

    tipo_mantenimiento_equipo = fields.Selection([
                                        ('AJUSTE', 'AJUSTE'),
                                        ('REVISION', 'REVISIÓN'),                                   
                                        ('MANTENIMIENTOPRE', 'MANTENIMIENTO PRE'),
                                        ('MANTENIMIENTOCOR', 'MANTENIMIENTO COR'),
                                        ('REPARACION', 'REPARACIÓN'),
                                        ('SOLICITUDDECORRECCION', 'SOLICITUD DE CORRECIÓN'),
                                        ('N/A', 'N/A')],
                                        string='TIPO DE MANTENIMINETO',default='N/A',
    )


    tiempo_entrega = fields.Integer(
        string='TIEMPO ASIGNADO',
        help='Tiempo asignado en dias'
    )


    lugar_service = fields.Selection([
                                        ('LAB', 'LAB'),                                    
                                        ('SITIO', 'SITIO')],
                                        help='Lugar en doden se ejecutara el servicio',
                                        string='SERVICIO EN',
                                        default='LAB',
    )

    observations_lab = fields.Text(
        string='OBSERVACIÓNES',
        help='Observaciónes del equipo',
        tracking=True
    )






   
    date_proxima_calibracion = fields.Date(
        string='FECHA DE PROXIMA CALIBRACIÓN',
        help='Fecha sugerida por INSCO de México para la próxima calibración del equipo y para reportes internos  ',
        tracking=True
    )
    date_proxima_calibracion_opcional = fields.Char(
        string='FECHA DE PROXIMA CALIBRACIÓN OPCIONAL',
        tracking=True,
        help='Colocar N/A cuando el cliente no requiera fecha de próxima calibración colocar el formato que requiere el cliente '
    )







    date_supervision_lab = fields.Date(
        string='FECHA DE SUPERVISADO',
        help='Fecha en la que se realizó la supervisión',
        tracking=True
    )




    codificasion = fields.Selection([
                                        ('FA.G.12.11.09', 'FA.G.12.11.09'),
                                        ('FA.G.12.12.09', 'FA.G.12.12.09'),
                                        ('FA.G.12.13.09', 'FA.G.12.13.09'),
                                        ('FA.G.12.14.09', 'FA.G.12.14.09'),
                                        ('FA.G.12.15.09', 'FA.G.12.15.09'),
                                        ('FA.G.12.16.09', 'FA.G.12.16.09'),
                                        ('FA.G.12.17.09', 'FA.G.12.17.09'),
                                        ('FA.G.12.18.09', 'FA.G.12.18.09')],
                                        string="CODIFICACION PARA ETIQUETAS",tracking=True,copy=False)

    motivo_sustitucion_informe = fields.Selection([
                                        ('1', 'N/A'),
                                        ('2', 'Solicitud del cliente'),
                                        ('3', 'Error de laboratorio'),
                                        ('4', 'Error del área comercial'),
                                        ('5', 'Error de recepción de ítems')],
                                        string="MOTIVO DE SUSTITUCIÓN DE INFORME ",default='1' ,tracking=True)


    #campo para sacar y graficar por ASIGNADO A
    primer_usuario = fields.Many2one('res.users',
        string='PRIMER ASIGNADO',
        help='Este campo es para agrupar por ASIGNADO A ',
        compute='_compute_primer_usuario', store=True)
 

#--------------------------Campos del lab Med--------------------#




    os_termopares = fields.Char(
        string='O.S TERMOPARES', default='N/A'
    )

    date_cal_ter = fields.Date(string= 'FECHA DE CAL. TER'
    )

    os_temp_sensor = fields.Char(string = 'O.S. TEM. SENSOR', default='N/A'

    )

    os_hum_sensor = fields.Char(string='O.S. HUM. SENSOR', default='N/A'

    )

    getion_rieesgo_med = fields.Char(
        string="GESTION DE RIESGOS",
        tracking=True,
        default='N/A'
    )

    # date_inicio_med = fields.Date(string='FECHA DE INICIO MED'

    # )

    # date_termino_med = fields.Date(string='FECHA DE TERMINO MED'

    # )
    # date_entrega_med = fields.Date(string='FECHA DE ENTREGA MED.'

    # )
    # date_programada_entrega = fields.Date(string='FECHA PROGRAMADA DE ENTREGA MED.',
    #     #compute='_compute_date_entrega_med',

    # )
    # tiempo_entrega_med = fields.Integer(string='TIEMPO DE ENTREGA MED',
    #     #compute='_compute_num_dias_date_termino_med_date_entrega_med',

    # )

    # tiempo_asignado_med = fields.Integer(string='TIEMPO ASIGNADO MED')



    estado_service_lab_med = fields.Selection([
                                        ('N/A', 'N/A'),
                                        ('RECIBIDO', 'RECIBIDO'),
                                        ('ENVIO DE PROTOCOLOS', 'ENVÍO DE PROTOCLO'),                                   
                                        ('EJECUCION', 'EJECUCIÓ'),
                                        ('ELABORACIONDECARPETA', 'ELABORACIÓN DE CARPETA'),
                                        ('ENTREGADO', 'ENTREGADO'),
                                        ('CANCELADO', 'CANCELADO'),
                                        ('REPROGRAMADO', 'REPROGRAMADO')],
                                        string='ESTATUS MED', default='N/A'
    )

    # tipo_mantenimiento_med = fields.Selection([                                   
    #                                         ('MANTENIMIENTOPRE', 'MANTENIMIENTO PRE'),
    #                                         ('MANTENIMIENTOCOR', 'MANTENIMIENTO COR'),
    #                                         ('N/A', 'N/A')],
    #                                         string='TIPO DE MANTENIMIENTO MED', default='N/A'
    # )





    # clasificacion_equipo_med = fields.Selection([
    #                                         ('REFRIGERADOR', 'REFRIGERADOR'),
    #                                         ('MUFLA', 'MUFLA'),
    #                                         ('CÁMARACLIM', 'CAMARA CLIM'),
    #                                         ('ALMACEN', 'ALMACEN'),
    #                                         ('AUTOCLAVE', 'AUTOCLAVE'),
    #                                         ('TRANSPORTE', 'TRANSPORTE'),
    #                                         ('BAÑOMARIA', 'BAÑO MARIA'),
    #                                         ('UREFRIG', 'U.REFRIG'),
    #                                         ('INCUBADORA', 'INCUBADORA'),
    #                                         ('CONGELADOR', 'CONGELADOR'),
    #                                         ('HORNO', 'HORNO'),
    #                                         ('OTRO', 'OTRO')],
    #                                         string="CLASIFICACIÓN MED",tracking=True,copy=False)



    # codigo_documento_entregable = fields.Char(
    #     string="CODIGO DE DOCUMENTO ENTREGABLE",
    #     tracking=True
    # )

    tipo_servicio_med = fields.Selection([
                                        ('N/A', 'N/A'),
                                        ('CO CF', 'CO CF'),
                                        ('CF', 'CF'),
                                        ('CI CO CF', 'CI CO CF'),
                                        ('CD CI CO CF', 'CD CI CO CF'),
                                        ('CaracterizaciónCM ', 'Caracterización CM'),
                                        ('MonitoreoMT', 'Monitoreo MT'),
                                        ('Fallo electrico', 'Fallo electrico'),
                                        ('Apertura de puerta', 'Apertura de puerta'),
                                        ('Prueba de alarma', 'Prueba de alarma')],
                                        string="TIPO DE SERVICIO MED", default='N/A',tracking=True,copy=False)
    

#-------------------Metodos para las bitacoras de los laboratorios de calibracion--------------------------#


# esta funcion cuenta los dias que los equipos del cliente se encuentran en las intalaciones de insco
    @api.depends('date_reception', 'date_delivery')
    def _compute_num_dias_recepcion_entrega(self):
        dias_no_habiles = [
        date(2024, 1, 1),   # 1 de enero: Año Nuevo
        date(2024, 2, 5),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        date(2024, 3, 18),  # 18 de marzo: Natalicio de Benito Juárez
        date(2024, 5, 1),   # 1 de mayo: Día del Trabajo
        date(2024, 9, 16),  # 16 de septiembre: Día de la Independencia
        date(2024, 10, 1),  # 1 de octubre: cambio de poder ejecutivo
        date(2024, 11, 18), # 18 de noviembre: revolucion mexicana
        date(2024, 12, 25), # Navidad
        ]
        for registro in self:
            if registro.date_reception and registro.date_delivery:
                date_reception = registro.date_reception
                date_delivery = registro.date_delivery
                diferencia = date_delivery - date_reception
                dias = diferencia.days + 1  # Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (date_reception + timedelta(d)).weekday() < 5 and (date_reception + timedelta(d)).day not in dias_no_habiles]
                registro.dias_entre_fechas_recepsion_entrega = len(dias_habiles)
            else:
                registro.dias_entre_fechas_recepsion_entrega = 0
    

# este metodo cuenta los dias entre la recepcion del equipo a insco hata que se realiza la orden de servicio 
    @api.depends('date_reception', 'date_service_order')
    def _compute_num_dias_recepsion_orden(self):
        dias_no_habiles = [
        date(2024, 1, 1),   # 1 de enero: Año Nuevo
        date(2024, 2, 5),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        date(2024, 3, 18),  # 18 de marzo: Natalicio de Benito Juárez
        date(2024, 5, 1),   # 1 de mayo: Día del Trabajo
        date(2024, 9, 16),  # 16 de septiembre: Día de la Independencia
        date(2024, 10, 1),  # 1 de octubre: cambio de poder ejecutivo
        date(2024, 11, 18), # 18 de noviembre: revolucion mexicana
        date(2024, 12, 25), # Navidad
        ]
        for registro in self:
            if registro.date_reception and registro.date_service_order:
                date_reception = registro.date_reception
                date_service_order = registro.date_service_order
                diferencia = date_service_order - date_reception
                dias = diferencia.days + 1  # Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (date_reception + timedelta(d)).weekday() < 5 and (date_reception + timedelta(d)).day not in dias_no_habiles]
                registro.dias_entre_fechas_recepsion_orden = len(dias_habiles)
            else:
                registro.dias_entre_fechas_recepsion_orden = 0

    
#Este metodo cuenta los dias entre la revicion de la cotizacion y el ingreso al laboratorio 
    @api.depends('fecha_revision_cotizacion', 'date_ingreso_lab')
    def _compute_num_dias_cotizacion_ingreso_lab(self):
        dias_no_habiles = [
        date(2024, 1, 1),   # 1 de enero: Año Nuevo
        date(2024, 2, 5),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        date(2024, 3, 18),  # 18 de marzo: Natalicio de Benito Juárez
        date(2024, 5, 1),   # 1 de mayo: Día del Trabajo
        date(2024, 9, 16),  # 16 de septiembre: Día de la Independencia
        date(2024, 10, 1),  # 1 de octubre: cambio de poder ejecutivo
        date(2024, 11, 18), # 18 de noviembre: revolucion mexicana
        date(2024, 12, 25), # Navidad
        ]
        for registro in self:
            if registro.fecha_revision_cotizacion and registro.date_ingreso_lab:
                fecha_revision_cotizacion = registro.fecha_revision_cotizacion
                date_ingreso_lab = registro.date_ingreso_lab
                diferencia = date_ingreso_lab - fecha_revision_cotizacion
                dias = diferencia.days + 1  # Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (fecha_revision_cotizacion + timedelta(d)).weekday() < 5 and (fecha_revision_cotizacion + timedelta(d)).day not in dias_no_habiles]
                registro.dias_entre_fechas_cotizacion_ingreso_lab = len(dias_habiles)
            else:
                registro.dias_entre_fechas_cotizacion_ingreso_lab = 0


#este metodo calcula la fecha de entrega desde la fecha de ingreso al laboratorio y los dias asignados 
    @api.depends('date_ingreso_lab', 'tiempo_entrega')
    def _compute_date_entrega_lab(self):
        dias_no_habiles = [
        date(2024, 1, 1),   # 1 de enero: Año Nuevo
        date(2024, 2, 5),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        date(2024, 3, 18),  # 18 de marzo: Natalicio de Benito Juárez
        date(2024, 5, 1),   # 1 de mayo: Día del Trabajo
        date(2024, 9, 16),  # 16 de septiembre: Día de la Independencia
        date(2024, 10, 1),  # 1 de octubre: cambio de poder ejecutivo
        date(2024, 11, 18), # 18 de noviembre: revolucion mexicana
        date(2024, 12, 25), # Navidad
        ]
        for registro in self:
            if registro.date_ingreso_lab and registro.tiempo_entrega:
                if registro.lugar_service == 'SITIO' and registro.date_calibracion:
                    fecha_entrega = registro.date_calibracion
                    dias_entrega = registro.tiempo_entrega
                else:
                    fecha_entrega = registro.date_ingreso_lab
                    dias_entrega = registro.tiempo_entrega
                while dias_entrega > 0:
                    fecha_entrega += timedelta(days=1)
                    if fecha_entrega.weekday() < 5 and fecha_entrega not in dias_no_habiles:
                        dias_entrega -= 1
                registro.date_entrega_lab = fecha_entrega
            else:
                registro.date_entrega_lab = False


    
    #ESTA FUNCION CUENTA LOS DIAS ENTRE LA FECHA DE INGREDO AL LABORATORIO Y LA FECHA REAL DE ENTREGA 
    @api.depends('date_ingreso_lab', 'date_entrega_lab_real')
    def _compute_num_dias_ingreso_salida_lab(self):
        dias_no_habiles = [
        date(2024, 1, 1),   # 1 de enero: Año Nuevo
        date(2024, 2, 5),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        date(2024, 3, 18),  # 18 de marzo: Natalicio de Benito Juárez
        date(2024, 5, 1),   # 1 de mayo: Día del Trabajo
        date(2024, 9, 16),  # 16 de septiembre: Día de la Independencia
        date(2024, 10, 1),  # 1 de octubre: cambio de poder ejecutivo
        date(2024, 11, 18), # 18 de noviembre: revolucion mexicana
        date(2024, 12, 25), # Navidad
        ]
        for registro in self:
            if registro.date_ingreso_lab and registro.date_entrega_lab_real:
                date_ingreso_lab = registro.date_ingreso_lab
                date_entrega_lab_real = registro.date_entrega_lab_real
                diferencia = date_entrega_lab_real - date_ingreso_lab
                dias = diferencia.days + 1  # Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (date_ingreso_lab + timedelta(d)).weekday() < 5 and (date_ingreso_lab + timedelta(d)).day not in dias_no_habiles]
                registro.dias_entre_fechas_ingreso_salida_lab = len(dias_habiles)
            else:
                registro.dias_entre_fechas_ingreso_salida_lab = 0

    

#---------Esta funcion es para calcular el primer usuario que esta en el campo user_ids y asi poder sacar una grafica--------#

    @api.depends('user_ids')
    def _compute_primer_usuario(self):
        for tarea in self:
            if tarea.user_ids:
                primer_usuario = tarea.user_ids[0]  # Seleccionar el primer usuario
                tarea.primer_usuario = primer_usuario


#-----------------------Metodos para la bitacora de Medicones especiales--------------------#

    #este metodo calcula la fecha programada de entrega de el lab de meciicones especiales  
    # @api.depends('date_termino_med', 'tiempo_asignado_med')
    # def _compute_date_entrega_med(self):
    #     dias_no_habiles = [
    #     date(2023, 1, 1),   # Año Nuevo
    #     date(2023, 2, 6),   # Dia de la constitucion Méxica
    #     date(2023, 3, 20),  # Natalicio de benitojuares
    #     date(2023, 5, 1),   # Día del trabajo
    #     date(2023, 9, 16),  # Día de la Independencia de México.
    #     date(2023, 11, 20), # Día de la revolucion
    #     date(2023, 12, 25), # Navidad
    #     ]
    #     for registro in self:
    #         if registro.date_termino_med and registro.tiempo_asignado_med:
    #             fecha_entrega = registro.date_termino_med
    #             dias_entrega = registro.tiempo_asignado_med
    #             while dias_entrega > 0:
    #                 fecha_entrega += timedelta(days=1)
    #                 if fecha_entrega.weekday() < 5 and fecha_entrega not in dias_no_habiles:
    #                     dias_entrega -= 1
    #             registro.date_programada_entrega = fecha_entrega
    #         else:
    #             registro.date_programada_entrega = False

    # esta funcion cuenta los dias despues del termino de del servicio en campo y la fecha de entrega 
    # @api.depends('date_termino_med', 'date_entrega_med')
    # def _compute_num_dias_date_termino_med_date_entrega_med(self):
    #     dias_no_habiles = [
    #     date(2023, 1, 1),   # Año Nuevo
    #     date(2023, 2, 6),   # Dia de la constitucion Méxica
    #     date(2023, 3, 20),  # Natalicio de benitojuares
    #     date(2023, 5, 1),   # Día del trabajo
    #     date(2023, 9, 16),  # Día de la Independencia de México.
    #     date(2023, 11, 20), # Día de la revolucion
    #     date(2023, 12, 25), # Navidad
    #     ]
    #     for registro in self:
    #         if registro.date_termino_med and registro.date_entrega_med:
    #             date_termino_med = registro.date_termino_med
    #             date_entrega_med = registro.date_entrega_med
    #             diferencia = date_entrega_med - date_termino_med
    #             dias = diferencia.days + 1  # Se agrega 1 para incluir la fecha final
    #             #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
    #             dias_habiles = [d for d in range(dias) if (date_termino_med + timedelta(d)).weekday() < 5 and (date_termino_med + timedelta(d)).day not in dias_no_habiles]
    #             registro.tiempo_entrega_med = len(dias_habiles)
    #         else:
    #             registro.tiempo_entrega_med = 0


#-----------------------Metodos para visualizar las ventanas de los wizard para los numeros de informe--------#


    def open_certificate_wizard_masa(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Masa',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_masa').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_temperatura(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Temperatura',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_temperatura').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_humedad(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Humedad',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_humedad').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }
    def open_certificate_wizard_med(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio MED',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_med').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_kaye(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Kaye',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_kaye').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_volumen(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio volumen',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_volumen').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_electrica(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Electrica',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_report_projects.certificate_wizard_view_form_electrica').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }


#-------------metodos para los reportes en pdf------------------#


    def get_street_partner(self):
        return "{}, {}, {}".format(
            self.partner_id.street_name or '',
            self.partner_id.street_number or '',
            self.partner_id.street_number2 or '')

    def get_address_partner(self):
        return {
            'colony': self.partner_id.l10n_mx_edi_colony or '',
            'city': self.partner_id.city or '',
            'zip': self.partner_id.zip or '',
            'street_name': self.partner_id.street_name or '',
            'number1': self.partner_id.street_number or '',
            'number2': self.partner_id.street_number2 or '',
            'vat': self.partner_id.vat or '',
            'phone': self.partner_id.phone or '',
            'state': self.partner_id.state_id.name if self.partner_id.state_id.name else '',
            'x_studio_contacto' : self.create_uid.address_id.x_studio_contacto}


    def branch_office_company(self):
        return {
            'colony': self.create_uid.address_id.l10n_mx_edi_colony or '',
            'city': self.create_uid.address_id.city or '',
            'zip': self.create_uid.address_id.zip or '',
            'street_name': self.create_uid.address_id.street_name or '',
            'number1': self.create_uid.address_id.street_number or '',
            'number2': self.create_uid.address_id.street_number2 or '',
            'vat': self.create_uid.address_id.vat or '',
            'phone': self.create_uid.address_id.phone or '',
            'state': self.create_uid.address_id.state_id.name if self.create_uid.address_id.state_id.name else '',
            'x_studio_contacto' : self.partner_id.x_studio_contacto}



    def get_street_shipping(self):
        return "{}, {}, {}".format(
            self.sale_line_id.order_id.partner_shipping_id.street_name or '',
            self.sale_line_id.order_id.partner_shipping_id.street_number or '',
            self.sale_line_id.order_id.partner_shipping_id.street_number2 or '')

    def get_certificate_addres(self):
        return {
            'name': self.sale_line_id.order_id.partner_shipping_id.name or '',
            'street': self.sale_line_id.order_id.partner_shipping_id.street_name or '',
            'colony': self.sale_line_id.order_id.partner_shipping_id.l10n_mx_edi_colony or '',
            'city': self.sale_line_id.order_id.partner_shipping_id.city or '',
            'zip': self.sale_line_id.order_id.partner_shipping_id.zip or '',
            'state': self.sale_line_id.order_id.partner_shipping_id.state_id.name or '',
            'email': self.sale_line_id.order_id.partner_shipping_id.email or '',
            'number': self.sale_line_id.order_id.partner_invoice_id.street_number or '',
            'number2': self.sale_line_id.order_id.partner_invoice_id.street_number2 or ''
        }

    def convert_description_pad(self, description):
        flags = re.IGNORECASE | re.MULTILINE
        html = re.sub(r'\[font\s*([^\]]+)\]', '<font \1>', description, flags=flags)
        html = re.sub(r'\[/font\s*\]', '</font>', html, flags=flags)
        return html

    def get_description_text(self):
        html = self.convert_description_pad(self.description)
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.ignore_emphasis = True
        return h.handle(html)



# Clases para complemetar lasbitacoras

class customItemMarca(models.Model):
    _name = "item.marca"
    _description = "Item-Marca"


    name= fields.Char(string='Marca', required=True, copy=False, readonly=True, index=True)


class customItemModelo(models.Model):
    _name = "item.modelo"
    _description = "Item-Modelo"

    name= fields.Char(string='Modelo', required=True, copy=False, readonly=True, index=True)

class customItemClasificacion(models.Model):
    _name = "item.clasificacion"
    _description = "clasificacion-equipo"


    name= fields.Char(string='Clasificacion', required=True, copy=False, readonly=True, index=True)
    tiempo_asignado=fields.Integer(string='TIEMPO ASIGNADO EN DIAS')