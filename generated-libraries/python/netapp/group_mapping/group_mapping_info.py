from netapp.netapp_object import NetAppObject

class GroupMappingInfo(NetAppObject):
    """
    group mapping configuration for Vservers. The possible sources of
    group mapping information and the order in which they are
    searched is determined by the Vserver's 'name-mapping-switch'
    option. If the 'name-mapping-switch' is set to 'file', the rules
    in this table are used to determine the mapping. Windows user
    groups, UNIX user groups and Kerberos principal groups can be
    three disjoint sets of groups. A mechanism is needed to map
    groups from one set to another when presenting ACLs across
    multiprotocol clients. Each group mapping entry represents one
    such map in a given direction. group mappings are done using
    standard UNIX style regular expressions for pattern replacement.
    For example if a configuration is required to convert any Windows
    user in the Windows domain name 'EXAMPLE' into a UNIX user with
    the same name in NIS, the direction entry should be set to
    'win-unix', the pattern string should be set to 'EXAMPLE\\(.+)'
    and the replacement string should be set to1412      :double
    backslash (\\) in the pattern matches a single backslash in the
    source name. The parentheses denote a subexpression but do not
    match any characters themselves. The 'period' matches any single
    character. The 'plus' matches one or more characters of the
    previous expression. The pattern 'EXAMPLE\\(.+)' matches
    'EXAMPLE\' followed by one or more of any character. In the
    replacement, '\1' refers to the string that the first
    subexpression matched. Assuming the Windows user 'EXAMPLE\user1',
    the replacement evaluates to 'user1'. If a mapping is required
    from Windows to UNIX and none of the name mapping entries match,
    the domain name is stripped from the the username and it is
    directly mapped to the UNIX user of the same name. Similarly if a
    mapping is required from a UNIX user to a Windows user and none
    of the name mapping entries match, the domain name is prefixed to
    the username and it is directly mapped to a Windows user of the
    same name.
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
    
    _vserver = None
    @property
    def vserver(self):
        """
        Specifies the Vserver for the group mapping.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _position = None
    @property
    def position(self):
        """
        Position of an existing group mapping in the list of
        group mappings for this Vserver.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._position
    @position.setter
    def position(self, val):
        if val != None:
            self.validate('position', val)
        self._position = val
    
    _direction = None
    @property
    def direction(self):
        """
        Direction in which the group mapping is applied.
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "krb_unix"  - Kerberos principal name to UNIX user
        name mapping,
        <li> "win_unix"  - Windows user name to UNIX user name
        mapping,
        <li> "unix_win"  - UNIX user name to Windows user name
        mapping
        </ul>
        """
        return self._direction
    @direction.setter
    def direction(self, val):
        if val != None:
            self.validate('direction', val)
        self._direction = val
    
    _replacement = None
    @property
    def replacement(self):
        """
        The group that is to be used as a replacement if the
        pattern associated with this entry matches. The
        replacement is a string containing escape sequences
        representing subexpressions from the pattern, as in the
        UNIX 'sed' program.
        Attributes: required-for-create, modifiable
        """
        return self._replacement
    @replacement.setter
    def replacement(self, val):
        if val != None:
            self.validate('replacement', val)
        self._replacement = val
    
    _pattern = None
    @property
    def pattern(self):
        """
        Pattern to use to match the group while searching for a
        group that can be used as a replacement. The pattern is a
        UNIX-style regular expression. Regular expressions are
        case-insensitive when mapping from Windows to UNIX, and
        they are case-sensitive for mappings from Kerberos to
        UNIX and UNIX to Windows.
        Attributes: required-for-create, modifiable
        """
        return self._pattern
    @pattern.setter
    def pattern(self, val):
        if val != None:
            self.validate('pattern', val)
        self._pattern = val
    
    @staticmethod
    def get_api_name():
          return "group-mapping-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'position',
            'direction',
            'replacement',
            'pattern',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'position': { 'class': int, 'is_list': False, 'required': 'optional' },
            'direction': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'replacement': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'pattern': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
