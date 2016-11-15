# -*- coding: utf-8 -*-

__author__ = "Anup Swamy Veena"
__license__ = "MIT"
__status__ = "Production"


from .tjson import tjson
from .Exceptions import ParseError

tjson = tjson()
loads = tjson.parse
dumps = tjson.generate
