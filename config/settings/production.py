from .base import *

ALLOWED_HOSTS = [
    "{}.nl".format(env('DOMAIN')),
    "{}.alpha.go2people.nl".format(env('DOMAIN')),
    "www.{}.nl".format(env('DOMAIN')),
    "alpha.go2people.nl",
]

EMAIL_SUBJECT_PREFIX += "[PRODUCTION] "
