# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2020 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Santiago Dueñas <sduenas@bitergia.com>
#     Miguel Ángel Fernández <mafesan@bitergia.com>
#

import enum


@enum.unique
class ErrorCode(enum.Enum):
    """Error codes for Bestiary"""

    BASE_ERROR = 1
    ALREADY_EXISTS_ERROR = 2
    NOT_FOUND_ERROR = 3
    VALUE_ERROR = 4


class BaseError(Exception):
    """Base class error.

    Derived classes can overwrite error message declaring
    'message' property.
    """
    code = ErrorCode.BASE_ERROR
    message = "Bestiary unknown error"

    def __init__(self, **kwargs):
        super().__init__()
        self.msg = self.message % kwargs

    def __str__(self):
        return self.msg

    def __int__(self):
        return self.code


class AlreadyExistsError(BaseError):
    """Exception raised when an entity already exists in the registry"""

    message = "%(entity)s '%(eid)s' already exists in the registry"
    code = ErrorCode.ALREADY_EXISTS_ERROR

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entity = kwargs['entity']
        self.eid = kwargs['eid']


class NotFoundError(BaseError):
    """Exception raised when an entity is not found in the registry"""

    message = "%(entity)s not found in the registry"
    code = ErrorCode.NOT_FOUND_ERROR


class InvalidValueError(BaseError):
    """Exception raised when a value is invalid"""

    code = ErrorCode.VALUE_ERROR
    message = "%(msg)s"
