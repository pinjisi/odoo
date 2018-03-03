# -*- coding: utf-8 -*-
{
    'name': "aps free disk space check 8.0",

    'summary': """
        This module checks for free server disk space""",

    'description': """
        This module is a cron job that runs evry 24hrs to check for free disk space.  If the free disk space is too low (less than 20%) an email will be sent to the company email address.  Otherwise an email with free disk space notification is sent on the 17th monthly
    """,

    'author': "A P Systems - Bill Made - billm@ap-accounting.co.za",
    'website': "http://www.ap-accounting.co.za",

    # Categories can be used to filter modules in modules listing
   
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'ir_cron.xml',
    ],
    
}