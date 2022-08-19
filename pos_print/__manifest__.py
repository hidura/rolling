# -*- coding: utf-8 -*-
{
    'name': "POSPrinter",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "OikosChain",
    'website': "http://www.oikoschain.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],'assets':
    {
        'point_of_sale.assets':[
            'pos_print/static/src/js/Screens/ProductScreen/ControlButtons/PrintKitchenButton.js',
            'RestaurantPOS/static/src/js/Screens/ProductScreen/ProductScreen.js',
            'RestaurantPOS/static/src/js/models.js',
        ]
    }
}
