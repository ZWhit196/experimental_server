'''
    Register the views here.
'''
from views.front import front_router
from views.accounts import accounts_router
from views.tests import test_router

dev_routes = [
    front_router,
    accounts_router,
    test_router
]

routes = [
    front_router,
    accounts_router
]

def Routes(dev=False):
    if dev:
        return dev_routes
    return routes