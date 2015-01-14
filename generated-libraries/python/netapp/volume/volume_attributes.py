from netapp.volume.volume_hybrid_cache_attributes import VolumeHybridCacheAttributes
from netapp.volume.volume_mirror_attributes import VolumeMirrorAttributes
from netapp.volume.volume_space_attributes import VolumeSpaceAttributes
from netapp.volume.volume_directory_attributes import VolumeDirectoryAttributes
from netapp.volume.volume_state_attributes import VolumeStateAttributes
from netapp.volume.volume_autosize_attributes import VolumeAutosizeAttributes
from netapp.volume.volume_flexcache_attributes import VolumeFlexcacheAttributes
from netapp.volume.volume_id_attributes import VolumeIdAttributes
from netapp.volume.volume_antivirus_attributes import VolumeAntivirusAttributes
from netapp.volume.volume_qos_attributes import VolumeQosAttributes
from netapp.volume.volume_transition_attributes import VolumeTransitionAttributes
from netapp.volume.volume_snapshot_attributes import VolumeSnapshotAttributes
from netapp.volume.volume_language_attributes import VolumeLanguageAttributes
from netapp.volume.volume_security_attributes import VolumeSecurityAttributes
from netapp.volume.volume_sis_attributes import VolumeSisAttributes
from netapp.volume.volume_performance_attributes import VolumePerformanceAttributes
from netapp.volume.volume_inode_attributes import VolumeInodeAttributes
from netapp.volume.volume_snapshot_autodelete_attributes import VolumeSnapshotAutodeleteAttributes
from netapp.volume.volume_vm_align_attributes import VolumeVmAlignAttributes
from netapp.volume.volume_64bit_upgrade_attributes import Volume64BitUpgradeAttributes
from netapp.volume.volume_clone_attributes import VolumeCloneAttributes
from netapp.volume.volume_infinitevol_attributes import VolumeInfinitevolAttributes
from netapp.volume.volume_export_attributes import VolumeExportAttributes
from netapp.netapp_object import NetAppObject

