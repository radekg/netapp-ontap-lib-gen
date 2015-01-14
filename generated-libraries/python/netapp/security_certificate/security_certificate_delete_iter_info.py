from netapp.security_certificate.certificate_info import CertificateInfo
from netapp.netapp_object import NetAppObject

class SecurityCertificateDeleteIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against security-certificate object.
    but were not deleted due to some error.
    deleted due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the deletion operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    _security_certificate_key = None
    @property
    def security_certificate_key(self):
        """
        The keys for the security-certificate object to which the
        deletion applies.
        """
        return self._security_certificate_key
    @security_certificate_key.setter
    def security_certificate_key(self, val):
        if val != None:
            self.validate('security_certificate_key', val)
        self._security_certificate_key = val
    
    @staticmethod
    def get_api_name():
          return "security-certificate-delete-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'security-certificate-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_certificate_key': { 'class': CertificateInfo, 'is_list': False, 'required': 'required' },
        }
