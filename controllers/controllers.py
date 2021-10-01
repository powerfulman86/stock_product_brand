# -*- coding: utf-8 -*-
# from odoo import http


# class StockProductBrand(http.Controller):
#     @http.route('/stock_product_brand/stock_product_brand/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_product_brand/stock_product_brand/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_product_brand.listing', {
#             'root': '/stock_product_brand/stock_product_brand',
#             'objects': http.request.env['stock_product_brand.stock_product_brand'].search([]),
#         })

#     @http.route('/stock_product_brand/stock_product_brand/objects/<model("stock_product_brand.stock_product_brand"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_product_brand.object', {
#             'object': obj
#         })
