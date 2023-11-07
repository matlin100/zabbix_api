

class SwitchConnectConfiguration:

    """
    witch  connection configuration Policy
    """

    def __init__(self):
        self._juniper_success = []
        self._cisco_success = []
        self._failed_login = []

    @property
    def juniper_success(self):
        return self._juniper_success

    @juniper_success.setter
    def juniper_success(self, value):
        if isinstance(value, list):
            self.juniper_success.append(value)

        else:
            print("invalid data expected a list in juniper_success var")

    @property
    def cisco_success(self):
        return self._cisco_success

    @juniper_success.setter
    def cisco_success(self, value):
        if isinstance(value, list):
            self.cisco_success = value
        else:
            print("invalid data expected a list in cisco_success var")

    @property
    def failed_login(self):
        return self._failed_login

    @juniper_success.setter
    def failed_login(self, value):
        if isinstance(value, list):
            self._failed_login = value
        else:
            print("invalid data expected a list in failed_login var")

