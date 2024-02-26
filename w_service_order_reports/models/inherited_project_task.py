# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2019 Wedoo - https://wedoo.tech
# All Rights Reserved.
#
# Developer(s): Sergio Ernesto Tostado Sánchez
#               (sts@wedoo.tech)
#
########################################################################
#
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

from odoo import api, fields, models, _
from datetime import datetime, date, timedelta


class ProjectTask(models.Model):

    _inherit = "project.task"

    service_order = fields.Char(
        string="Service Order",
        help="Service Order for this task.",
        tracking=True
    )

    procedimiento = fields.Char(
        string="Procedimiento",
        related = 'sale_line_id.product_id.x_studio_etiquetas', 
        store = True,
        tracking=True
    )
    descripcion_linea_ventas = fields.Text(
        string="DESCRIPCIÓN DEL ITEM",
        related = 'sale_line_id.name'
    )


#------------------Campos de los documentos de recepcion, orden de servicio y entrega-------------------# 


    fecha_revision_cotizacion = fields.Date(
        string='FECHA DE REVISIÓN DE COTIZACION',
        help='Fecha en la que se revisa la cotización sin errores',
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




    sucursal_lab = fields.Selection([
                                        ('M', 'Laboratorio Matriz'),
                                        ('G', 'Sucursal Guadalajara'),
                                        ('Y', 'Sucursal Mérida'),
                                        ('B', 'Sucursal Bajío')],
                                        default='M', string='SUCURSAL')

    fecha_envio_facturar = fields.Date(
        string="FECHA DE SOLICITUD DE FACTURA"
    )

    fecha_solicitud_cotizacion = fields.Date(string="Fecha Solicitud de cotizacion")

#----------------------Campos generales de la bitacora de areas tecnicas--------------------#


    date_ingreso_lab = fields.Date(
        string='FECHA DE RECEPCIÓN A LAB',
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
        store=True,
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
                                        ('ENPROCESO', 'EN PROCESO'),                                   
                                        ('ENTREGADO', 'ENTREGADO'),
                                        ('CANCELADO', 'CANCELADO'),
                                        ('PENDIENTE', 'PENDIENTE')],
                                        help='Es el estatus en el que se encuentra el equipo dentro del laboratorio',
                                        string='ESTATUS LAB',
    )

    urgencia_del_servicio = fields.Selection([
                                            ('ordinario', 'ORDINARIO'),
                                            ('urgente', 'URGENTE')],
                                            help='Cómo ejecutará el servicio',
                                            string='URGENCIA DEL SERVICIO',
                                            default='ordinario',
    )

    # tipo_mantenimiento_equipo = fields.Selection([
    #                                     ('AJUSTE', 'AJUSTE'),
    #                                     ('REVISION', 'REVISIÓN'),                                   
    #                                     ('MANTENIMIENTOPRE', 'MANTENIMIENTO PRE'),
    #                                     ('MANTENIMIENTOCOR', 'MANTENIMIENTO COR'),
    #                                     ('REPARACION', 'REPARACIÓN'),
    #                                     ('SOLICITUDDECORRECCION', 'SOLICITUD DE CORRECIÓN'),#eliminar
    #                                     ('N/A', 'N/A')],
    #                                     string='TIPO DE MANTENIMINETO',default='N/A',
    # )

    tipo_mantenimiento_equipo = fields.Selection([
                                        ('AJUSTE', 'Ajuste'),
                                        ('REVISION', 'Revisión'),                                   
                                        ('MANTENIMIENTOPRE', 'Mantenimiento preventivo'),
                                        ('MANTENIMIENTOCOR', 'Mantenimiento correctivo'),
                                        ('REPARACION', 'Reparación'),
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
        string='OBSERVACIÓNES LAB',
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
                                        ('PENDIENTE', 'PENDIENTE'),
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
        datetime(2024, 1, 1).date(),   # 1 de enero: Año Nuevo
        datetime(2024, 2, 5).date(),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        datetime(2024, 3, 18).date(),  # 18 de marzo: Natalicio de Benito Juárez
        datetime(2024, 5, 1).date(),   # 1 de mayo: Día del Trabajo
        datetime(2024, 9, 16).date(),   # 16 de septiembre: Día de la Independencia
        datetime(2024, 10, 1).date(),  # 1 de octubre: cambio de poder ejecutivo
        datetime(2024, 11, 18).date(), # 18 de noviembre: revolucion mexicana
        datetime(2024, 12, 25).date(), # Navidad
        ]
        for registro in self:
            if registro.date_reception and registro.date_delivery:
                date_reception = registro.date_reception
                date_delivery = registro.date_delivery
                diferencia = date_delivery - date_reception
                dias = diferencia.days #+ 1   Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (date_reception + timedelta(d)).weekday() < 5 and (date_reception + timedelta(d)) not in dias_no_habiles]
                registro.dias_entre_fechas_recepsion_entrega = len(dias_habiles)
            else:
                registro.dias_entre_fechas_recepsion_entrega = 0
    

# este metodo cuenta los dias entre la recepcion del equipo a insco hata que se realiza la orden de servicio 
    @api.depends('date_reception', 'date_service_order')
    def _compute_num_dias_recepsion_orden(self):
        dias_no_habiles = [
        datetime(2024, 1, 1).date(),   # 1 de enero: Año Nuevo
        datetime(2024, 2, 5).date(),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        datetime(2024, 3, 18).date(),  # 18 de marzo: Natalicio de Benito Juárez
        datetime(2024, 5, 1).date(),   # 1 de mayo: Día del Trabajo
        datetime(2024, 9, 16).date(),   # 16 de septiembre: Día de la Independencia
        datetime(2024, 10, 1).date(),  # 1 de octubre: cambio de poder ejecutivo
        datetime(2024, 11, 18).date(), # 18 de noviembre: revolucion mexicana
        datetime(2024, 12, 25).date(), # Navidad
        ]
        for registro in self:
            if registro.date_reception and registro.date_service_order:
                date_reception = registro.date_reception
                date_service_order = registro.date_service_order
                diferencia = date_service_order - date_reception
                dias = diferencia.days + 1  # Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (date_reception + timedelta(d)).weekday() < 5 and (date_reception + timedelta(d)) not in dias_no_habiles]
                registro.dias_entre_fechas_recepsion_orden = len(dias_habiles)
            else:
                registro.dias_entre_fechas_recepsion_orden = 0

    
#Este metodo cuenta los dias entre la revicion de la cotizacion y el ingreso al laboratorio 
    @api.depends('fecha_revision_cotizacion', 'date_ingreso_lab')
    def _compute_num_dias_cotizacion_ingreso_lab(self):
        dias_no_habiles = [
        datetime(2024, 1, 1).date(),   # 1 de enero: Año Nuevo
        datetime(2024, 2, 5).date(),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        datetime(2024, 3, 18).date(),  # 18 de marzo: Natalicio de Benito Juárez
        datetime(2024, 5, 1).date(),   # 1 de mayo: Día del Trabajo
        datetime(2024, 9, 16).date(),   # 16 de septiembre: Día de la Independencia
        datetime(2024, 10, 1).date(),  # 1 de octubre: cambio de poder ejecutivo
        datetime(2024, 11, 18).date(), # 18 de noviembre: revolucion mexicana
        datetime(2024, 12, 25).date(), # Navidad
        ]
        for registro in self:
            if registro.fecha_revision_cotizacion and registro.date_ingreso_lab:
                fecha_revision_cotizacion = registro.fecha_revision_cotizacion
                date_ingreso_lab = registro.date_ingreso_lab
                diferencia = date_ingreso_lab - fecha_revision_cotizacion
                dias = diferencia.days #+ 1   Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (fecha_revision_cotizacion + timedelta(d)).weekday() < 5 and (fecha_revision_cotizacion + timedelta(d)) not in dias_no_habiles]
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


    
    #ESTA FUNCION CUENTA LOS DIAS ENTRE LA FECHA DE INGRESO AL LABORATORIO Y LA FECHA REAL DE ENTREGA 
    #TAMBIEN SI EL EN SITIO CUENTA LOS DIAS APARTIR DE LA FECHA DE CALIBRACION
    @api.depends('date_ingreso_lab', 'date_entrega_lab_real', 'date_calibracion')
    def _compute_num_dias_ingreso_salida_lab(self):
        dias_no_habiles = [
        datetime(2024, 1, 1).date(),   # 1 de enero: Año Nuevo
        datetime(2024, 2, 5).date(),   # 5 de febrero: Aniversario de la promulgación de la Constitución de 1917
        datetime(2024, 3, 18).date(),  # 18 de marzo: Natalicio de Benito Juárez
        datetime(2024, 5, 1).date(),   # 1 de mayo: Día del Trabajo
        datetime(2024, 9, 16).date(),   # 16 de septiembre: Día de la Independencia
        datetime(2024, 10, 1).date(),  # 1 de octubre: cambio de poder ejecutivo
        datetime(2024, 11, 18).date(), # 18 de noviembre: revolucion mexicana
        datetime(2024, 12, 25).date(), # Navidad
        ]
        for registro in self:
            if registro.date_ingreso_lab and registro.date_entrega_lab_real:
                date_ingreso_lab = registro.date_ingreso_lab
                date_entrega_lab_real = registro.date_entrega_lab_real

                # Agregar lógica para manejar lugar_service
                if registro.lugar_service == 'SITIO' and registro.date_calibracion:
                    date_ingreso_lab = registro.date_calibracion

                diferencia = date_entrega_lab_real - date_ingreso_lab
                dias = diferencia.days #+ 1  Se agrega 1 para incluir la fecha final
                #dias_no_habiles = [d.day for d in dias_no_habiles]  # Convertir objetos fecha a enteros (días)
                dias_habiles = [d for d in range(dias) if (date_ingreso_lab + timedelta(d)).weekday() < 5 and (date_ingreso_lab + timedelta(d)) not in dias_no_habiles]
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
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_masa').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_temperatura(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Temperatura',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_temperatura').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_humedad(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Humedad',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_humedad').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }
    def open_certificate_wizard_med(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio MED',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_med').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_kaye(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Kaye',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_kaye').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_volumen(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio volumen',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_volumen').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }

    def open_certificate_wizard_electrica(self):
        return {
            'name': 'Asignar Tipo de documento Laboratorio Electrica',
            'type': 'ir.actions.act_window',
            'res_model': 'certificate.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('w_service_order_reports.certificate_wizard_view_form_electrica').id,
            'target': 'new',
            'context': {'active_ids': self._ids},
        }



    #--------------------metodos de los reportes----------------------#

    @api.model
    def getServiceOrders(self, docs, no_sequence=True):
        if no_sequence:
            docs_needs_serv_order = docs.filtered(lambda r: not r.service_order)
            if docs_needs_serv_order:
                next_serv_order = self.env['ir.sequence'].next_by_code(
                    'service.order')
                docs_needs_serv_order.write({
                    'service_order': next_serv_order
                })
        service_orders = ", ".join(
            set([task.service_order for task in docs if task.service_order]))
        procedures = ", ".join(set(
            [task.sale_line_id.product_id.product_tmpl_id.process for task in docs if task.sale_line_id.product_id.product_tmpl_id.process]))
        # init for second list in first iteration after the list principal
        # and join exclude duplicates
        tags = ",".join(set(
            [tag.name for task in docs for tag in task.tag_ids]))
        service_types = [
            {
                'service': task.sale_line_id.name,
                'product_id': task.sale_line_id.product_id,
                'origin': task.service_order,
                'qty': task.sale_line_id.product_uom_qty,
                'description': task.get_description_text(),
                'procedures': procedures,
                'tags': tags,
                'certificate_number': task.certificate_number,
                'observations_report_equipment_delivery': task.observations_report_equipment_delivery,
                'observations_report_equipment_reception': task.observations_report_equipment_reception
                } for task in docs]
        return docs[0].with_context({
            'service_orders': service_orders,
            'service_types': service_types
        })

    @api.model
    def get_services_description(self, docs):
        service_orders = ", ".join(set(
            [task.service_order for task in docs if task.service_order]))
        procedures = ", ".join(set(
            [task.sale_line_id.product_id.product_tmpl_id.process for task in docs if task.sale_line_id.product_id.product_tmpl_id.process]))
        service_types = [
            {   'service_orders': service_orders,
                'service': task.sale_line_id.name,
                'qty': task.sale_line_id.product_uom_qty,
                'procedures': procedures,
                'origin': task.service_order} for task in docs]
        return {'service_types': service_types}
