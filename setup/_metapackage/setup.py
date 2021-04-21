import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-delivery-carrier",
    description="Meta package for oca-delivery-carrier Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-delivery_carrier_info',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)