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
{
    'name': "WEDOO | Service Order Reports",
    'summary': "Service Order Reports",
    'description': """
WEDOO | Service Order Reports
-----------------------------

Service Order Reports for INSCO.
    """,
    'author': "WEDOO ©",
    'website': "https://wedoo.tech",
    'category': 'Sales',
    'version': '1.0',
    'depends': [
        'base',
        'web',
        'project',
        'w_report_projects'
    ],
    'data': [
        'views/web_assets.xml',
        'data/service_order_data.xml',
        'views/inherited_project_views.xml',
        'report/service_order_multi_template.xml',
        'report/service_order_multi_report.xml',
        'report/inherited_service_order_report.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
}

