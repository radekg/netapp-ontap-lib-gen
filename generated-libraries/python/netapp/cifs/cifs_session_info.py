from netapp.cifs.volumes_list_info import VolumesListInfo
from netapp.netapp_object import NetAppObject

class CifsSessionInfo(NetAppObject):
    """
    Information about a single cifs session.
    """
    
    _files = None
    @property
    def files(self):
        """
        Number of open files.
        """
        return self._files
    @files.setter
    def files(self, val):
        if val != None:
            self.validate('files', val)
        self._files = val
    
    _dirs = None
    @property
    def dirs(self):
        """
        Number of open directories.
        """
        return self._dirs
    @dirs.setter
    def dirs(self, val):
        if val != None:
            self.validate('dirs', val)
        self._dirs = val
    
    _volumes_list = None
    @property
    def volumes_list(self):
        """
        List of volumes being accessed during the session.
        """
        return self._volumes_list
    @volumes_list.setter
    def volumes_list(self, val):
        if val != None:
            self.validate('volumes_list', val)
        self._volumes_list = val
    
    _shares = None
    @property
    def shares(self):
        """
        Number of open shares.
        """
        return self._shares
    @shares.setter
    def shares(self, val):
        if val != None:
            self.validate('shares', val)
        self._shares = val
    
    _change_notifies = None
    @property
    def change_notifies(self):
        """
        Number of active ChangeNotify requests.
        """
        return self._change_notifies
    @change_notifies.setter
    def change_notifies(self, val):
        if val != None:
            self.validate('change_notifies', val)
        self._change_notifies = val
    
    _host_name = None
    @property
    def host_name(self):
        """
        NetBios name of the CIFS client. This may be unavailable
        in certain situations. In such cases, the ONTAPI element
        'host-ip' alone provides identity of the host.
        """
        return self._host_name
    @host_name.setter
    def host_name(self, val):
        if val != None:
            self.validate('host_name', val)
        self._host_name = val
    
    _user = None
    @property
    def user(self):
        """
        Name of the user.
        """
        return self._user
    @user.setter
    def user(self, val):
        if val != None:
            self.validate('user', val)
        self._user = val
    
    _host_ip = None
    @property
    def host_ip(self):
        """
        IP address, in dotted-decimal format, of the CIFS client.
        """
        return self._host_ip
    @host_ip.setter
    def host_ip(self, val):
        if val != None:
            self.validate('host_ip', val)
        self._host_ip = val
    
    @staticmethod
    def get_api_name():
          return "cifs-session-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'files',
            'dirs',
            'volumes-list',
            'shares',
            'change-notifies',
            'host-name',
            'user',
            'host-ip',
        ]
    
    def describe_properties(self):
        return {
            'files': { 'class': int, 'is_list': False, 'required': 'required' },
            'dirs': { 'class': int, 'is_list': False, 'required': 'required' },
            'volumes_list': { 'class': VolumesListInfo, 'is_list': True, 'required': 'required' },
            'shares': { 'class': int, 'is_list': False, 'required': 'required' },
            'change_notifies': { 'class': int, 'is_list': False, 'required': 'required' },
            'host_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'host_ip': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
