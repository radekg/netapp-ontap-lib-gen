from netapp.netapp_object import NetAppObject

class AvEngineOption(NetAppObject):
    """
    Antivirus engine options
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
    
    _max_recursion_depth = None
    @property
    def max_recursion_depth(self):
        """
        Max recursion depth into archives
        Attributes: non-creatable, modifiable
        """
        return self._max_recursion_depth
    @max_recursion_depth.setter
    def max_recursion_depth(self, val):
        if val != None:
            self.validate('max_recursion_depth', val)
        self._max_recursion_depth = val
    
    _decompressed_file_size_limit = None
    @property
    def decompressed_file_size_limit(self):
        """
        Max size of files in archive
        Attributes: non-creatable, modifiable
        """
        return self._decompressed_file_size_limit
    @decompressed_file_size_limit.setter
    def decompressed_file_size_limit(self, val):
        if val != None:
            self.validate('decompressed_file_size_limit', val)
        self._decompressed_file_size_limit = val
    
    _decompressed_file_count_limit = None
    @property
    def decompressed_file_count_limit(self):
        """
        File count to decompress in archive
        Attributes: non-creatable, modifiable
        """
        return self._decompressed_file_count_limit
    @decompressed_file_count_limit.setter
    def decompressed_file_count_limit(self, val):
        if val != None:
            self.validate('decompressed_file_count_limit', val)
        self._decompressed_file_count_limit = val
    
    _proxy_password = None
    @property
    def proxy_password(self):
        """
        proxy server password
        Attributes: non-creatable, modifiable
        """
        return self._proxy_password
    @proxy_password.setter
    def proxy_password(self, val):
        if val != None:
            self.validate('proxy_password', val)
        self._proxy_password = val
    
    _mark_files_greater_than_2gb_clean = None
    @property
    def mark_files_greater_than_2gb_clean(self):
        """
        Mark the State of Files Greater Than 2GB Clean
        Attributes: non-creatable, modifiable
        """
        return self._mark_files_greater_than_2gb_clean
    @mark_files_greater_than_2gb_clean.setter
    def mark_files_greater_than_2gb_clean(self, val):
        if val != None:
            self.validate('mark_files_greater_than_2gb_clean', val)
        self._mark_files_greater_than_2gb_clean = val
    
    _decompression_layers_limit = None
    @property
    def decompression_layers_limit(self):
        """
        Max layers to traverse in archive
        Attributes: non-creatable, modifiable
        """
        return self._decompression_layers_limit
    @decompression_layers_limit.setter
    def decompression_layers_limit(self, val):
        if val != None:
            self.validate('decompression_layers_limit', val)
        self._decompression_layers_limit = val
    
    _proxy_port = None
    @property
    def proxy_port(self):
        """
        proxy server port number
        Attributes: non-creatable, modifiable
        """
        return self._proxy_port
    @proxy_port.setter
    def proxy_port(self, val):
        if val != None:
            self.validate('proxy_port', val)
        self._proxy_port = val
    
    _group_archive_unpack = None
    @property
    def group_archive_unpack(self):
        """
        Scan archive file formats
        Attributes: non-creatable, modifiable
        """
        return self._group_archive_unpack
    @group_archive_unpack.setter
    def group_archive_unpack(self, val):
        if val != None:
            self.validate('group_archive_unpack', val)
        self._group_archive_unpack = val
    
    _cache_size = None
    @property
    def cache_size(self):
        """
        Max Cache Size for Scanning Files (MB)
        Attributes: non-creatable, modifiable
        """
        return self._cache_size
    @cache_size.setter
    def cache_size(self, val):
        if val != None:
            self.validate('cache_size', val)
        self._cache_size = val
    
    _is_spyware_enabled = None
    @property
    def is_spyware_enabled(self):
        """
        Spyware enable/disable
        Attributes: non-creatable, modifiable
        """
        return self._is_spyware_enabled
    @is_spyware_enabled.setter
    def is_spyware_enabled(self, val):
        if val != None:
            self.validate('is_spyware_enabled', val)
        self._is_spyware_enabled = val
    
    _proxy_host = None
    @property
    def proxy_host(self):
        """
        proxy server name e.g. http://proxy_server_name
        Attributes: non-creatable, modifiable
        """
        return self._proxy_host
    @proxy_host.setter
    def proxy_host(self, val):
        if val != None:
            self.validate('proxy_host', val)
        self._proxy_host = val
    
    _mime_lines_to_scan = None
    @property
    def mime_lines_to_scan(self):
        """
        Max Lines to Scan to Identify MIME file
        Attributes: non-creatable, modifiable
        """
        return self._mime_lines_to_scan
    @mime_lines_to_scan.setter
    def mime_lines_to_scan(self, val):
        if val != None:
            self.validate('mime_lines_to_scan', val)
        self._mime_lines_to_scan = val
    
    _scan_mime = None
    @property
    def scan_mime(self):
        """
        Scan MIME-Encoded Files
        Attributes: non-creatable, modifiable
        """
        return self._scan_mime
    @scan_mime.setter
    def scan_mime(self, val):
        if val != None:
            self.validate('scan_mime', val)
        self._scan_mime = val
    
    _heuristic_analysis = None
    @property
    def heuristic_analysis(self):
        """
        Heuristic Virus Search Analysis
        Attributes: non-creatable, modifiable
        """
        return self._heuristic_analysis
    @heuristic_analysis.setter
    def heuristic_analysis(self, val):
        if val != None:
            self.validate('heuristic_analysis', val)
        self._heuristic_analysis = val
    
    _macro_analysis = None
    @property
    def macro_analysis(self):
        """
        Macro Virus Search Analysis
        Attributes: non-creatable, modifiable
        """
        return self._macro_analysis
    @macro_analysis.setter
    def macro_analysis(self, val):
        if val != None:
            self.validate('macro_analysis', val)
        self._macro_analysis = val
    
    _decompression_size_factor = None
    @property
    def decompression_size_factor(self):
        """
        Max decompression size factor of files in archive
        Attributes: non-creatable, modifiable
        """
        return self._decompression_size_factor
    @decompression_size_factor.setter
    def decompression_size_factor(self, val):
        if val != None:
            self.validate('decompression_size_factor', val)
        self._decompression_size_factor = val
    
    _proxy_login = None
    @property
    def proxy_login(self):
        """
        proxy server login
        Attributes: non-creatable, modifiable
        """
        return self._proxy_login
    @proxy_login.setter
    def proxy_login(self, val):
        if val != None:
            self.validate('proxy_login', val)
        self._proxy_login = val
    
    @staticmethod
    def get_api_name():
          return "av-engine-option"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'max-recursion-depth',
            'decompressed-file-size-limit',
            'decompressed-file-count-limit',
            'proxy-password',
            'mark-files-greater-than-2gb-clean',
            'decompression-layers-limit',
            'proxy-port',
            'group-archive-unpack',
            'cache-size',
            'is-spyware-enabled',
            'proxy-host',
            'mime-lines-to-scan',
            'scan-mime',
            'heuristic-analysis',
            'macro-analysis',
            'decompression-size-factor',
            'proxy-login',
        ]
    
    def describe_properties(self):
        return {
            'max_recursion_depth': { 'class': int, 'is_list': False, 'required': 'optional' },
            'decompressed_file_size_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'decompressed_file_count_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'proxy_password': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mark_files_greater_than_2gb_clean': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'decompression_layers_limit': { 'class': int, 'is_list': False, 'required': 'optional' },
            'proxy_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'group_archive_unpack': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'cache_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_spyware_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'proxy_host': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mime_lines_to_scan': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scan_mime': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'heuristic_analysis': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'macro_analysis': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'decompression_size_factor': { 'class': int, 'is_list': False, 'required': 'optional' },
            'proxy_login': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
