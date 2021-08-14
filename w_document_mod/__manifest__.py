# -*- coding: utf-8 -*-
{
    'name': "WEDOO | Wedoo Document Modific",
    'summary': """
        Wedoo Document Modific for INSCO""",
    'description': """
WEDOO | Wedoo Document Modific
------------------------------
Wedoo addons to modificate documents for INSCO.
    """,
    'author': "INSCO©",
    'website': "https://www.inscomex.com",
    'category': 'Sales',
    'version': '1.0',
    'depends': [
        'base',
        'sale',
        'account',
        'l10n_mx_edi'
    ],
    'data': [
        'views/inherit_res_company_view.xml',
        'report/_inherit_sale_report_templates.xml',
        'report/_inherit_account_invoice_report_templates.xml',
        'views/inherit_sale_order_view.xml',
        'views/inherit_product_view.xml',
        'views/inherit_res_config_settings.xml',
        'views/inherit_account_invoice_view.xml',
    ],
    'demo': [
    ],
}