from .base import *

ALLOWED_HOSTS = [
    "{}.nl".format(env('DOMAIN')),
    "www.{}.nl".format(env('DOMAIN')),
]

EMAIL_SUBJECT_PREFIX += "[PRODUCTION] "