class VolumeAttributes(NetAppObject):
    """
    Attributes of a volume.
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
    
    _volume_hybrid_cache_attributes = None
    @property
    def volume_hybrid_cache_attributes(self):
        """
        This field contains information on Flash Pool caching
        attributes on a volume
        """
        return self._volume_hybrid_cache_attributes
    @volume_hybrid_cache_attributes.setter
    def volume_hybrid_cache_attributes(self, val):
        if val != None:
            self.validate('volume_hybrid_cache_attributes', val)
        self._volume_hybrid_cache_attributes = val
    
    _volume_mirror_attributes = None
    @property
    def volume_mirror_attributes(self):
        """
        This field contains information applying exclusive to
        volume mirror.
        """
        return self._volume_mirror_attributes
    @volume_mirror_attributes.setter
    def volume_mirror_attributes(self, val):
        if val != None:
            self.validate('volume_mirror_attributes', val)
        self._volume_mirror_attributes = val
    
    _volume_space_attributes = None
    @property
    def volume_space_attributes(self):
        """
        This field contains information related to volume disk
        space management including on-disk layout.
        """
        return self._volume_space_attributes
    @volume_space_attributes.setter
    def volume_space_attributes(self, val):
        if val != None:
            self.validate('volume_space_attributes', val)
        self._volume_space_attributes = val
    
    _volume_directory_attributes = None
    @property
    def volume_directory_attributes(self):
        """
        This field contains information related to directories in
        a volume.
        """
        return self._volume_directory_attributes
    @volume_directory_attributes.setter
    def volume_directory_attributes(self, val):
        if val != None:
            self.validate('volume_directory_attributes', val)
        self._volume_directory_attributes = val
    
    _volume_state_attributes = None
    @property
    def volume_state_attributes(self):
        """
        This field contains information about the state or status
        of a volume or its features.
        """
        return self._volume_state_attributes
    @volume_state_attributes.setter
    def volume_state_attributes(self, val):
        if val != None:
            self.validate('volume_state_attributes', val)
        self._volume_state_attributes = val
    
    _volume_autosize_attributes = None
    @property
    def volume_autosize_attributes(self):
        """
        This field contains information about the autosize
        settings of the volume.
        """
        return self._volume_autosize_attributes
    @volume_autosize_attributes.setter
    def volume_autosize_attributes(self, val):
        if val != None:
            self.validate('volume_autosize_attributes', val)
        self._volume_autosize_attributes = val
    
    _volume_flexcache_attributes = None
    @property
    def volume_flexcache_attributes(self):
        """
        This field contains information applying exclusively to
        flexcache volumes.
        """
        return self._volume_flexcache_attributes
    @volume_flexcache_attributes.setter
    def volume_flexcache_attributes(self, val):
        if val != None:
            self.validate('volume_flexcache_attributes', val)
        self._volume_flexcache_attributes = val
    
    _volume_id_attributes = None
    @property
    def volume_id_attributes(self):
        """
        This field contains identification information about the
        volume.
        """
        return self._volume_id_attributes
    @volume_id_attributes.setter
    def volume_id_attributes(self, val):
        if val != None:
            self.validate('volume_id_attributes', val)
        self._volume_id_attributes = val
    
    _volume_antivirus_attributes = None
    @property
    def volume_antivirus_attributes(self):
        """
        This field contains information about Antivirus On-Access
        settings for the volume.
        """
        return self._volume_antivirus_attributes
    @volume_antivirus_attributes.setter
    def volume_antivirus_attributes(self, val):
        if val != None:
            self.validate('volume_antivirus_attributes', val)
        self._volume_antivirus_attributes = val
    
    _volume_qos_attributes = None
    @property
    def volume_qos_attributes(self):
        """
        This field contains the information that relates to QoS.
        """
        return self._volume_qos_attributes
    @volume_qos_attributes.setter
    def volume_qos_attributes(self, val):
        if val != None:
            self.validate('volume_qos_attributes', val)
        self._volume_qos_attributes = val
    
    _volume_transition_attributes = None
    @property
    def volume_transition_attributes(self):
        """
        This field contains information applying exclusively to
        transitioned or transitioning volumes.
        """
        return self._volume_transition_attributes
    @volume_transition_attributes.setter
    def volume_transition_attributes(self, val):
        if val != None:
            self.validate('volume_transition_attributes', val)
        self._volume_transition_attributes = val
    
    _volume_snapshot_attributes = None
    @property
    def volume_snapshot_attributes(self):
        """
        This field contains information applying exclusively to
        all the snapshots in the volume. Volume disk
        space-related settings are excluded.
        """
        return self._volume_snapshot_attributes
    @volume_snapshot_attributes.setter
    def volume_snapshot_attributes(self, val):
        if val != None:
            self.validate('volume_snapshot_attributes', val)
        self._volume_snapshot_attributes = val
    
    _volume_language_attributes = None
    @property
    def volume_language_attributes(self):
        """
        This field contains information about volume
        language-related settings.
        """
        return self._volume_language_attributes
    @volume_language_attributes.setter
    def volume_language_attributes(self, val):
        if val != None:
            self.validate('volume_language_attributes', val)
        self._volume_language_attributes = val
    
    _volume_security_attributes = None
    @property
    def volume_security_attributes(self):
        """
        This field contains information about volume security
        settings.
        """
        return self._volume_security_attributes
    @volume_security_attributes.setter
    def volume_security_attributes(self, val):
        if val != None:
            self.validate('volume_security_attributes', val)
        self._volume_security_attributes = val
    
    _volume_sis_attributes = None
    @property
    def volume_sis_attributes(self):
        """
        This field contains information about Deduplication, file
        clone, compression, etc.
        """
        return self._volume_sis_attributes
    @volume_sis_attributes.setter
    def volume_sis_attributes(self, val):
        if val != None:
            self.validate('volume_sis_attributes', val)
        self._volume_sis_attributes = val
    
    _volume_performance_attributes = None
    @property
    def volume_performance_attributes(self):
        """
        This field contains information that relates to the
        performance of the volume.
        """
        return self._volume_performance_attributes
    @volume_performance_attributes.setter
    def volume_performance_attributes(self, val):
        if val != None:
            self.validate('volume_performance_attributes', val)
        self._volume_performance_attributes = val
    
    _volume_inode_attributes = None
    @property
    def volume_inode_attributes(self):
        """
        This field contains information about inodes in a
        volume.
        """
        return self._volume_inode_attributes
    @volume_inode_attributes.setter
    def volume_inode_attributes(self, val):
        if val != None:
            self.validate('volume_inode_attributes', val)
        self._volume_inode_attributes = val
    
    _volume_snapshot_autodelete_attributes = None
    @property
    def volume_snapshot_autodelete_attributes(self):
        """
        This field contains information about snapshot autodelete
        policy settings.
        """
        return self._volume_snapshot_autodelete_attributes
    @volume_snapshot_autodelete_attributes.setter
    def volume_snapshot_autodelete_attributes(self, val):
        if val != None:
            self.validate('volume_snapshot_autodelete_attributes', val)
        self._volume_snapshot_autodelete_attributes = val
    
    _volume_vm_align_attributes = None
    @property
    def volume_vm_align_attributes(self):
        """
        This field contains information related to the Virtual
        Machine alignment settings on a volume
        """
        return self._volume_vm_align_attributes
    @volume_vm_align_attributes.setter
    def volume_vm_align_attributes(self, val):
        if val != None:
            self.validate('volume_vm_align_attributes', val)
        self._volume_vm_align_attributes = val
    
    _volume_64bit_upgrade_attributes = None
    @property
    def volume_64bit_upgrade_attributes(self):
        """
        Information related to 64-bit upgrade. After 64-bit
        upgrade completes, this information is no longer
        available.
        """
        return self._volume_64bit_upgrade_attributes
    @volume_64bit_upgrade_attributes.setter
    def volume_64bit_upgrade_attributes(self, val):
        if val != None:
            self.validate('volume_64bit_upgrade_attributes', val)
        self._volume_64bit_upgrade_attributes = val
    
    _volume_clone_attributes = None
    @property
    def volume_clone_attributes(self):
        """
        This field contains information applying exclusively to
        clone volumes.
        """
        return self._volume_clone_attributes
    @volume_clone_attributes.setter
    def volume_clone_attributes(self, val):
        if val != None:
            self.validate('volume_clone_attributes', val)
        self._volume_clone_attributes = val
    
    _volume_infinitevol_attributes = None
    @property
    def volume_infinitevol_attributes(self):
        """
        This field contains information about the state of an
        Infinite Volume.
        """
        return self._volume_infinitevol_attributes
    @volume_infinitevol_attributes.setter
    def volume_infinitevol_attributes(self, val):
        if val != None:
            self.validate('volume_infinitevol_attributes', val)
        self._volume_infinitevol_attributes = val
    
    _volume_export_attributes = None
    @property
    def volume_export_attributes(self):
        """
        This field contains information about export settings of
        the volume.
        """
        return self._volume_export_attributes
    @volume_export_attributes.setter
    def volume_export_attributes(self, val):
        if val != None:
            self.validate('volume_export_attributes', val)
        self._volume_export_attributes = val
    
    @staticmethod
    def get_api_name():
          return "volume-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-hybrid-cache-attributes',
            'volume-mirror-attributes',
            'volume-space-attributes',
            'volume-directory-attributes',
            'volume-state-attributes',
            'volume-autosize-attributes',
            'volume-flexcache-attributes',
            'volume-id-attributes',
            'volume-antivirus-attributes',
            'volume-qos-attributes',
            'volume-transition-attributes',
            'volume-snapshot-attributes',
            'volume-language-attributes',
            'volume-security-attributes',
            'volume-sis-attributes',
            'volume-performance-attributes',
            'volume-inode-attributes',
            'volume-snapshot-autodelete-attributes',
            'volume-vm-align-attributes',
            'volume-64bit-upgrade-attributes',
            'volume-clone-attributes',
            'volume-infinitevol-attributes',
            'volume-export-attributes',
        ]
    
    def describe_properties(self):
        return {
            'volume_hybrid_cache_attributes': { 'class': VolumeHybridCacheAttributes, 'is_list': False, 'required': 'optional' },
            'volume_mirror_attributes': { 'class': VolumeMirrorAttributes, 'is_list': False, 'required': 'optional' },
            'volume_space_attributes': { 'class': VolumeSpaceAttributes, 'is_list': False, 'required': 'optional' },
            'volume_directory_attributes': { 'class': VolumeDirectoryAttributes, 'is_list': False, 'required': 'optional' },
            'volume_state_attributes': { 'class': VolumeStateAttributes, 'is_list': False, 'required': 'optional' },
            'volume_autosize_attributes': { 'class': VolumeAutosizeAttributes, 'is_list': False, 'required': 'optional' },
            'volume_flexcache_attributes': { 'class': VolumeFlexcacheAttributes, 'is_list': False, 'required': 'optional' },
            'volume_id_attributes': { 'class': VolumeIdAttributes, 'is_list': False, 'required': 'optional' },
            'volume_antivirus_attributes': { 'class': VolumeAntivirusAttributes, 'is_list': False, 'required': 'optional' },
            'volume_qos_attributes': { 'class': VolumeQosAttributes, 'is_list': False, 'required': 'optional' },
            'volume_transition_attributes': { 'class': VolumeTransitionAttributes, 'is_list': False, 'required': 'optional' },
            'volume_snapshot_attributes': { 'class': VolumeSnapshotAttributes, 'is_list': False, 'required': 'optional' },
            'volume_language_attributes': { 'class': VolumeLanguageAttributes, 'is_list': False, 'required': 'optional' },
            'volume_security_attributes': { 'class': VolumeSecurityAttributes, 'is_list': False, 'required': 'optional' },
            'volume_sis_attributes': { 'class': VolumeSisAttributes, 'is_list': False, 'required': 'optional' },
            'volume_performance_attributes': { 'class': VolumePerformanceAttributes, 'is_list': False, 'required': 'optional' },
            'volume_inode_attributes': { 'class': VolumeInodeAttributes, 'is_list': False, 'required': 'optional' },
            'volume_snapshot_autodelete_attributes': { 'class': VolumeSnapshotAutodeleteAttributes, 'is_list': False, 'required': 'optional' },
            'volume_vm_align_attributes': { 'class': VolumeVmAlignAttributes, 'is_list': False, 'required': 'optional' },
            'volume_64bit_upgrade_attributes': { 'class': Volume64BitUpgradeAttributes, 'is_list': False, 'required': 'optional' },
            'volume_clone_attributes': { 'class': VolumeCloneAttributes, 'is_list': False, 'required': 'optional' },
            'volume_infinitevol_attributes': { 'class': VolumeInfinitevolAttributes, 'is_list': False, 'required': 'optional' },
            'volume_export_attributes': { 'class': VolumeExportAttributes, 'is_list': False, 'required': 'optional' },
        }
