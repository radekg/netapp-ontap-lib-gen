from netapp.netapp_object import NetAppObject

class AutosupportCompliantInfo(NetAppObject):
    """
    Compliant AutoSupport has data
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _node = None
    @property
    def node(self):
        """
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _plaintext = None
    @property
    def plaintext(self):
        """
        Plaintext
        Attributes: key, non-creatable, non-modifiable
        """
        return self._plaintext
    @plaintext.setter
    def plaintext(self, val):
        if val != None:
            self.validate('plaintext', val)
        self._plaintext = val
    
    _hash = None
    @property
    def hash(self):
        """
        hash
        Attributes: non-creatable, non-modifiable
        """
        return self._hash
    @hash.setter
    def hash(self, val):
        if val != None:
            self.validate('hash', val)
        self._hash = val
    
    _last_used_sequence = None
    @property
    def last_used_sequence(self):
        """
        Last AutoSupport that used this hash
        Attributes: non-creatable, non-modifiable
        """
        return self._last_used_sequence
    @last_used_sequence.setter
    def last_used_sequence(self, val):
        if val != None:
            self.validate('last_used_sequence', val)
        self._last_used_sequence = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-compliant-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'plaintext',
            'hash',
            'last-used-sequence',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'plaintext': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hash': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_used_sequence': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
