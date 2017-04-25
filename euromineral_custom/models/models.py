# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MrpProductionEeuromineral(models.Model):
    _inherit = 'mrp.production'

    product_qty_on_stock = fields.Float(
        u'На складе',
        related='product_id.qty_available'
    )


class SaleOrderEM(models.Model):
    _inherit = 'sale.order'

    customer_city = fields.Char(u'Город')

    @api.onchange('partner_id')
    def _onchage_parnter_city(self):
        self.customer_city = self.partner_id.city


class StockPickingEM(models.Model):
    _inherit = 'stock.picking'

    customer_city = fields.Char(u'Город', related='sale_id.customer_city')
