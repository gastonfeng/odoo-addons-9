# -*- coding: utf-8 -*-

{
    'name': 'LiqPay Payment Acquirer',
    'category': 'Website',
    'summary': 'Payment Acquirer: LiqPay Implementation',
    'version': '1.2',
    # 'price': 100.00,
    # 'currency': 'EUR',
    'author': "ERP Ukraine",
    'website': "https://erp.co.ua",
    'description': """LiqPay Payment Acquirer""",
    'depends': ['payment', 'website_sale'],
    'data': [
        'views/liqpay.xml',
        'views/payment_liqpay.xml',
        'data/liqpay.xml',
    ],
    'installable': True,
}
