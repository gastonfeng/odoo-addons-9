# -*- coding: utf-8 -*-
{
    'name': 'PrivatBank online synchronization',
    'author': 'ERP Ukraine',
    'website': 'https://erp.co.ua',
    'summary': u"Онлайн синхронізація з ПриватБанком",
    'category': 'Accounting & Finance',
    'depends': ['account'],
    'version': '1.0',
    'description': """
Цей додаток дозволяє синхронізувати виписку та платежі
з ПриватБанком у режимі онлайн.
""",
    'auto_install': False,
    'demo': [],
    'data': ['wizard/p24b_bank_sync_wizard_view.xml'],
    'installable': True
}
