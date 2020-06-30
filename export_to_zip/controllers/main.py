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


from odoo.addons.web.controllers import main as report
from odoo.http import content_disposition, route, request
from odoo.tools.safe_eval import safe_eval

import json
import time


class ReportController(report.ReportController):
    @route()
    def report_routes(self, reportname, docids=None, converter=None, **data):
        print('converter', converter)
        if converter == 'zip':
            report = request.env['ir.actions.report']._get_report_from_name(
                reportname)
            context = dict(request.env.context)
            if docids:
                docids = [int(i) for i in docids.split(',')]
            if data.get('options'):
                data.update(json.loads(data.pop('options')))
            zipfile = report.with_context(context).render_zip(
                docids, data=data
            )[0]
            filename = "%s.%s" % (report.name, "zip")
            if docids:
                obj = request.env[report.model].browse(docids)
                if report.print_report_name and not len(obj) > 1:
                    report_name = safe_eval(
                        report.print_report_name,
                        {'object': obj, 'time': time, 'multi': False})
                    filename = "%s.%s" % (report_name, "zip")
                elif report.print_report_name and len(obj) > 1:
                    report_name = safe_eval(
                        report.print_report_name,
                        {'objects': obj, 'time': time, 'multi': True})
                    filename = "%s.%s" % (report_name, "zip")
            ziphttpheaders = [
                ('Content-Type', 'text/zip'),
                ('Content-Length', len(zipfile)),
                (
                    'Content-Disposition',
                    content_disposition(filename)
                )
            ]
            return request.make_response(zipfile, headers=ziphttpheaders)
        return super(ReportController, self).report_routes(
            reportname, docids, converter, **data
        )
