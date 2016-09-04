# -*- coding: utf-8 -*-

from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp


class ASM_StockLocation(models.Model):
    _inherit = 'stock.location'

    valuation_analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account')


class ASM_StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.v7
    def _prepare_account_move_line(self,
                                   cr,
                                   uid,
                                   move,
                                   qty,
                                   cost,
                                   credit_account_id,
                                   debit_account_id,
                                   context=None):
        res = super(ASM_StockQuant, self)._prepare_account_move_line(
            cr,
            uid,
            move,
            qty,
            cost,
            credit_account_id,
            debit_account_id,
            context=context)

        if move.location_dest_id.valuation_in_account_id:
            res[0][2]['analytic_account_id'] = \
                move.location_dest_id.valuation_analytic_account_id and \
                move.location_dest_id.valuation_analytic_account_id.id or False

        return res

    @api.v8
    def _prepare_account_move_line(self,
                                   move,
                                   qty,
                                   cost,
                                   credit_account_id,
                                   debit_account_id):
        res = super(ASM_StockQuant, self)._prepare_account_move_line(
            move,
            qty,
            cost,
            credit_account_id,
            debit_account_id)

        if move.location_dest_id.valuation_in_account_id:
            res[0][2]['account_analytic_id'] = \
                move.location_dest_id.valuation_analytic_account_id and \
                move.location_dest_id.valuation_analytic_account_id.id or False

        return res

    @api.v7
    def _account_entry_move(self, cr, uid, quants, move, context=None):
        res = super(ASM_StockQuant, self)._account_entry_move(
            cr, uid, quants, move, context=context)

        location_obj = self.pool.get('stock.location')
        location_from = move.location_id
        location_to = quants[0].location_id
        company_from = location_obj._location_owner(
            cr, uid, location_from, context=context)
        company_to = location_obj._location_owner(
            cr, uid, location_to, context=context)
        # from WH to production
        if company_from == company_to and move.location_id.usage == 'internal':
            if move.location_dest_id.usage in ('production', 'inventory'):
                journal_id, acc_src, acc_dest, acc_valuation = \
                    self._get_accounting_data_for_valuation(
                        cr, uid, move, context=ctx)
                if location_to and location_to.usage in ('production', 'inventory'):
                    # goods returned
                    self._create_account_move_line(
                        cr, uid,
                        quants, move, acc_valuation, acc_src, journal_id,
                        context=ctx)
                else:
                    # direct move
                    self._create_account_move_line(
                        cr, uid,
                        quants, move, acc_valuation, acc_dest, journal_id,
                        context=ctx)
        # from production to WH
        if company_from == company_to and move.location_dest_id.usage == 'internal':
            if move.location_id.usage in ('production', 'inventory'):
                journal_id, acc_src, acc_dest, acc_valuation = \
                    self._get_accounting_data_for_valuation(
                        cr, uid, move, context=ctx)
                if location_from and location_from.usage in ('production', 'inventory'):
                    # goods returned
                    self._create_account_move_line(
                        cr, uid,
                        quants, move, acc_dest, acc_valuation, journal_id,
                        context=ctx)
                else:
                    # direct move
                    self._create_account_move_line(
                        cr, uid,
                        quants, move, acc_src, acc_valuation, journal_id,
                        context=ctx)

    @api.v8
    def _account_entry_move(self, quants, move):
        res = super(ASM_StockQuant, self)._account_entry_move(
            quants, move)

        location_obj = self.pool.get('stock.location')
        location_from = move.location_id
        location_to = quants[0].location_id
        company_from = location_obj._location_owner(location_from)
        company_to = location_obj._location_owner(location_to)
        # from WH to production
        if company_from == company_to and move.location_id.usage == 'internal':
            if move.location_dest_id.usage in ('production', 'inventory'):
                journal_id, acc_src, acc_dest, acc_valuation = \
                    self._get_accounting_data_for_valuation(move)
                if location_to and location_to.usage in ('production', 'inventory'):
                    # goods returned
                    self._create_account_move_line(
                        quants, move, acc_valuation, acc_src, journal_id)
                else:
                    # direct move
                    self._create_account_move_line(
                        quants, move, acc_valuation, acc_dest, journal_id)
        # from production to WH
        if company_from == company_to and move.location_dest_id.usage == 'internal':
            if move.location_id.usage in ('production', 'inventory'):
                journal_id, acc_src, acc_dest, acc_valuation = \
                    self._get_accounting_data_for_valuation(move)
                if location_from and location_from.usage in ('production', 'inventory'):
                    # goods returned
                    self._create_account_move_line(
                        quants, move, acc_dest, acc_valuation, journal_id)
                else:
                    # direct move
                    self._create_account_move_line(
                        quants, move, acc_src, acc_valuation, journal_id)
