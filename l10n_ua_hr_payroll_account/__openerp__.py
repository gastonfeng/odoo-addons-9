# -*- encoding: utf-8 -*-
{
    'name': 'Ukrainian - Payroll with Accounting',
    'category': 'Localization',
    'depends': ['l10n_be_hr_payroll', 'hr_payroll_account', 'l10n_be'],
    'version': '1.0',
    'description': """
Accounting Data for Belgian Payroll Rules.
==========================================
    """,

    'auto_install': True,
    'website': 'https://www.odoo.com/page/accounting',
    'demo': [],
    'data': [
        'l10n_ua_hr_payroll_account_data.xml',
    ],
    'post_init_hook': '_set_accounts',
    'installable': True
}
