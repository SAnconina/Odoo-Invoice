# coding: utf-8
{
    'name': "DEVXOPS INVOICE CUSTOM",
    'summary': """
        DEVXOPS INVOICE""",
    'description': """
        Description de votre module""",
    'author': "DevXOps",
    'website': "https://www.devxopslabs.com",
    'category': 'Accounting',
    'version': '16.0',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move_view.xml',
        'views/account_move_form.xml',
    ],
    'application': True,
    'icon': ''
}