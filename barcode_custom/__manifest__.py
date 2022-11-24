# -*- coding: utf-8 -*-
{
    'name': "barcode_custom",

    'summary': """
        Smart solution for medical barcode""",

    'description': """
        new feature for medical barcode once you use the app will change in inventory to be similar as medical systems 
    """,

    'author': "IT ZAIN",
    'website': "https://itzain.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],

}
