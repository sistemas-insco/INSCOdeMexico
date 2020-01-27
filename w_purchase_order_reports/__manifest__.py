# -*- coding: utf-8 -*-
{
    'name': 'WEDOO | w_purchase_order_reports',

    'summary': "Custom format for purchase order reports",

    'description': """
    """,

    'author': 'TELEMATEL ©',
    'website': "https://www.telematel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase'
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        #'reports/inherit_purchase_stock_report.xml',
        'reports/inherit_purchase_report.xml',

    ],
    # only loaded in demonstration mode
   'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}