from unittest.mock import Mock

from django.test import TestCase

from tests.object_environment.factory import EnvironmentFactory


class UseCaseTestCase(TestCase, EnvironmentFactory):

    def setUp(self) -> None:
        self.listener = Mock()
        self.request = None

    def create_request(self, fields):
        return NotImplementedError()

    def run_use_case(self):
        raise NotImplementedError()

    def assertNotCalled(self, method):
        TestCase().assertFalse(method.called, '\n' + str(method) + '\nExpected: Not called\nActual: Called')

    def assertCalled(self, method):
        TestCase().assertTrue(method.called, '\n' + str(method) + '\nExpected: Called\nActual: Not called')

    def assertOnlyCalled(self, method):
        call_count = len(self.listener.method_calls)
        TestCase().assertTrue(method.called and call_count == 1,
                              "\nExpected: Only the method '" + str(method) + "' called"
                              + '\nActual: The methods ' + str(self.listener.method_calls) + ' were called')

    def assertMultipleOnlyCalled(self, *args, listener):
        method_calls = listener.method_calls
        call_count = len(method_calls)
        TestCase().assertTrue(call_count == len(args), self._display_methods(method_calls))
        for a in args:
            TestCase().assertTrue(a.called, self._display_methods(method_calls))

    def _display_methods(self, method_list, msg_before='', msg_after=''):
        msg = '\n'
        msg += msg_before + '\n'
        msg += 'Actual interactions with the listener:\n'
        msg += '________________________________________________________________\n'
        for m in method_list:
            msg += str(m) + '\n'
        msg += '_________________________________________________________________\n'
        msg += msg_after
        return msg
