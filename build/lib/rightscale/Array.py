from XMLModel import XMLModel
from rightscale.util import ElementTreeValueOK

class Array(XMLModel):

    _href = None
    _nickname = None
    _deployment_href = None
    _server_template_ = None
    _active = None
    _array_type = None

    def __str__(self):
        return "<Array '%s'>" % self.nickname

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
    def deployment_href(self):
        return self._deployment_href

    @deployment_href.setter
    @ElementTreeValueOK
    def deployment_href(self, value):
        self._deployment_href = value

    
    @property
    def server_template(self):
        return self._server_template

    @server_template.setter
    @ElementTreeValueOK
    def server_template(self, value):
        self._server_template = value

    
    @property
    def active(self):
        return (self._active == "true")

    @active.setter
    @ElementTreeValueOK
    def active(self, value):
        self._active = value


    @property
    def array_type(self):
        return self._array_type

    @array_type.setter
    @ElementTreeValueOK
    def array_type(self, value):
        self._array_type = value
    

    ELEMENTS = {
        'href': href,
        'nickname': nickname,
        'deployment-href': deployment_href,
        'server-template-href': server_template,
        'active': active,
        'array-type': array_type
    }


