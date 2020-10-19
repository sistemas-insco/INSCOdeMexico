# -*- coding: utf-8 -*-
# from odoo import http


# class IReportFlota(http.Controller):
#     @http.route('/i_report_flota/i_report_flota/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/i_report_flota/i_report_flota/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('i_report_flota.listing', {
#             'root': '/i_report_flota/i_report_flota',
#             'objects': http.request.env['i_report_flota.i_report_flota'].search([]),
#         })

#     @http.route('/i_report_flota/i_report_flota/objects/<model("i_report_flota.i_report_flota"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('i_report_flota.object', {
#             'object': obj
#         })
