# -*- coding: utf-8 -*-
{
    'name': 'PrivatBank online synchronization',
    'author': 'ERP Ukraine',
    'website': 'https://erp.co.ua',
    'summary': u"Sync statements with PrivatBank online",
    'category': 'Accounting & Finance',
    'depends': ['account'],
    'version': '1.0',
    'description': """
This app enables online synchronization of
bank statement and payments with PrivatBank.
""",
    'auto_install': False,
    'demo': [],
    'data': [
        'wizard/p24b_bank_sync_wizard_view.xml',
        'views/account_journal_view.xml'
    ],
    'installable': True
}
