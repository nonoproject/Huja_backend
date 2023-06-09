# -*- coding: utf-8 -*-
{
    'name': "Huja",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/city.xml',
        'views/area.xml',
        'views/home_services.xml',
        'views/trip_services.xml',
        'views/water_services.xml',
        'views/medicine.xml',
        'views/missing_people_services.xml',
        'views/phone_balance_services.xml',
        'views/doctor_services.xml',
        'views/fuel_services.xml',
        'views/electricity_service.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
