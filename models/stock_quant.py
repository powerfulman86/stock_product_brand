from odoo import api, fields, models, _


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    brand_id = fields.Many2one(related='product_id.brand_id', readonly=True, store=True)


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    brand_id = fields.Many2one(related='product_id.brand_id', readonly=True, store=True)


class StockMove(models.Model):
    _inherit = 'stock.move'

    brand_id = fields.Many2one(related='product_id.brand_id', readonly=True, store=True)


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    brand_id = fields.Many2one(related='product_id.brand_id', readonly=True, store=True)


# class ReportStockQuantity(models.Model):
#     _inherit = 'report.stock.quantity'
#
#     # brand_id = fields.Many2one(related='product_id.brand_id', readonly=True, store=True)
#     brand_id = fields.Many2one('product.brand', compute="_compute_brand", store=True)
#
#     @api.depends('product_id')
#     def _compute_brand(self):
#         for rec in self:
#             rec.brand_id = rec.product_id.brand_id.id
