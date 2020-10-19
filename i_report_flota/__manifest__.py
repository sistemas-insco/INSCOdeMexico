# -*- coding: utf-8 -*-
{
    'name': " INSCO | Reporte de entrega de vehiculos",

    'summary': "Reporte de entrega de vehiculos",

    'description': """
        modelo que agrega un reporte de imprecion en 
        el modulo de flota  
    """,

    'author': "Insco de México",
    'website': "http://www.inscomex.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Vehiculos',
    'version': '1.0',   

    # any module necessary for this one to work correctly
    'depends': ['base','fleet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report_flota.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': False,
}
