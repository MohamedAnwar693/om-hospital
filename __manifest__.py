# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """""",
    'sequence': -100,
    'description': """
        Long description of module's purpose
    """,

    'author': "Mohamed Anwar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'mail', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_views.xml',
        'wizard/appointment_report_view.xml',
        'wizard/all_patient_report_view.xml',
        'views/patient.xml',
        'views/sale.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/partner.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/report.xml',
        'report/appointment_details.xml',
        'report/all_patient_list.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
