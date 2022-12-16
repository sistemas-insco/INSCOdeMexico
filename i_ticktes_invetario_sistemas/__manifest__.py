# -*- coding: utf-8 -*-
{
    'name': "INSCO | SOPORTE TI",
    'summary': """
        Insco Tickets, Inventario""",
    'description': """
INSCO | Soporte TI, Invenario TI
------------------------------
INSCO.
    """,
    'author': "Andres Gonzalez",
    'website': "https://www.inscomex.com",
    'category': 'rh',
    'version': '1.0',
    'depends': [
        'base',
        'mail',
        'hr'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'report/ticktes_inventario_sistemas_report.xml',
        'data/mail_template_ticket.xml',
        'data/base_automatizacion.xml',
        'views/view_equipo_computadora_mantenimiento.xml',
        'views/view_equipo_computadora.xml',
        'report/template_entrega_equipo.xml',
        'report/template_matenimiento.xml',
        
    ],
    'demo': [],
     'installable': True,
    'application': True,
     'license': 'LGPL-3',
}