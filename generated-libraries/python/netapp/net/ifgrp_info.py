from netapp.netapp_object import NetAppObject

class IfgrpInfo(NetAppObject):
    """
    ifgrp name, type, and components.
    """
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        The interface name.
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _links = None
    @property
    def links(self):
        """
        array of interface names in interface group.
        An ifgrp with no members is possible.
        """
        return self._links
    @links.setter
    def links(self, val):
        if val != None:
            self.validate('links', val)
        self._links = val
    
    _favored = None
    @property
    def favored(self):
        """
        interface that is favored.
        Only applies if ifgrp-type = single.
        """
        return self._favored
    @favored.setter
    def favored(self, val):
        if val != None:
            self.validate('favored', val)
        self._favored = val
    
    _ifgrp_type = None
    @property
    def ifgrp_type(self):
        """
        Possible values: [single|multi|lacp].
        """
        return self._ifgrp_type
    @ifgrp_type.setter
    def ifgrp_type(self, val):
        if val != None:
            self.validate('ifgrp_type', val)
        self._ifgrp_type = val
    
    _ifgrp_policy = None
    @property
    def ifgrp_policy(self):
        """
        Possible values: [rr|mac|ip|port|single].  Default is ip.
        """
        return self._ifgrp_policy
    @ifgrp_policy.setter
    def ifgrp_policy(self, val):
        if val != None:
            self.validate('ifgrp_policy', val)
        self._ifgrp_policy = val
    
    _nofavored = None
    @property
    def nofavored(self):
        """
        interface that is not favored.
        Only applies if ifgrp-type = single.
        """
        return self._nofavored
    @nofavored.setter
    def nofavored(self, val):
        if val != None:
            self.validate('nofavored', val)
        self._nofavored = val
    
    @staticmethod
    def get_api_name():
          return "ifgrp-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'interface-name',
            'links',
            'favored',
            'ifgrp-type',
            'ifgrp-policy',
            'nofavored',
        ]
    
    def describe_properties(self):
        return {
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'links': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'favored': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ifgrp_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ifgrp_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nofavored': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
