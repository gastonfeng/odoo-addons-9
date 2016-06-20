# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import UserError

import base64


class P24AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.multi
    @api.depends('payment_type', 'journal_id', 'payment_method_id')
    def _compute_hide_p24b(self):
        for rec in self:
            if not rec.journal_id:
                rec.hide_p24b = True
                return
            if rec.payment_type == 'outbound':
                if rec.payment_method_id:
                    if rec.payment_method_id.code == 'p24b':
                        rec.hide_p24b = False
                        return
            rec.hide_p24b = True
            return

    hide_p24b = fields.Boolean(compute='_compute_hide_p24b')

    @api.multi
    def p24_payment_export(self):
        for rec in self:
            login = ''
            passwd = ''
            if not rec.journal_id.bank_acc_number:
                raise UserError(_(u'Provide account number on bank journal!'))
            if rec.journal_id.p24_login:
                login = base64.b64decode(rec.journal_id.p24_login)
            if rec.journal_id.p24_passwd:
                passwd = base64.b64decode(rec.journal_id.p24_passwd)
            if not rec.partner_id:
                raise UserError(_(u'Provide partner!'))

            if not rec.partner_id.bank_ids[0]:
                raise UserError(_(u'Provide partner bank!'))
            bank = rec.partner_id.bank_ids[0]
            if not bank.acc_number or not bank.bank_name or not bank.bank_bic:
                raise UserError(_(u'Provide partner bank info!'))
            if not rec.partner_id.company_registry:
                raise UserError(_(u'Provide partner code!'))
            # fill journal, part, amount, memo, date
            initial_values = {
                'journal_id': rec.journal_id.id,
                'bank_acc': rec.journal_id.bank_acc_number,
                'state': 'success',
                'task': 'send_payment',
                'partner_id': rec.partner_id.id,
                'amount': rec.amount,
                'currency_id': rec.currency_id.id,
                'payment_date': rec.payment_date,
                'memo': rec.communication,
                'login': login,
                'passwd': passwd
            }

            p24b = self.env['account.p24b.sync'].create(initial_values)
            return p24b.do_sync()
