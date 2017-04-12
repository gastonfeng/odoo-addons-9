# -*- coding: utf-8 -*-

from odoo import fields, models


class MrpProductionEeuromineral(models.Model):
    _inherit = 'mrp.production'

    product_qty_on_stock = fields.Float(
        # 'Quantity On Hand',
        related='product_id.qty_available'
    )
