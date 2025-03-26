{
    'name': 'Didoseg Contacts',
    'version': '1.0',
    'description': 'Didoseg Contacts',
    'summary': 'Didoseg Contacts',
    'author': 'Soy Calidad',
    'website': 'https://www.soycalidad.com',
    'license': 'LGPL-3',
    'category': 'didoseg',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
