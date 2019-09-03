"""core views"""

from django.shortcuts import render
from django.views import View


class BaseView(View):
    """Base view"""

    @property
    def template_name(self):
        """required attribute"""
        return NotImplemented

    @classmethod
    def get_context(cls):
        """required method"""
        return NotImplemented

    def get(self, request, *args, **kwargs):
        """retrieve context and render template"""
        context = self.get_context()
        return render(request, self.template_name, context)

