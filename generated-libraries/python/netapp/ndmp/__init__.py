from netapp.connection import NaConnection
from ndmp_password_info import NdmpPasswordInfo # 3 properties

class NdmpConnection(NaConnection):
    
    def ndmp_password_generate(self, user_name, desired_attributes=None):
        """
        Generate NDMP password for the given user in a specific Vserver
        context. The generated NDMP password is based on the actual
        login password for the user; hence it should be regenerated
        whenever the actual user password is changed.
        
        :param user_name: The user for which the password is to be generated.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ndmp-password-generate", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NdmpPasswordInfo, 'None' ], False ],
        }, {
            'attributes': [ NdmpPasswordInfo, False ],
        } )
