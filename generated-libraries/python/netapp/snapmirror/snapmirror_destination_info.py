from netapp.netapp_object import NetAppObject

class SnapmirrorDestinationInfo(NetAppObject):
    """
    Information about a Destination of a SnapMirror Relationship
    Source
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
    
    _source_vserver = None
    @property
    def source_vserver(self):
        """
        Specifies the name of the source Vserver for the
        SnapMirror relationship. The name of the source volume
        must also be specified if using this parameter.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._source_vserver
    @source_vserver.setter
    def source_vserver(self, val):
        if val != None:
            self.validate('source_vserver', val)
        self._source_vserver = val
    
    _source_volume = None
    @property
    def source_volume(self):
        """
        Specifies the name of the source volume of the SnapMirror
        relationship. The name of the source Vserver must also be
        specified if using this parameter.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._source_volume
    @source_volume.setter
    def source_volume(self, val):
        if val != None:
            self.validate('source_volume', val)
        self._source_volume = val
    
    _transfer_progress = None
    @property
    def transfer_progress(self):
        """
        Specifies the number of bytes processed so far for the
        ongoing transfer.
        Attributes: non-creatable, non-modifiable
        """
        return self._transfer_progress
    @transfer_progress.setter
    def transfer_progress(self, val):
        if val != None:
            self.validate('transfer_progress', val)
        self._transfer_progress = val
    
    _relationship_type = None
    @property
    def relationship_type(self):
        """
        Specifies the SnapMirror relationship type.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "data_protection"               ,
        <li> "load_sharing"                  ,
        <li> "vault"                         ,
        <li> "restore"                       ,
        <li> "transition_data_protection"
        </ul>
        """
        return self._relationship_type
    @relationship_type.setter
    def relationship_type(self, val):
        if val != None:
            self.validate('relationship_type', val)
        self._relationship_type = val
    
    _source_volume_node = None
    @property
    def source_volume_node(self):
        """
        Node which owns the source volume of the relationship.
        Attributes: non-creatable, non-modifiable
        """
        return self._source_volume_node
    @source_volume_node.setter
    def source_volume_node(self, val):
        if val != None:
            self.validate('source_volume_node', val)
        self._source_volume_node = val
    
    _destination_vserver = None
    @property
    def destination_vserver(self):
        """
        Specifies the name of the destination Vserver for the
        relationship. The name of the destination volume must
        also be specified if using this parameter.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_vserver
    @destination_vserver.setter
    def destination_vserver(self, val):
        if val != None:
            self.validate('destination_vserver', val)
        self._destination_vserver = val
    
    _destination_location = None
    @property
    def destination_location(self):
        """
        Specifies the destination endpoint of the  SnapMirror
        relationship in the format [vserver:]volume. This format
        may change in the future.
        The destination endpoint can be specified using the
        location format above, or by specifying the parameters
        for the name of the destination Vserver and the name of
        the destination volume.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_location
    @destination_location.setter
    def destination_location(self, val):
        if val != None:
            self.validate('destination_location', val)
        self._destination_location = val
    
    _progress_last_updated = None
    @property
    def progress_last_updated(self):
        """
        Specifies the timestamp indicating when the progress of
        the ongoing transfer was last updated.
        Attributes: non-creatable, non-modifiable
        """
        return self._progress_last_updated
    @progress_last_updated.setter
    def progress_last_updated(self, val):
        if val != None:
            self.validate('progress_last_updated', val)
        self._progress_last_updated = val
    
    _destination_volume = None
    @property
    def destination_volume(self):
        """
        Specifies the name of destination volume for the
        SnapMirror relationshp. The name of the destination
        Vserver must also be specified if using this parameter.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._destination_volume
    @destination_volume.setter
    def destination_volume(self, val):
        if val != None:
            self.validate('destination_volume', val)
        self._destination_volume = val
    
    _source_location = None
    @property
    def source_location(self):
        """
        Specifies the source endpoint of the SnapMirror
        relationship in the format [vserver:]volume. This format
        may change in the future.
        The source endpoint can be specified using the location
        format above, or by specifying the parameters for the
        name of the source Vserver and the name of the source
        volume.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._source_location
    @source_location.setter
    def source_location(self, val):
        if val != None:
            self.validate('source_location', val)
        self._source_location = val
    
    _relationship_id = None
    @property
    def relationship_id(self):
        """
        Specifies the SnapMirror relationship ID.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._relationship_id
    @relationship_id.setter
    def relationship_id(self, val):
        if val != None:
            self.validate('relationship_id', val)
        self._relationship_id = val
    
    _relationship_status = None
    @property
    def relationship_status(self):
        """
        Specifies the SnapMirror relationship status. This
        parameter is present only if at least one transfer has
        been performed since the node hosting the source volume
        joined the quorum. Possible values are:
        <ul>
        <li>'idle',
        <li>'transferring'
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._relationship_status
    @relationship_status.setter
    def relationship_status(self, val):
        if val != None:
            self.validate('relationship_status', val)
        self._relationship_status = val
    
    _is_constituent = None
    @property
    def is_constituent(self):
        """
        Specifies whether or not the SnapMirror relationship is
        between Infinite Volume constituent volumes.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_constituent
    @is_constituent.setter
    def is_constituent(self, val):
        if val != None:
            self.validate('is_constituent', val)
        self._is_constituent = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-destination-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'source-vserver',
            'source-volume',
            'transfer-progress',
            'relationship-type',
            'source-volume-node',
            'destination-vserver',
            'destination-location',
            'progress-last-updated',
            'destination-volume',
            'source-location',
            'relationship-id',
            'relationship-status',
            'is-constituent',
        ]
    
    def describe_properties(self):
        return {
            'source_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'transfer_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'relationship_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_volume_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'progress_last_updated': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'relationship_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'relationship_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_constituent': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
