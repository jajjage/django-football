"""views"""
from django.contrib.auth.views import PasswordResetView

from core.constants import SITE_CONTEXT


class PasswordResetHtmlView(PasswordResetView):
    """override email templates"""

    html_email_template_name = "registration/password_reset_email.html"
    email_template_name = "registration/password_reset_email.txt"
    extra_context = SITE_CONTEXT
