from netapp.connection import NaConnection
from unix_user_info import UnixUserInfo # 5 properties
from name_mapping_direction import NameMappingDirection # 0 properties
from name_mapping_info import NameMappingInfo # 5 properties
from unix_group_info import UnixGroupInfo # 4 properties
from name_mapping_unix_user_get_iter_key_td import NameMappingUnixUserGetIterKeyTd # 2 properties
from name_mapping_unix_group_get_iter_key_td import NameMappingUnixGroupGetIterKeyTd # 2 properties
from unix_user_name import UnixUserName # 1 properties
from name_mapping_get_iter_key_td import NameMappingGetIterKeyTd # 3 properties

class NameMappingConnection(NaConnection):
    
    def name_mapping_delete(self, position, direction):
        """
        Delete an existing name mapping entry.
        
        :param position: Position of an existing name mapping in the list of name mappings
                for this Vserver.
        
        :param direction: Direction in which the name mapping is applied.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        """
        return self.request( "name-mapping-delete", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
        }, {
        } )
    
    def name_mapping_unix_group_modify(self, group_name, group_id=None):
        """
        Modify the attributes of a UNIX group.
        
        :param group_name: Specifies UNIX group name.
        
        :param group_id: Specifies an identification number for the UNIX group.
        """
        return self.request( "name-mapping-unix-group-modify", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'group_id': [ group_id, 'group-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_insert(self, position, direction, replacement, pattern):
        """
        Insert a name mapping into the table at a specified position.
        
        :param position: Position within the set of name mappings that this new mapping
                will take. If a mapping already exists at this position, it will
                be moved to the next position in the list.
        
        :param direction: Direction of the name mapping to be inserted.
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
        return self.request( "name-mapping-insert", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
            'replacement': [ replacement, 'replacement', [ basestring, 'None' ], False ],
            'pattern': [ pattern, 'pattern', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_unix_user_destroy(self, user_name):
        """
        Destroy an existing UNIX user.
        
        :param user_name: Specifies user's UNIX account name.
        """
        return self.request( "name-mapping-unix-user-destroy", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_unix_group_get(self, group_name, desired_attributes=None):
        """
        Get the attributes of a UNIX group.
        
        :param group_name: Specifies UNIX group name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "name-mapping-unix-group-get", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ UnixGroupInfo, 'None' ], False ],
        }, {
            'attributes': [ UnixGroupInfo, False ],
        } )
    
    def name_mapping_unix_group_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of UNIX groups.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                UNIX group information object.
                All UNIX group information objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "name-mapping-unix-group-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ UnixGroupInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ UnixGroupInfo, 'None' ], False ],
        }, {
            'attributes-list': [ UnixGroupInfo, True ],
        } )
    
    def name_mapping_modify(self, position, direction, replacement=None, pattern=None):
        """
        Modify an existing name mapping entry.
        
        :param position: Position of an existing name mapping in the list of name mappings
                for this Vserver.
        
        :param direction: Direction in which the name mapping is applied.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        
        :param replacement: The name that is to be used as a replacement if the pattern
                associated with this entry matches. The replacement is a string
                containing escape sequences representing subexpressions from the
                pattern, as in the UNIX 'sed' program.
        
        :param pattern: Pattern to use to match the name while searching for a name that
                can be used as a replacement. The pattern is a UNIX-style regular
                expression. Regular expressions are case-insensitive when mapping
                from Windows to UNIX, and they are case-sensitive for mappings
                from Kerberos to UNIX and UNIX to Windows.
        """
        return self.request( "name-mapping-modify", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
            'replacement': [ replacement, 'replacement', [ basestring, 'None' ], False ],
            'pattern': [ pattern, 'pattern', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of name mappings in the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                name-mapping object.
                All name-mapping objects matching this query up to 'max-records'
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
        return self.request( "name-mapping-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NameMappingInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NameMappingInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NameMappingInfo, True ],
        } )
    
    def name_mapping_unix_user_modify(self, user_name, full_name=None, user_id=None, group_id=None):
        """
        Modify the attributes of a UNIX user.
        
        :param user_name: Specifies user's UNIX account name.
        
        :param full_name: Specifies the full name of the UNIX user.
        
        :param user_id: Specifies an identification number for the UNIX user.
        
        :param group_id: Specifies the primary group identification number for the UNIX
                user.
        """
        return self.request( "name-mapping-unix-user-modify", {
            'full_name': [ full_name, 'full-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'user_id': [ user_id, 'user-id', [ int, 'None' ], False ],
            'group_id': [ group_id, 'group-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_unix_user_get(self, user_name, desired_attributes=None):
        """
        Get the attributes of a UNIX user.
        
        :param user_name: Specifies user's UNIX account name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "name-mapping-unix-user-get", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ UnixUserInfo, 'None' ], False ],
        }, {
            'attributes': [ UnixUserInfo, False ],
        } )
    
    def name_mapping_unix_group_create(self, group_name, group_id, return_record=None):
        """
        Create a new UNIX group.
        
        :param group_name: Specifies UNIX group name.
        
        :param group_id: Specifies an identification number for the UNIX group.
        
        :param return_record: If set to true, returns the UNIX group information on successful
                creation.
                Default: false
        """
        return self.request( "name-mapping-unix-group-create", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'group_id': [ group_id, 'group-id', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ UnixGroupInfo, False ],
        } )
    
    def name_mapping_unix_group_delete_user(self, group_name, user_name):
        """
        Delete a user from a UNIX group
        
        :param group_name: Specifies UNIX group name.
        
        :param user_name: Specifies user's UNIX account name.
        """
        return self.request( "name-mapping-unix-group-delete-user", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_create(self, position, direction, replacement, pattern, return_record=None):
        """
        Create a new name mapping for a Vserver.
        
        :param position: Position of an existing name mapping in the list of name mappings
                for this Vserver.
        
        :param direction: Direction in which the name mapping is applied.
                Possible values:
                <ul>
                <li> "krb_unix"  - Kerberos principal name to UNIX user name
                mapping,
                <li> "win_unix"  - Windows user name to UNIX user name
                mapping,
                <li> "unix_win"  - UNIX user name to Windows user name mapping
                </ul>
        
        :param replacement: The name that is to be used as a replacement if the pattern
                associated with this entry matches. The replacement is a string
                containing escape sequences representing subexpressions from the
                pattern, as in the UNIX 'sed' program.
        
        :param pattern: Pattern to use to match the name while searching for a name that
                can be used as a replacement. The pattern is a UNIX-style regular
                expression. Regular expressions are case-insensitive when mapping
                from Windows to UNIX, and they are case-sensitive for mappings
                from Kerberos to UNIX and UNIX to Windows.
        
        :param return_record: If set to true, returns the name-mapping on successful creation.
                Default: false
        """
        return self.request( "name-mapping-create", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'name-mapping-direction' ], False ],
            'replacement': [ replacement, 'replacement', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'pattern': [ pattern, 'pattern', [ basestring, 'None' ], False ],
        }, {
            'result': [ NameMappingInfo, False ],
        } )
    
    def name_mapping_unix_user_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of UNIX users.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                UNIX user information object.
                All UNIX user information objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "name-mapping-unix-user-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ UnixUserInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ UnixUserInfo, 'None' ], False ],
        }, {
            'attributes-list': [ UnixUserInfo, True ],
        } )
    
    def name_mapping_swap(self, position, direction, with_position):
        """
        Swap the position of one name mapping with another. The position
        is the place in the sequence of name mappings in which the
        mappings are applied.
        
        :param position: Position of an existing name mapping in the list of name mappings
                for this Vserver.
        
        :param direction: Direction in which the name mapping is applied.
        
        :param with_position: Position of an existing name mapping entry in the list of name
                mappings for this Vserver. This entry will be swapped with the
                entry at 'position'.
        """
        return self.request( "name-mapping-swap", {
            'position': [ position, 'position', [ int, 'None' ], False ],
            'direction': [ direction, 'direction', [ basestring, 'None' ], False ],
            'with_position': [ with_position, 'with-position', [ int, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_unix_group_destroy(self, group_name):
        """
        Destroy an existing UNIX group.
        
        :param group_name: Specifies UNIX group name.
        """
        return self.request( "name-mapping-unix-group-destroy", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_unix_group_add_user(self, group_name, user_name):
        """
        Add a user to a UNIX group
        
        :param group_name: Specifies UNIX group name.
        
        :param user_name: Specifies user's UNIX account name.
        """
        return self.request( "name-mapping-unix-group-add-user", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def name_mapping_unix_user_create(self, user_name, user_id, group_id, full_name=None, return_record=None):
        """
        Create a new UNIX user.
        
        :param user_name: Specifies user's UNIX account name.
        
        :param user_id: Specifies an identification number for the UNIX user.
        
        :param group_id: Specifies the primary group identification number for the UNIX
                user.
        
        :param full_name: Specifies the full name of the UNIX user.
        
        :param return_record: If set to true, returns the UNIX user information on successful
                creation.
                Default: false
        """
        return self.request( "name-mapping-unix-user-create", {
            'full_name': [ full_name, 'full-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'user_id': [ user_id, 'user-id', [ int, 'None' ], False ],
            'group_id': [ group_id, 'group-id', [ int, 'None' ], False ],
        }, {
            'result': [ UnixUserInfo, False ],
        } )
