from netapp.volume.volume_security_unix_attributes import VolumeSecurityUnixAttributes
from netapp.netapp_object import NetAppObject

class VolumeSecurityAttributes(NetAppObject):
    """
    All security aspects of a volume.
    """
    
    _volume_security_unix_attributes = None
    @property
    def volume_security_unix_attributes(self):
        """
        The Unix-oriented security settings associated with this
        volume.
        """
        return self._volume_security_unix_attributes
    @volume_security_unix_attributes.setter
    def volume_security_unix_attributes(self, val):
        if val != None:
            self.validate('volume_security_unix_attributes', val)
        self._volume_security_unix_attributes = val
    
    _style = None
    @property
    def style(self):
        """
        The security style associated with this volume.
        <p>
        Possible values:
        <ul>
        <li> 'mixed' ... Mixed-style security,
        <li> 'ntfs'  ... NTFS/Windows-style security,
        <li> 'unified'  .Unified-style security, Unified
        UNIX, NFS and CIFS permissions (default for Infinite
        Volume)
        <li> 'unix'  ... Unix-style security (default for
        Flexible Volume)
        </ul>
        <p>
        This field is only returned if this volume is online. If
        this field is empty ('') or not present for an online
        volume, this attribute isn't applicable to the volume.
        Infinite Volumes can only use the 'unified' security
        style.
        All other volumes cannot use the 'unified' security
        style.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._style
    @style.setter
    def style(self, val):
        if val != None:
            self.validate('style', val)
        self._style = val
    
    @staticmethod
    def get_api_name():
          return "volume-security-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-security-unix-attributes',
            'style',
        ]
    
    def describe_properties(self):
        return {
            'volume_security_unix_attributes': { 'class': VolumeSecurityUnixAttributes, 'is_list': False, 'required': 'optional' },
            'style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
