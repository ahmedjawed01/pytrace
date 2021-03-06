# Copyright (c) Django Software Foundation and individual contributors.
# All rights reserved.

# Taken from Django Framework (https://www.djangoproject.com)
# and modified based on usecase by Adnan Umer <u.adnan@outlook.com>
# See LICENSE.django for complete Django Framework license

from __future__ import absolute_import

from importlib import import_module
import sys
import six


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by
    the last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        msg = "%s doesn't look like a module path" % dotted_path
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError:
        msg = 'Module "%s" does not define a "%s" attribute/class' % (
            dotted_path, class_name)
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])
