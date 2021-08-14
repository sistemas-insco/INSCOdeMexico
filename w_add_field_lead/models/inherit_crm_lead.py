# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Alan Guzmán
#               (age@wedoo.tech)
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
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

#     Refrencias
#     finance_type = fields.Selection([('short', 'Short term Ecopulse'), ('long', 'Long term Ecopulse')],
#         string='Type of financing')
    rpu = fields.Char('RPU', help='CFE Control number',size=20)
    cfe_name = fields.Char('CFE name', help='Customer name on the CFE receip')
    rpu_home = fields.Char('RPU home', help='Customer Address  on the CFE receip')
    url_locations = fields.Char(
        'Location', help='URL of the location of the property')
    no_smartsheet = fields.Char('Control Code', help='Control Code')
#     Datos Tecnicos
    inverter_band = fields.Selection(
        [('solar', 'Solar Edge'), ('fronius', 'Fronius'),
         ('ingeteam', 'Ingeteam'), ('emphase', 'Emphase'),
         ('huawei','Huawei'), ('other', 'Other'), ('outback', 'Outback')],
        string='Inverter band')
    inverter_model = fields.Selection([
        ('solar', 'Solar Edge'), ('fronius', 'Fronius'),
        ('ingeteam', 'Ingeteam'), ('emphase', 'Emphase'), ('other', 'Other')],
        string='Inverter model')
    measurement_sonsumption = fields.Selection([('envoy', 'Envoy'), ('neurio', 'Neurio'), ('meter', 'Meter'), ('egauge', 'EGauge'), ('any', 'Any')],
        string='Consumption Measurement')
    panel_band = fields.Selection([('solar', 'Solar'), ('jinko', 'Jinko'), ('tec', 'Solar Tec'), ('sun', 'Sun Power'), ('et', 'ET Solar'),('longi','Longi')],
        string='Panel Band')
    panel_potential = fields.Char('Panel Potential', help='Panel Potential')
    qty_panel = fields.Integer('Panel qty', help='Panel qty')
#     Documentacion
    oficial_id = fields.Binary("Oficial Indentification", attachment=True,
        help="Limited to 1024x1024px",)
    oficial_id_filename = fields.Char()
    cfe_receipt = fields.Binary("CFE receipt", attachment=True,
        help="Limited to 1024x1024px",)
    cfe_receipt_filename = fields.Char()
    predial = fields.Binary("Predial", attachment=True,
        help="Limited to 1024x1024px",)
    predial_filename = fields.Char()
    quotation = fields.Binary("Quotation", attachment=True,
        help="Limited to 1024x1024px",)
    quotation_filename = fields.Char()
#     Datos contabilidad
    inv_name = fields.Char('Billing name', help='Billing name')
    inv_mail = fields.Char('Billing mail', help='Billing mail')
    inv_home = fields.Char('Billing home', help='Billing home')
    rfc = fields.Char('RFC', help='RFC')
    use_cfi = fields.Char('RFC use', help='CFDI use')
    bank = fields.Char('Bank', help='Bank')
    account_number = fields.Char('Account number', help='Account number')
    card_digits = fields.Integer('Card digits', help='Card digits')
    way_pay = fields.Selection([('pue', 'Single exibition'), ('ppd', 'Partial pay')],
        string='Way to pay')
    method_pay = fields.Selection([('01', 'Cash'), ('02', 'Nominative Check'),('03', 'Electronic Background Transfer')],
        string='Payment method')
    currency_account_id = fields.Selection([('mxn:', 'Mexican Peso:'), ('usd:', 'American Dollar:')],
        string='Currency')
    exchange_rate = fields.Float('Exchange rate', help='Exchange rate')
#     Contratos y tramites
    ver_documents = fields.Boolean('Verification of documents', default=False)
    sing_documents = fields.Boolean('Sing of documents', default=False)
    sing_ecopulse_contract = fields.Boolean('Signed Ecopulse contract', default=False)
    start_process_cfe = fields.Boolean('Start process CFE', default=False)
    sing_cfe_agree = fields.Boolean('Signature CFE agreement', default=False)
    sing_obteined = fields.Boolean('CFE signatures were obtained in agreement signed by the client', default=False)
    achieve_order = fields.Boolean('Achieve Order No.', default=False)
    change_meter = fields.Boolean('Change of meter', default=False)
    delivery_agreement = fields.Boolean('Delivery copy of agreement', default=False)
    done_procedure = fields.Boolean('Finalize procedure', default=False)
#     Contabilidad
    data_verification = fields.Boolean('Data Verification', default=False)
    invoiced_collection = fields.Boolean('Invoice and collection', default=False)
    authorized_collection = fields.Boolean('Authorized collection, authorization of installation', default=False)
    collection_balance = fields.Boolean('Collection of balances', default=False)
    collection_completed = fields.Boolean('Collection completed', default=False)
#     Diseño
    awaiting_project = fields.Boolean('Awaiting project acceptance', default=False)
    performs_survey = fields.Boolean('Performs survey, reviews inventory and proposal', default=False)
    short_3d = fields.Boolean('Short 3d model and heliscope and location', default=False)
    review_authorization = fields.Boolean('Review with the client and authorization', default=False)
    engineering = fields.Boolean('Engineering', default=False)
    list_material = fields.Boolean('List of materials to winery', default=False)
    proccess_finish = fields.Boolean('Finish process', default=False)

