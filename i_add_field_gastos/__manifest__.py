# -*- coding: utf-8 -*-
{
    'name': "INSCO | Campos para Gastos",
    'summary': """
        Insco Gastos Modific for INSCO""",
    'description': """
INSCO | Insco Gastos Modific
------------------------------
modificate gastos for INSCO.
    """,
    'author': "Andres Gonzalez",
    'website': "https://www.inscomex.com",
    'category': 'Sales',
    'version': '1.0',
    'depends': [
        'base',
        'hr_expense'
    ],
    'data': [
        'views/inherit_gastos_view_from.xml',
        'views/inherit_gastos_view_tree.xml',
    ],
    'demo': [
    ],
}