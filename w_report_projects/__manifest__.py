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
{
    'name': 'TELEMATEL | Report projects',
    'author': 'TELEMATEL ©',
    'category': 'Extra Tools',
    'sequence': 50,
    'summary': "Report projects document",
    'website': 'https://www.telematel.com',
    'version': '1.0',
    'description': """
    """,
    'depends': [
        'base',
        'sale',
        'project',
        'w_document_mod'
    ],
    'data': [
        'report/template_project_task_equipment_delivery.xml',
        'report/template_project_task_service_order.xml',
        'report/template_project_task_reception_equipment.xml',
        'report/project_task_report.xml',
        'views/inherit_res_company_view.xml',
        'views/inherit_project_task_view.xml',
        'views/inherit_sale_order.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}
