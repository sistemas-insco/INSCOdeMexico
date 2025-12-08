from odoo import models, fields, api
import base64
# Ya no es necesario directamente para cadena, ya que ahora lo maneja la lógica central de Odoo
# from odoo.tools import xslt
# CFDI_XSLT_CADENA_TFD = 'l10n_mx_edi/data/xslt/3.3/cadenaoriginal_TFD_1_1.xslt'


class AccountMove(models.Model): # Se cambió el nombre de AccountInvoice a AccountMove para mayor claridad, ya que el modelo es account.move.
    _inherit = 'account.move'

    observations = fields.Text(
        string='Observaciones'
    )
    # Los campos a continuación se calcularán utilizando los métodos estándar de Odoo V18
    # Obtendremos todos los valores CFDI de una sola llamada a _l10n_mx_edi_get_extra_invoice_report_values()
    # Y luego asignarlas.

    # Estos campos pueden permanecer como campos Char
    sello_cfdi = fields.Char(
        string="Sello CFDI",
        compute="_compute_custom_cfdi_values", # Se cambió el nombre del método de cálculo para evitar conflictos
        store=False, # Marcar como Falso si no necesita almacenarlos en la base de datos para mejorar el rendimiento
    )
    sello_sat = fields.Char(
        string="Sello SAT",
        compute="_compute_custom_cfdi_values",
        store=False,
    )
    cfdi_cadena = fields.Char(
        string="Cadena Original",
        compute='_compute_custom_cfdi_values',
        store=False,
    )
    payment_method = fields.Char(
        string='Método de Pago CFDI', # Clarified string
        compute="_compute_custom_cfdi_values",
        store=False,
    )
    serial_number = fields.Char(
        string='Número de Serie del Certificado',
        compute='_compute_custom_cfdi_values',
        store=False,
    )

    # En Odoo V18, debes utilizar principalmente  _l10n_mx_edi_get_extra_common_report_values()
    # ó _l10n_mx_edi_get_extra_invoice_report_values() Para obtener datos CFDI.
    # The _get_l10n_mx_edi_cadena El método ya no es necesario ya que la cadena es parte del diccionario estándar devuelto por los métodos de Odoo.
    # Entonces este método se puede eliminar.

    @api.depends('l10n_mx_edi_cfdi_attachment_id', 'l10n_mx_edi_cfdi_state')
    def _compute_custom_cfdi_values(self):
        # Iteraremos a través de los registros para aplicar cálculos.
        for record in self:
            # Utilice el método estándar de Odoo V18 para obtener todos los valores del informe
            # Este método ya maneja la decodificación del XML CFDI
            cfdi_report_values = record._l10n_mx_edi_get_extra_invoice_report_values()

            if cfdi_report_values:
                record.sello_sat = cfdi_report_values.get('sello_sat')
                record.serial_number = cfdi_report_values.get('certificate_number')
                record.sello_cfdi = cfdi_report_values.get('sello') # 'sello' es la clave en V18
                record.cfdi_cadena = cfdi_report_values.get('cadena') # 'cadena' es la clave en V18
                record.payment_method = cfdi_report_values.get('payment_way') # 'payment_way'  en V18 es el método formateado
            else:
                # Establecer valores predeterminados/vacíos si no se encuentran datos CFDI
                record.sello_sat = False
                record.serial_number = False
                record.sello_cfdi = False
                record.cfdi_cadena = False
                record.payment_method = False

    # Este método sigue siendo en gran medida el mismo, ya que se ocupa de los campos de dirección del socio.
    # que suelen ser estables.
    def get_address_partner(self):
        self.ensure_one()
        return {
            'colony': self.partner_id.l10n_mx_edi_colony or '',
            'city': self.partner_id.city or '',
            'zip': self.partner_id.zip or '',
            'street_name': self.partner_id.street_name or '',
            'number1': self.partner_id.street_number or '',
            'number2': self.partner_id.street_number2 or '',
            'vat': self.partner_id.vat or '',
            'phone': self.partner_id.phone or '',
            'state': self.partner_id.state_id.name if self.partner_id.state_id else '', # Compruebe primero el state_id
            'fiscal_regime': self.partner_id.l10n_mx_edi_fiscal_regime or ''
        }

    # Este método sigue siendo en gran medida el mismo.
    def get_cfdi_related_1(self):
        self.ensure_one()
        # En V18, no se utiliza l10n_mx_edi_origin para documentos relacionados cambia a l10n_mx_edi_cfdi_origin, 
        # por lo que con este cambio debería funcionar bien.
        if not self.l10n_mx_edi_cfdi_origin:
            return {}
        origin = self.l10n_mx_edi_cfdi_origin.split('|')
        uuids = origin[1].split(',') if len(origin) > 1 else []
        return {
            'type': origin[0],
            'related': [u.strip() for u in uuids],
        }