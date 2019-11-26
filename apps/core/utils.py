"""Helper functions and utilities, used throughout the project"""


def setup_view(view, request, *args, **kwargs):
    """
    For class based views.
    Mimic ``as_view()``, but returns view instance.
    Use this function to get view instances on which you can run unit tests,
    by testing specific methods.

    From: https://bit.ly/2NOmZgA
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view
