'''
    Register the views here.
'''
from views.front import front_router
from views.accounts import accounts_router
from views.tests import test_router

routes = [
    front_router,
    accounts_router,
    test_router
]

def Routes():
    return routes