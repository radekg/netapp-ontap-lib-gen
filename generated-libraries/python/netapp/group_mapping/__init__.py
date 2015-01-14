from netapp.connection import NaConnection
from group_mapping_info import GroupMappingInfo # 5 properties
from group_mapping_get_iter_key_td import GroupMappingGetIterKeyTd # 3 properties

class GroupMappingConnection(NaConnection):
    
    def group_mapping_swap(self, position, direction, with_position):
        """
        Swap the position of one group mapping with another. The position
        is the place in the sequence of group mappings in which the
        mappings are applied.
        
        :param position: Position of an existing group mapping in the list of group
                mappings for this Vserver.
        
        :param direction: Direction in which the group mapping is applied.
        
        :param with_position: Position of an existing group mapping entry in the list of group
                mappings for this Vserver. This entry will be swapped with the
                entry at 'position'.
        """
        return self.request( "group-mapping-swap", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'None' ], False ],
            'with_position': [ with_position, 'with-position', [ int, 'None' ], False ],
        }, {
        } )
    
    def group_mapping_insert(self, position, direction, replacement, pattern):
        """
        Insert a group mapping into the table at a specified position.
        
        :param position: Position within the set of group mappings that this new mapping
                will take. If a mapping already exists at this position, it will
                be moved to the next position in the list.
        
        :param direction: Direction of the group mapping to be inserted.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        
        :param replacement: The name that is to be used as a replacement if the pattern
                associated with this entry matches. The replacement may be a
                string containing escape sequences representing subexpressions
                from the pattern, as in the UNIX 'sed' program.
        
        :param pattern: Pattern to use to match the name while searching for a name that
                can be used as a replacement. The pattern is a UNIX-style regular
                expression. Regular expressions are case-insensitive when mapping
                from Windows to UNIX, and they are case-sensitive for mappings
                from Kerberos to UNIX and UNIX to Windows.
        """
        return self.request( "group-mapping-insert", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
            'replacement': [ replacement, 'replacement', [ basestring, 'None' ], False ],
            'pattern': [ pattern, 'pattern', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def group_mapping_modify(self, position, direction, replacement=None, pattern=None):
        """
        Modify an existing group mapping entry.
        
        :param position: Position of an existing group mapping in the list of group
                mappings for this Vserver.
        
        :param direction: Direction in which the group mapping is applied.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        
        :param replacement: The group that is to be used as a replacement if the pattern
                associated with this entry matches. The replacement is a string
                containing escape sequences representing subexpressions from the
                pattern, as in the UNIX 'sed' program.
        
        :param pattern: Pattern to use to match the group while searching for a group
                that can be used as a replacement. The pattern is a UNIX-style
                regular expression. Regular expressions are case-insensitive when
                mapping from Windows to UNIX, and they are case-sensitive for
                mappings from Kerberos to UNIX and UNIX to Windows.
        """
        return self.request( "group-mapping-modify", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
            'replacement': [ replacement, 'replacement', [ basestring, 'None' ], False ],
            'pattern': [ pattern, 'pattern', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def group_mapping_create(self, position, direction, replacement, pattern, return_record=None):
        """
        Create a new group mapping for a Vserver.
        
        :param position: Position of an existing group mapping in the list of group
                mappings for this Vserver.
        
        :param direction: Direction in which the group mapping is applied.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        
        :param replacement: The group that is to be used as a replacement if the pattern
                associated with this entry matches. The replacement is a string
                containing escape sequences representing subexpressions from the
                pattern, as in the UNIX 'sed' program.
        
        :param pattern: Pattern to use to match the group while searching for a group
                that can be used as a replacement. The pattern is a UNIX-style
                regular expression. Regular expressions are case-insensitive when
                mapping from Windows to UNIX, and they are case-sensitive for
                mappings from Kerberos to UNIX and UNIX to Windows.
        
        :param return_record: If set to true, returns the group-mapping on successful
                creation.
                Default: false
        """
        return self.request( "group-mapping-create", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
            'replacement': [ replacement, 'replacement', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'pattern': [ pattern, 'pattern', [ basestring, 'None' ], False ],
        }, {
            'result': [ GroupMappingInfo, False ],
        } )
    
    def group_mapping_delete(self, position, direction):
        """
        Delete an existing group mapping entry.
        
        :param position: Position of an existing group mapping in the list of group
                mappings for this Vserver.
        
        :param direction: Direction in which the group mapping is applied.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        """
        return self.request( "group-mapping-delete", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
        }, {
        } )
    
    def group_mapping_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of group mappings in the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                group-mapping object.
                All group-mapping objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "group-mapping-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ GroupMappingInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ GroupMappingInfo, 'None' ], False ],
        }, {
            'attributes-list': [ GroupMappingInfo, True ],
        } )
