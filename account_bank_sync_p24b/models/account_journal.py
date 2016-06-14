# -*- coding: utf-8 -*-

from openerp import models, fields, api


class P24AccountJournal(models.Model):
    _inherit = "account.journal"

    bank_statements_source = fields.Selection(
        selection_add=[('p24b_import', 'Privat24Business Import')])

    @api.multi
    def p24b_sync_statement(self):
        if not self.bank_acc_number:
            raise UserError(_(u'Provide account number on bank journal!'))

        initial_values = {
            'journal_id': self.id,
            'bank_acc': self.bank_acc_number,
            'state': 'success',
            'task': 'statement_import',
            'login': '',
            'passwd': ''
        }

        p24b = self.env['account.p24b.sync'].create(initial_values)
        return p24b.do_sync()
