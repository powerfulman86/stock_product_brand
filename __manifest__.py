# -*- coding: utf-8 -*-
{
    'name': "Stock Product Brand",

    'summary': """
        Stock Product Brand""",

    'description': """
        add brand attribute to products
    """,

    'author': "CubicIt Egypt",

    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'account', 'sale', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand_view.xml',
        'views/product_template.xml',
        'views/stock_quant.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
