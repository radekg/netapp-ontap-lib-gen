from netapp.connection import NaConnection
from useradmin_capability_info import UseradminCapabilityInfo # 1 properties
from useradmin_group_info import UseradminGroupInfo # 5 properties
from useradmin_role_info import UseradminRoleInfo # 3 properties
from sid import Sid # 0 properties
from useradmin_user_info import UseradminUserInfo # 9 properties

class UseradminConnection(NaConnection):
    
    def useradmin_user_has_capability(self, capability, user_name):
        """
        Returns true if the user has the associated capability.
        This API can only return true if the user recently
        logged in and the user information is in the cache.
        
        :param capability: Check if the user has this capability. Only a single
                capability is accepted.
                Possible values include: "*", "login-*", "cli-*",
                "api-*", "security-*"...
        
        :param user_name: Find out if this user has the associated capability.
                The username can reference a local or non-local
                user. A domain user will have the format <domain>\<user>.
        """
        return self.request( "useradmin-user-has-capability", {
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
            'is-user-capable': [ bool, False ],
        } )
    
    def useradmin_user_list(self, group_name=None, user_name=None, verbose=None):
        """
        Lists information for all administrative users on the system
        with the exception of root and snmp.
        
        :param group_name: List only the users which are a part of this group.
                This option must be left empty if the option "user-name"
                contains a value.
        
        :param user_name: List only the information associated with this user.
                This option must be left empty if the option "group-name"
                contains a value.
        
        :param verbose: Default is false. If set to true, then the allowed
                capabilities are placed into the user-info structure.
                Depending on number of users, groups, and roles; this operation
                may take a long time.
        """
        return self.request( "useradmin-user-list", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'useradmin-users': [ UseradminUserInfo, True ],
        } )
    
    def useradmin_domainuser_list(self, group_name):
        """
        List all of the SIDs in a given group. This API is only
        used in a windows environment.
        @test
        
        :param group_name: List only the SIDs in this group.
        """
        return self.request( "useradmin-domainuser-list", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
        }, {
            'user-identifiers': [ basestring, True ],
        } )
    
    def useradmin_group_modify(self, useradmin_group, new_group_name=None):
        """
        Modifies a group given the information provided.
        
        :param useradmin_group: A group must have a name. If one or more roless and/or a
                comment is provided, the group is modified
                accordingly. All other fields are ignored.
        
        :param new_group_name: New group name for this group. This is used to rename the
                group specified in useradmin-group. If this value is invalid,
                useradmin-group-modify fails without changing anything.
                The value is optional, and if not provided, the group name
                will be unchanged.
        """
        return self.request( "useradmin-group-modify", {
            'new_group_name': [ new_group_name, 'new-group-name', [ basestring, 'None' ], False ],
            'useradmin_group': [ useradmin_group, 'useradmin-group', [ UseradminGroupInfo, 'None' ], False ],
        }, {
        } )
    
    def useradmin_role_list(self, role_name=None):
        """
        Lists full information for all roles on the system.
        
        :param role_name: List only the information associated with this role.
        """
        return self.request( "useradmin-role-list", {
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
        }, {
            'useradmin-roles': [ UseradminRoleInfo, True ],
        } )
    
    def useradmin_role_add(self, useradmin_role):
        """
        Adds a role given the information provided.
        
        :param useradmin_role: New role information. A role must have a name and at least
                one allowed capability. A role-info comment is also
                allowed. All other fields are ignored.
        """
        return self.request( "useradmin-role-add", {
            'useradmin_role': [ useradmin_role, 'useradmin-role', [ UseradminRoleInfo, 'None' ], False ],
        }, {
        } )
    
    def useradmin_user_modify(self, useradmin_user):
        """
        Modifies a user given the information provided.
        
        :param useradmin_user: A user must have a name. If one or more groups a comment
                and/or a full-name is provided, the user is modified
                accordingly. All other fields are ignored.
        """
        return self.request( "useradmin-user-modify", {
            'useradmin_user': [ useradmin_user, 'useradmin-user', [ UseradminUserInfo, 'None' ], False ],
        }, {
        } )
    
    def useradmin_group_list(self, group_name=None, verbose=None):
        """
        Lists full information for all groups on the system.
        
        :param group_name: List only the information associated with this group.
        
        :param verbose: Default is false. If set to true, then the allowed
                capabilities are placed into the group-info structure.
                Depending on number of groups and roles, this operation
                may take a long time.
        """
        return self.request( "useradmin-group-list", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
            'verbose': [ verbose, 'verbose', [ bool, 'None' ], False ],
        }, {
            'useradmin-groups': [ UseradminGroupInfo, True ],
        } )
    
    def useradmin_user_modify_password(self, new_password, user_name, old_password=None):
        """
        Changes the password of a specified user.
        @test
        
        :param new_password: New password for the user. Please see documentation for
                constraints on the password.
        
        :param user_name: The user who's password should be changed.
        
        :param old_password: Current password for the user. A user with the
                capability 'security-passwd-change-others' and at least the
                same capabilities as the user being changed, does not
                need to enter the current password in order to change it to
                a new one.
        """
        return self.request( "useradmin-user-modify-password", {
            'new_password': [ new_password, 'new-password', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'old_password': [ old_password, 'old-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def useradmin_domainuser_add(self, user_identifier, useradmin_groups):
        """
        Adds a nonlocal user into a group or groups. The user can
        be added as a SID or as domain\username. This API is only
        used in a windows environment.
        @test
        
        :param user_identifier: Name of the user in domain\username format. This can
                also be a SID (Windows security identifier) describing
                a user. A SID has the format S-1-5-21-int-int-int-rid.
        
        :param useradmin_groups: List of local groups to contain the domain user.
        """
        return self.request( "useradmin-domainuser-add", {
            'user_identifier': [ user_identifier, 'user-identifier', [ basestring, 'None' ], False ],
            'useradmin_groups': [ useradmin_groups, 'useradmin-groups', [ UseradminGroupInfo, 'None' ], True ],
        }, {
        } )
    
    def useradmin_group_delete(self, group_name):
        """
        Deletes a group.
        
        :param group_name: The name of the group to be deleted.
        """
        return self.request( "useradmin-group-delete", {
            'group_name': [ group_name, 'group-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def useradmin_user_add(self, useradmin_user, password):
        """
        Adds a user given the information provided.
        
        :param useradmin_user: New user information. A user must have a name and at least
                one group. A comment and full-name are also allowed. All
                other fields are ignored.
        
        :param password: Password for the user. Please see documentation for
                constraints on the password.
        """
        return self.request( "useradmin-user-add", {
            'useradmin_user': [ useradmin_user, 'useradmin-user', [ UseradminUserInfo, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def useradmin_role_modify(self, useradmin_role):
        """
        Modifies a role given the information provided.
        
        :param useradmin_role: A role must have a name. If one or more capabilities and/or
                a comment is provided, the role is modified
                accordingly.
        """
        return self.request( "useradmin-role-modify", {
            'useradmin_role': [ useradmin_role, 'useradmin-role', [ UseradminRoleInfo, 'None' ], False ],
        }, {
        } )
    
    def useradmin_user_delete(self, user_name):
        """
        Deletes a user.
        
        :param user_name: The name of the user to be deleted.
        """
        return self.request( "useradmin-user-delete", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def useradmin_domainuser_delete(self, user_identifier, useradmin_groups):
        """
        Removes a nonlocal user from a group or groups. The user can
        be removed as a SID or as domain\username. This API is only
        used in a windows environment.
        @test
        
        :param user_identifier: Name of the user in domain\username format. This can
                also be a SID (Windows security identifier) describing
                a user. A SID has the format S-1-5-21-int-int-int-rid.
        
        :param useradmin_groups: Remove the SID from this list of local groups.
        """
        return self.request( "useradmin-domainuser-delete", {
            'user_identifier': [ user_identifier, 'user-identifier', [ basestring, 'None' ], False ],
            'useradmin_groups': [ useradmin_groups, 'useradmin-groups', [ UseradminGroupInfo, 'None' ], True ],
        }, {
        } )
    
    def useradmin_role_delete(self, role_name):
        """
        Deletes a role.
        
        :param role_name: The name of the role to be deleted.
        """
        return self.request( "useradmin-role-delete", {
            'role_name': [ role_name, 'role-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def useradmin_group_add(self, useradmin_group):
        """
        Adds a group given the information provided.
        
        :param useradmin_group: New group information. A group must have a name and at least
                one role. A comment is also allowed. All other
                fields are ignored.
        """
        return self.request( "useradmin-group-add", {
            'useradmin_group': [ useradmin_group, 'useradmin-group', [ UseradminGroupInfo, 'None' ], False ],
        }, {
        } )
