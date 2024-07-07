{
    'name': "Account Import",
    'description': """
        Actualizacion de precio de los productos de origen extranjero
    """,

    'author': "Tonny Velazquez Juarez",
    'website': "corner.store59@gmail.com",
    'category': 'account',
    "version": '15.0.1.0.0',
    'depends': ['analytic', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_analytic_account_views.xml',
        # 'views/templates.xml',
    ],
    "license": "Other proprietary",
}
