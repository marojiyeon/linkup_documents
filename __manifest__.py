# -*- coding: utf-8 -*-
{
    'name': "linkup_documents",

    'summary': """""",

    'description': """""",

    'author': "link-up",
    'website': "http://www.link-up.co.kr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'documents',],

    # always loaded
    'data': [
        'views/documents_views.xml',
        'views/templates.xml',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'application': False
}