# -*- coding: utf-8 -*-
{
    'name': "钉钉办公-回调管理",
    'summary': """钉钉办公-回调管理""",
    'description': """ 钉钉办公-回调管理 """,
    'author': "SuXueFeng",
    'website': "https://www.sxfblog.com",
    'category': 'dindin',
    'version': '1.0',
    'depends': ['base', 'ali_dindin'],
    'installable': True,
    'application': False,
    'auto_install': True,
    'data': [
        'security/ir.model.access.csv',
        'data/system_conf.xml',
        'data/call_back.xml',
        'views/call_back_list.xml',
        'views/call_back.xml',
    ],
    # 'qweb': [
    #     'static/xml/*.xml'
    # ]

}