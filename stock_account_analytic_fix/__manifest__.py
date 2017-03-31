# -*- coding: utf-8 -*-
{
    'name': "stock_account_analytic_fix",


    'description': """
        stock_account_analytic_fix
    """,

    'author': "ERP Ukraine",
    'website': "https://erp.co.ua",


    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock_account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
