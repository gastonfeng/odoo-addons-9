# -*- coding: utf-8 -*-
from odoo import http

# class StockAccountAnalyticFix(http.Controller):
#     @http.route('/stock_account_analytic_fix/stock_account_analytic_fix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_account_analytic_fix/stock_account_analytic_fix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_account_analytic_fix.listing', {
#             'root': '/stock_account_analytic_fix/stock_account_analytic_fix',
#             'objects': http.request.env['stock_account_analytic_fix.stock_account_analytic_fix'].search([]),
#         })

#     @http.route('/stock_account_analytic_fix/stock_account_analytic_fix/objects/<model("stock_account_analytic_fix.stock_account_analytic_fix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_account_analytic_fix.object', {
#             'object': obj
#         })