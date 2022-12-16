# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 INSCO - http://www.inscomex.com/
# All Rights Reserved.
#
# Developer(s): Andres Gonzalez
#               (sistemas@inscomexico.com)
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
{
    'name': 'INSCO | Permisos y Vacaciones',
    'author': 'Andres Gonzalez INSCO',
    'category': 'rh',
    'summary': "Menu Empleados permisos",
    'website': 'https://www.inscomex.com',
    'version': '1.0',
    'description': """
    """,
    'depends': [
        'base',
        'mail',
        'hr'
    ],
    'data': [
        'security/security.xml',
        'data/mail_template_solicitud.xml',
        'security/ir.model.access.csv',
        'views/view_solicitud_vacaciones.xml',
        'views/view_inherit_empelados.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}




























# -*- coding: utf-8 -*-
# {
#     'name': "INSCO | Menu para Empleados",
#     'summary': """
#         Permisos y vacaciones INSCO""",
#     'description': """
# INSCO | Insco Empleados
# ------------------------------
# Menu para solicitar permisos o vacaciones.
#     """,
#     'author': "Andres Gonzalez",
#     'website': "https://www.inscomex.com",
#     'category': 'rh',
#     'version': '1.0',
#     'depends': [
#         'base',
#         'mail',
#         'hr'
#     ],
#     'data': [
#         'security/security.xml',
#         'security/ir.model.access.csv',
#         'views/view_solicitud_vacaciones.xml',
#         'views/view_inherit_empelados.xml',
#     ],
#     'demo': [
#     ],
# }