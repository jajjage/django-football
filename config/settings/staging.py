from .base import *

ALLOWED_HOSTS = [
    "{}.test.go2people.nl".format(env('DOMAIN')),
]

EMAIL_SUBJECT_PREFIX += "[STAGING] "
