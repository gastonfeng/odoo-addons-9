# -*- coding: utf-8 -*-

from odoo import fields, models


class PartnerST(models.Model):
    _inherit = 'res.partner'

    user_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user or False,
        help='''The internal user that is in charge of
                communicating with this contact if any.''')

    my_company_ids = fields.One2many(
        'res.company',
        'partner_id',
        string='My Company')
