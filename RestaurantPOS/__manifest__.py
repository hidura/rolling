# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS Restaurant Driver',
    'version': '1.0',
    'sequence': 265,
    'category':"Sales",
    'author':'Oikos Chain Team',
    'depends': ['pos_sale', 'point_of_sale', 'sale', 'stock'],
    'summary': "POS handler for restaurant",
    'description': """
        The system that allows to create documents to be print in the local from the cloud system.
    """,
    'category': 'Sales',

    'data': [
        'views/productsVariants.xml',
        'views/pos_product.xml',
        'views/pos_config.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_qweb': [
            'RestaurantPOS/static/src/xml/**',
        ],
        'point_of_sale.assets':[
            'RestaurantPOS/static/src/js/Screens/ProductScreen/ControlButtons/PrintKitchenButton.js',
        ]
    }
}
