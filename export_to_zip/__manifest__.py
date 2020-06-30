# Copyright (C) 2020 Suwat Ueng-amnuaiphon
# 
# "Export to ZIP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# "Export to ZIP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with "Export to ZIP. If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-
{
    'name': "Export to ZIP",
    'description': """
        For Export multi-report as ZIP
    """,

    'author': "Suwat Ueng-amnuaiphon, Odoo Community Association (OCA)",
    'website': "https://github.com/suwatuanp",
    'category': 'Reporting',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'views/webclient_templates.xml',
    ],

}