from odoo import models, fields, api
import base64

CFDI_XSLT_CADENA_TFD = 'l10n_mx_edi/data/xslt/3.3/cadenaoriginal_TFD_1_1.xslt'


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    observations = fields.Text(
        string='Observaciones'
    )
    sello_cfdi = fields.Char(
        compute="_compute_cfdi_values"
    )
    sello_sat = fields.Char(
        compute="_compute_cfdi_values"
    )
    cfdi_cadena = fields.Char(
        compute='_compute_cfdi_values'
    )
    payment_method = fields.Char(
        compute="_compute_cfdi_values",
        string='Metodo pago'
    )

    serial_number = fields.Char(
        compute='_compute_cfdi_values'
    )


    @api.model
    def _get_l10n_mx_edi_cadena(self):
        self.ensure_one()
        # get the xslt path
        xslt_path = CFDI_XSLT_CADENA_TFD
        # get the cfdi as eTree
        try:
            cfdi = base64.decodestring(self.l10n_mx_edi_cfdi)
            cfdi = self.l10n_mx_edi_get_xml_etree(cfdi)
            cfdi = self.l10n_mx_edi_get_tfd_etree(cfdi)
            return self.l10n_mx_edi_generate_cadena(xslt_path, cfdi)
        except Exception as e:
            print(e)



    @api.depends('edi_document_ids')
    def _compute_cfdi_values(self):
        res = super(AccountInvoice, self)._compute_cfdi_values()
        for record in self:
            attachment_id = record._l10n_mx_edi_decode_cfdi()
            
            # record.l10n_mx_edi_cfdi_uuid = attachment_id.get('uuid')
            # record.l10n_mx_edi_cfdi_supplier_rfc = attachment_id.get('supplier_rfc')
            # record.l10n_mx_edi_cfdi_customer_rfc = attachment_id.get('customer_rfc')
            # record.l10n_mx_edi_cfdi_amount = attachment_id.get('amount_total')
            record.sello_sat = attachment_id.get('sello_sat')

            #certificate = attachment_id.get('noCertificado', attachment_id.get('NoCertificado'))
            #record.serial_number = certificate
            record.serial_number = attachment_id.get('certificate_number')
            record.sello_cfdi = attachment_id.get('sello', attachment_id.get('Sello', 'No identificado'))
            cfdi_cadena = record._get_l10n_mx_edi_cadena()
            record.cfdi_cadena = attachment_id.get('cadena')
            record.payment_method = attachment_id.get('payment_method')
        return res

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
            'fiscal_regime': self.partner_id.l10n_mx_edi_fiscal_regime or ''}




    def get_cfdi_related_1(self):
        self.ensure_one()
        if not self.l10n_mx_edi_origin:
            return {}
        origin = self.l10n_mx_edi_origin.split('|')
        uuids = origin[1].split(',') if len(origin) > 1 else []
        return {
            'type': origin[0],
            'related': [u.strip() for u in uuids],
            }