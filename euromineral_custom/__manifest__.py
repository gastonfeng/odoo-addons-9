# -*- coding: utf-8 -*-
{
    'name': "Euromineral Ukraine Custom Module",
    'summary': """Euromineral Ukraine Custom Module""",
    'description': """Euromineral Ukraine Custom Module""",
    'author': 'ERP Ukraine',
    'website': 'https://erp.co.ua',
    'support': 'support@erp.co.ua',
    'license': 'AGPL-3',
    'category': 'Sales',
    'depends': ['mrp', 'sale_stock', 'delivery'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
