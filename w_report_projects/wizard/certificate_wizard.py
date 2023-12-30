from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CertificateWizard(models.TransientModel):
    _name = 'certificate.wizard'
    _description = 'Asignacion de tipo de documento y secuencia'
    
    # prefix = fields.Char(string="codificación a certificados o reportes",
    #     help='Esto es una prueba de ayuda'
    #     )
    
    # suffix = fields.Char(string="Sufijo")

    tipo_documento = fields.Selection([
                                        ('CC', 'Certificado de Calibración'),
                                        ('CM', 'Certificado de Medición o Caracterización'),
                                        ('CE', 'Certificado de estudio térmico'),
                                        ('RC', 'Reporte de Calificación'),
                                        ('RS', 'Reporte de servicio, que puede ser de revisión, mantenimiento o reparación'),
                                        ('RM', 'Reporte de Monitoreo')],
                                        default='CC', string='codificación a certificados o reportes')
    lugar_lab = fields.Selection([
                                        ('M', 'Laboratorio Matriz'),
                                        ('G', 'Sucursal Guadalajara'),
                                        ('Y', 'Sucursal Mérida'),
                                        ('B', 'Sucursal Bajío')],
                                        default='M', string='Lugar donde se realizaron las mediciones')
    # tipo_lab = fields.Selection([
    #                                     ('M', 'Masa'),
    #                                     ('T', 'Temperatura'),
    #                                     ('H', 'Huemedad'),
    #                                     ('MED', 'MED'),
    #                                     ('K', 'Kaye'),
    #                                     ('E', 'Electrica'),
    #                                     ('V', 'Volumen')],
    #                                     default='CCM', string='Lugar donde se realizaron las mediciones')
    
    # @api.model
    # def default_get(self, fields):
    #     defaults = super(CertificateWizard, self).default_get(fields)
    #     task_ids = self.env.context.get('active_ids')
    #     task_objs = self.env['project.task'].browse(task_ids)
    #     prefix = task_objs[0].certificate_number.split('.')[0]
    #     suffix = task_objs[0].certificate_number.split('.')[-1]
    #     defaults.update({'prefix': prefix, 'suffix': suffix})
    #     return defaults


    # Funcion que asigna numero de secuencia o infome para el laboratorio de Masa#
    def update_certificate_number_masa(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_masa_matriz_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        elif self.tipo_documento == 'RS':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_masa_matriz_reporte_servicio')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else: raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")

 # Funcion que asigna numero de secuencia o infome para el laboratorio de Temperatura#
    def update_certificate_number_temperatura(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_matriz_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            elif self.lugar_lab == 'G':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_guadalajara_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")

        elif self.tipo_documento == 'CM':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_matriz_certificado_medicion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            elif self.lugar_lab == 'G':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_guadalajara_certificado_medicion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")

        elif self.tipo_documento == 'CE':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_matriz_certificado_estudio_termico')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            elif self.lugar_lab == 'G':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_guadalajara_certificado_estudio_termico')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")

        elif self.tipo_documento == 'RS':
            if self.lugar_lab == 'M': 
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_matriz_reporte_servicio')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            elif self.lugar_lab == 'G': 
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_temperatura_guadalajara_reporte_servicio')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else:raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")

     # Funcion que asigna numero de secuencia o infome para el laboratorio de Humedad#

    def update_certificate_number_humedad(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_humedad_matriz_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            elif self.lugar_lab == 'G':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_humedad_guadalajara_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else: raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")

 # # Funcion que asigna numero de secuencia o infome para el laboratorio Mediciones espciales#

    def update_certificate_number_med(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CM':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_med_matriz_certificado_medicion_caracterizacion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        elif self.tipo_documento == 'RM':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_med_matriz_reporte_monitoreo')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        elif self.tipo_documento == 'RC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_med_matriz_reporte_calificacion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number

                    sequenceGR = self.env.ref('w_service_order_reports.sequence_lab_med_matriz_gestion_riesgo')
                    certificate_number = "{}{}{}".format('GR',self.lugar_lab, sequenceGR.next_by_id())
                    task.getion_rieesgo_med = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else: raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")




 # Funcion que asigna numero de secuencia o infome para el laboratorio de Kaye#
    def update_certificate_number_kaye(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_kaye_matriz_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        elif self.tipo_documento == 'RS':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_kaye_matriz_reporte_servicio')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else: raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")

    def update_certificate_number_volumen(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_volumen_matriz_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        elif self.tipo_documento == 'RS':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_volumen_matriz_reporte_servicio')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else: raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")

 # Funcion que asigna numero de secuencia o infome para el laboratorio de Electrica#
    def update_certificate_number_electrica(self):
        task_ids = self.env.context.get('active_ids')
        task_objs = self.env['project.task'].browse(task_ids)
        if self.tipo_documento == 'CC':
            if self.lugar_lab == 'M':
                for task in task_objs:
                    sequence = self.env.ref('w_service_order_reports.sequence_lab_electrica_matriz_certificado_calibracion')
                    certificate_number = "{}{}{}".format(self.tipo_documento,self.lugar_lab, sequence.next_by_id())
                    task.certificate_number = certificate_number
            else:raise ValidationError("El tipo de  laboratorio no se encuentra valido para tu sucursal")
        else: raise ValidationError("El tipo de documento no se encuentra valido para tu laboratorio")


