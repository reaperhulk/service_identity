"""
Verify service identities.
"""

from __future__ import absolute_import, division, print_function

from . import pyopenssl
from .exceptions import (
    CertificateError,
    VerificationError,
)


__version__ = "15.0.0.dev0"

__title__ = "service_identity"
__description__ = "Service identity verification for pyOpenSSL."
__keywords__ = "cryptography openssl pyopenssl"
__uri__ = "https://github.com/pyca/service_identity"

__author__ = "Hynek Schlawack"
__email__ = "hs@ox.cx"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2014-2015 Hynek Schlawack"


__all__ = [
    "CertificateError",
    "VerificationError",
    "pyopenssl",
]
