# -*- coding: utf-8 -*-
from odoo import http

# class EuromineralCustom(http.Controller):
#     @http.route('/euromineral_custom/euromineral_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/euromineral_custom/euromineral_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('euromineral_custom.listing', {
#             'root': '/euromineral_custom/euromineral_custom',
#             'objects': http.request.env['euromineral_custom.euromineral_custom'].search([]),
#         })

#     @http.route('/euromineral_custom/euromineral_custom/objects/<model("euromineral_custom.euromineral_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('euromineral_custom.object', {
#             'object': obj
#         })