# -*- coding: utf-8 -*-

from odoo import api, fields, models
from random import randint


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Brand', help='Select a brand for this product')

    def set_product_internal(self):
        code = str(randint(0, 999999)).zfill(6)
        product_id = self.env['product.product'].search([('default_code', '=', code)])
        if product_id:
            self.set_product_internal()
        else:
            return code

    @api.model
    def create(self, values):
        values['default_code'] = self.set_product_internal()
        return super(ProductTemplate, self).create(values)

    def write(self, values):
        if not self.default_code:
            values['default_code'] = self.set_product_internal()
        return super(ProductTemplate, self).write(values)
