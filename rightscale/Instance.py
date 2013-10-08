from XMLModel import XMLModel
from rightscale.util import ElementTreeValueOK

class Instance(XMLModel):

    _href = None
    _nickname = None
    _state = None
    _ip_address = None

    def __str__(self):
        return "<Instance '%s'>" % self.nickname

    @property
    def href(self):
        return self._href

    @href.setter
    @ElementTreeValueOK
    def href(self, value):
        self._href = value


    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    @ElementTreeValueOK
    def nickname(self, value):
        self._nickname = value
    
    @property
    def state(self):
        return self._state

    @state.setter
    @ElementTreeValueOK
    def state(self, value):
        self._state = value
    
    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    @ElementTreeValueOK
    def ip_address(self, value):
        self._ip_address = value



    ELEMENTS = {
        'href': href,
        'state': state,
        'nickname': nickname,
        'ip-address': ip_address,
    }


