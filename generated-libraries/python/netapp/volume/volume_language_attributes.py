from netapp.netapp_object import NetAppObject

class VolumeLanguageAttributes(NetAppObject):
    """
    Information about the volume language settings.
    """
    
    _language_code = None
    @property
    def language_code(self):
        """
        The volume's language code (e.g. 'en_US').
        <p>
        Volume language can be specified using 'language-code'
        parameter.
        <p>
        Attributes: optional-for-create, non-modifiable
        """
        return self._language_code
    @language_code.setter
    def language_code(self, val):
        if val != None:
            self.validate('language_code', val)
        self._language_code = val
    
    _nfs_character_set = None
    @property
    def nfs_character_set(self):
        """
        The NFS language mapping character set that is currently
        in effect for the volume.
        <p>
        This field is of the following format:
        <ul>
        <li>
        '&lt;nfs-character-set&gt;|&lt;display-name&gt;|&lt;asctime&gt;'
        </ul>
        Note that '|' is not an OR syntax.
        <p>
        &lt;asctime&gt; is the timestamp in the language
        configuration file header and its format is based on the
        standard: 'A la ISO/IEC 9945-1, ANSI/IEEE Std 1003.1,
        Second Edition, 1996-07-12.'
        <p>
        It uses the C Programming Language Printf format:
        <p>
        <ul>
        <li> '%.3s %.3s%3d %02d:%02d:%02d %s %d'
        </ul>
        <p>
        This format takes the following parameters in order:
        <ul>
        <li> &lt;weekday name&gt;,
        <li> &lt;month name&gt;,
        <li> &lt;month day&gt;,
        <li> &lt;hour&gt;,
        <li> &lt;minute&gt;,
        <li> &lt;second&gt;
        <li> &lt;timezone&gt; OR &lt;''&gt;,
        <li> &lt;year&gt;
        </ul>
        <p>
        E.g., If the volume language code is set to 'en_US,' the
        default NFS character set is as follows:
        <ul>
        <li> 'iso-8859-1|iso-8859-1|Thu Oct  1 15:00:53 PDT
        1998'
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._nfs_character_set
    @nfs_character_set.setter
    def nfs_character_set(self, val):
        if val != None:
            self.validate('nfs_character_set', val)
        self._nfs_character_set = val
    
    _language = None
    @property
    def language(self):
        """
        The volume's fully-qualified language mapping, in the
        form: 'LanguageCode (Full Name).'
        <p>
        Example: 'en_US (English (US)).'
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._language
    @language.setter
    def language(self, val):
        if val != None:
            self.validate('language', val)
        self._language = val
    
    _is_convert_ucode_enabled = None
    @property
    def is_convert_ucode_enabled(self):
        """
        This field controls whether all directories in this
        volume are forcibly converted to UNICODE format when
        accessed from both NFS and CIFS.  The default value for
        7-Mode volumes is false, in which case access from CIFS
        causes conversion of pre-4.0 and 4.0-format directories,
        and access from NFS causes conversion to 4.0-format
        directories.  The default value for Cluster-Mode volumes
        is true.
        <p>
        Note that this field can be set to false if and only if
        the volume is a 7-Mode volume, or a Cluster-Mode volume
        that was transitioned from 7-Mode.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._is_convert_ucode_enabled
    @is_convert_ucode_enabled.setter
    def is_convert_ucode_enabled(self, val):
        if val != None:
            self.validate('is_convert_ucode_enabled', val)
        self._is_convert_ucode_enabled = val
    
    _oem_character_set = None
    @property
    def oem_character_set(self):
        """
        The OEM language mapping character set that is currently
        in effect for the volume.
        <p>
        This field is of the following format:
        <ul>
        <li>
        '&lt;oem-code-page&gt;|&lt;display-name&gt;|&lt;asctime&gt;'
        </ul>
        Note that '|' is not an OR syntax.
        <p>
        &lt;asctime&gt; is the timestamp in the language
        configuration file header and its format is based on the
        standard: 'A la ISO/IEC 9945-1, ANSI/IEEE Std 1003.1,
        Second Edition, 1996-07-12.'
        <p>
        It uses the C Programming Language Printf format:
        <ul>
        <li> '%.3s %.3s%3d %02d:%02d:%02d %s %d'
        </ul>
        <p>
        This format takes the following parameters in order:
        <ul>
        <li> &lt;weekday name&gt;,
        <li> &lt;month name&gt;,
        <li> &lt;month day&gt;,
        <li> &lt;hour&gt;,
        <li> &lt;minute&gt;,
        <li> &lt;second&gt;,
        <li> &lt;timezone&gt; OR &lt;''&gt;,
        <li> &lt;year&gt;
        </ul>
        <p>
        E.g., If the volume language code is set to 'en_US,' the
        default OEM character set is as follows:
        <ul>
        <li> 'cp437|cp437|Thu Oct  1 15:00:53 PDT 1998'
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._oem_character_set
    @oem_character_set.setter
    def oem_character_set(self, val):
        if val != None:
            self.validate('oem_character_set', val)
        self._oem_character_set = val
    
    _is_create_ucode_enabled = None
    @property
    def is_create_ucode_enabled(self):
        """
        This field controls whether all directories in this
        volume are forced to use the UNICODE format when they are
        created, both from NFS and CIFS.  The default value is
        false for 7-Mode volumes, in which case all directories
        are created in pre-4.0 format and only converted to
        UNICODE format upon the first CIFS access.  The default
        value is true for Cluster-Mode volumes.
        <p>
        Note that this field can be set to false if and only if
        the volume is a 7-Mode volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._is_create_ucode_enabled
    @is_create_ucode_enabled.setter
    def is_create_ucode_enabled(self, val):
        if val != None:
            self.validate('is_create_ucode_enabled', val)
        self._is_create_ucode_enabled = val
    
    @staticmethod
    def get_api_name():
          return "volume-language-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'language-code',
            'nfs-character-set',
            'language',
            'is-convert-ucode-enabled',
            'oem-character-set',
            'is-create-ucode-enabled',
        ]
    
    def describe_properties(self):
        return {
            'language_code': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nfs_character_set': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'language': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_convert_ucode_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'oem_character_set': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_create_ucode_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
