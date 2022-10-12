# pylint: disable=missing-module-docstring,missing-function-docstring
from packaging import version
try:
    from quart.__about__ import __version__ as quart_version
    QUART_VER_GT_09 = version.parse(quart_version) >= version.parse('0.9.0')
except ModuleNotFoundError as e:
    if e.name == 'quart.__about__':
        # Ignoring packaging bugs in super ancient versions, any release without this file
        # is newer than 0.9.0
        QUART_VER_GT_09 = True
    else:
        raise
import pytest
from quart_openapi import Pint


@pytest.fixture
def req_ctx():
    def func(testapp: Pint, page: str, method: str = ''):
        if QUART_VER_GT_09:
            return testapp.test_request_context(page, method=method)
        return testapp.test_request_context(method, page)
    return func

@pytest.fixture
def app():
    testapp = Pint('test', title='App Test', contact='foo',
                   contact_email='moo@bar.com', description='Sample Desc')
    return testapp
