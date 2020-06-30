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


from io import StringIO, BytesIO

from odoo import models
import os

import logging
_logger = logging.getLogger(__name__)

try:
    import zipfile
except ImportError:
    _logger.debug('Can not import zipfile`.')


class ReportZIPAbstract(models.AbstractModel):
    _name = 'report.export_to_zip.abstract'
    _description = 'Abstract Model for ZIP reports'

    def _get_objs_for_report(self, docids, data):
        """
        Returns objects for zip.  From WebUI these
        are either as docids taken from context.active_ids or
        in the case of wizard are in data.  Manual calls may rely
        on regular context, setting docids, or setting data.

        :param docids: list of integers, typically provided by
            qwebactionmanager for regular Models.
        :param data: dictionary of data, if present typically provided
            by qwebactionmanager for TransientModels.
        :param ids: list of integers, provided by overrides.
        :return: recordset of active model for ids.
        """
        if docids:
            ids = docids
        elif data and 'context' in data:
            ids = data["context"].get('active_ids', [])
        else:
            ids = self.env.context.get('active_ids', [])
        return self.env[self.env.context.get('active_model')].browse(ids)

    def create_zip_report(self, docids, data):
        print('=====zip=====', docids, data)
        objs = self._get_objs_for_report(docids, data)
        file_data = BytesIO()
        file = zipfile.ZipFile(file_data, mode="w",compression=zipfile.ZIP_DEFLATED)
        # file = self.zip_options(file, data)
        self.generate_zip_file(file, data, objs)
        file.close()
        print('getvalue', file_data.getvalue)
        file_data.seek(0)
        return file_data.read(), 'zip'

    # def zip_options(self, zip_file, data=None):
    #     """
    #     :return: zip. At least return 'zip', but
    #     you can optionally return parameters that zipfile.
    #     """
    #     return zip_file

    def generate_zip_file(self, file, data, objs):
        raise NotImplementedError()
