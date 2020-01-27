# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2018 Wedoo - http://www.wedoo.tech/
# All Rights Reserved.
#
# Developer(s): Ernesto García Medina
#               (ernesto.garcia@telematel.com)
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
    'name': 'WEDOO | Create project from lead - some stages',
    'author': 'WEDOO ©',
    'category': 'Projects',
    'sequence': 50,
    'summary': "Projects from Lead",
    'website': 'https://www.wedoo.tech',
    'version': '1.0',
    'description': """
Create project from lead - some stages
======================================

    """,
    'depends': [
        'project',
        'crm',
        'hr'
    ],
    'installable': True,
    'data': [
        'views/crm_lead_views.xml',
        'views/project_task_views.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'qweb': [],
    'application': False,
}
