
class ZabbixManagerConfigurationPolicy:
    """
    xabbix configuration Policy
    """
    def __init__(self):
        self._username = None
        self._password = None
        self._url = None


    @property
    def username(self):
        if self._username is None:
            raise ValueError("user name is not set")
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError(f"user name most be string instead {value} of type : {type(value)} ")
        self._username = value

    @property
    def password(self):
        if self._password is None:
            raise ValueError("password name is not set")
        return self._password

    @password.setter
    def password(self, value):
        if  not isinstance(value, str):
            raise ValueError(f"password most be string instead {value} of type : {type(value)} ")
        self._password = value

    @property
    def url(self):
        if self._url is None:
            raise ValueError("password name is not set")
        return self._url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise ValueError(f"password most be string instead {value} of type : {type(value)} ")
        self._url = value