#     Obras
    verify_collection = fields.Boolean('Verify collection', default=False)
    schedule_appointment = fields.Boolean('Schedule appointment with the client', default=False)
    notice_contractor = fields.Boolean('Notice to the contractor', default=False)
    start_work = fields.Boolean('Start of work', default=False)
    end_work = fields.Boolean('End work', default=False)
    physical_delivery = fields.Boolean('Physical delivery of work', default=False)

#     Financiamiento ecopulse corto plazo
    rfc_binary_short = fields.Binary("RFC5", attachment=True,
        help="Limited to 1024x1024px",)
    rfc_binary_short_filename = fields.Char()
    fico_calification_short = fields.Binary("FICO Formats", attachment=True,
        help="Limited to 1024x1024px",)
    fico_calification_short_filename = fields.Char()
    curp_binary_short = fields.Binary("CURP2", attachment=True,
        help="Limited to 1024x1024px",)
    curp_binary_short_filename = fields.Char()
    auth_installation_short = fields.Binary("Installation authorization", attachment=True,
        help="Limited to 1024x1024px",)
    auth_installation_short_filename = fields.Char()
#     Financiamiento ecopulse largo plazo
    rfc_binary_long = fields.Binary("RFC4", attachment=True,
        help="Limited to 1024x1024px",)
    rfc_binary_long_filename = fields.Char()
    fico_calification_long = fields.Binary("FICO Format", attachment=True,
        help="Limited to 1024x1024px",)
    fico_calification_long_filename = fields.Char()
    auth_installation_long = fields.Binary("Installation authorization2", attachment=True,
        help="Limited to 1024x1024px",)
    auth_installation_long_filename = fields.Char()
    rfc_legal_rep = fields.Binary("RFC legal representative", attachment=True,
        help="Limited to 1024x1024px",)
    rfc_legal_rep_filename = fields.Char()
    constitutive_act = fields.Binary("Constitutive Act", attachment=True,
        help="Limited to 1024x1024px",)
    constitutive_act_filename = fields.Char()
    power_legal_rep = fields.Binary("Power of the legal representative", attachment=True,
        help="Limited to 1024x1024px",)
    power_legal_rep_filename = fields.Char()
    two_month_account = fields.Binary("Two month account statement", attachment=True,
        help="Limited to 1024x1024px",)
    two_month_account_filename = fields.Char()
    guarantee_data = fields.Binary("Guarantee data", attachment=True,
        help="Limited to 1024x1024px",)
    guarantee_data_filename = fields.Char()
#     Financimiento FIDE
    rfc_fide = fields.Binary("RFC3", attachment=True,
        help="Limited to 1024x1024px",)
    rfc_fide_filename = fields.Char()
    credit_request = fields.Binary("Credit request", attachment=True,
        help="Limited to 1024x1024px",)
    credit_request_filename = fields.Char()
    auth_request_credit = fields.Binary("Authorization to request credit reports", attachment=True,
        help="Limited to 1024x1024px",)
    auth_request_credit_filename = fields.Char()
#     infonavit
    rfc_infonavit = fields.Binary("RFC2", attachment=True,
        help="Limited to 1024x1024px",)
    rfc_infonavit_filename = fields.Char()
    birth_certificate = fields.Binary("Birth certificate", attachment=True,
        help="Limited to 1024x1024px",)
    birth_certificate_filename = fields.Char()
    curp_infonavit = fields.Binary("CURP2", attachment=True,
        help="Limited to 1024x1024px",)
    curp_infonavit_filename = fields.Char()
    prequalification_infonavit = fields.Binary("Prequalification infonavit", attachment=True,
        help="Limited to 1024x1024px",)
    prequalification_infonavit_filename = fields.Char()
    credit_sic = fields.Binary("Credit application and SIC formats", attachment=True,
        help="Limited to 1024x1024px",)
    credit_sic_filename = fields.Char()
    workshop_know = fields.Binary("Constancy Workshop Know to decide", attachment=True,
        help="Limited to 1024x1024px",)
    workshop_know_filename = fields.Char()
    budget_shedule = fields.Binary("Budget and work schedule", attachment=True,
        help="Limited to 1024x1024px",)
    budget_shedule_filename = fields.Char()
    marriage_certificate = fields.Binary("Marriage certificate", attachment=True,
        help="Limited to 1024x1024px",)
    marriage_certificate_filename = fields.Char()


    #@api.multi
    def write(self, vals):
        stage_obj = self.env['crm.stage']
        for lead in self:
            if 'stage_id' in vals:
                stage_id = stage_obj.browse(vals.get('stage_id'))
                if lead.stage_id.control_id:
                    if not lead.no_smartsheet:
                        raise UserError(_('You do not have the ID control code enabled.'))
        return super(CrmLead, self).write(vals)


class CrmStage(models.Model):

    _inherit = 'crm.stage'

    control_id = fields.Boolean("Control Id", default=False)
