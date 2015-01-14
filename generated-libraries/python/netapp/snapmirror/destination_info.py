from netapp.netapp_object import NetAppObject

class DestinationInfo(NetAppObject):
    """
    Source location, destination location, and source snapshot
    of a snapmirrored pair.
    """
    
    _source_location = None
    @property
    def source_location(self):
        """
        The source location of the snapmirrored pair.
        The source location is of the
        volume form: &lt;filer&gt;:&lt;volume&gt;,
        or it is of the qtree form:
        &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;.
        In versions of ONTAP earlier than 7.0, there was a
        bug which omitted the filer name, so the volume form is:
        &lt;volume&gt;, and the qtree form is:
        /vol/&lt;volume&gt;/&lt;qtree&gt;.
        """
        return self._source_location
    @source_location.setter
    def source_location(self, val):
        if val != None:
            self.validate('source_location', val)
        self._source_location = val
    
    _source_snapshot = None
    @property
    def source_snapshot(self):
        """
        The source snapshot.
        """
        return self._source_snapshot
    @source_snapshot.setter
    def source_snapshot(self, val):
        if val != None:
            self.validate('source_snapshot', val)
        self._source_snapshot = val
    
    _destination_location = None
    @property
    def destination_location(self):
        """
        Destination location of the snapmirrored pair. The
        destination location is of the volume form:
        &lt;filer&gt;:&lt;volume&gt; or the qtree form:
        &lt;filer&gt;:/vol/&lt;volume&gt;/&lt;qtree&gt;
        or the clone form:
        &lt;filer&gt;:&lt;volume&gt;-&gt;[clone:&lt;clone_name&gt;].
        """
        return self._destination_location
    @destination_location.setter
    def destination_location(self, val):
        if val != None:
            self.validate('destination_location', val)
        self._destination_location = val
    
    @staticmethod
    def get_api_name():
          return "destination-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'source-location',
            'source-snapshot',
            'destination-location',
        ]
    
    def describe_properties(self):
        return {
            'source_location': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'source_snapshot': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'destination_location': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
