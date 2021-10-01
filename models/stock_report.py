# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class StockReport(models.Model):
    _inherit = "stock.report"

    brand_id = fields.Many2one('product.brand', 'Brand', readonly=True)

    def _select(self):
        return super(StockReport, self)._select() + ", t.brand_id as brand_id"

    def _group_by(self):
        return super(StockReport, self)._group_by() + ", t.brand_id"
