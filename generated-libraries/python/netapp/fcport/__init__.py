from netapp.connection import NaConnection
from fc_ports import FcPorts # 4 properties
from link_state_info import LinkStateInfo # 4 properties

class FcportConnection(NaConnection):
    
    def fcport_set_offline(self, adapter_name):
        """
        Offline a specific adapter on this system.
        This API should be used with care,
        as it can have adverse side effects, which you lose access to
        all devices of that port.
        The operation of offlining the already offlined adapter
        will be considered success.
        
        :param adapter_name: The adapter name is either a slot number, or, if a port letter
                is also presented, a slot number and port letter concatenated into
                a single name -- for example, "8a" or "11b".  If adapter-name
                is not supplied, the command will  return EAPIMISSINGARGUMENT.
        """
        return self.request( "fcport-set-offline", {
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcport_get_link_state(self, node_name, adapter_name):
        """
        Get the link state of a specific adapter on this system.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF.
                This is the storage system name the command will
                be executed on.
        
        :param adapter_name: The adapter name is either a slot number, or, if a port letter
                is also presented, a slot number and port letter concatenated into
                a single name -- for example, "8a" or "11b".  If adapter-name
                is not supplied, the command will return EAPIMISSINGARGUMENT.
        """
        return self.request( "fcport-get-link-state", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
            'adapter-name': [ basestring, False ],
            'adapter-link-state': [ LinkStateInfo, True ],
        } )
    
    def fcport_set_online(self, adapter_name):
        """
        Online a specific adapter on this system.
        The operation of onlining the already onlined adapter
        will be considered success.
        
        :param adapter_name: The adapter name is either a slot number, or, if a port letter
                is also presented, a slot number and port letter concatenated into
                a single name -- for example, "8a" or "11b".  If adapter-name
                is not supplied, the command will  return EAPIMISSINGARGUMENT.
        """
        return self.request( "fcport-set-online", {
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcport_reset_dev(self, device_id):
        """
        When invoked the device will be reset. The device will be
        temporarily suspended while it is reset, after which it will resume
        processing device operations.
        This command should be used with care  as it can have adverse effects,
        for instance pending commands to the device will be aborted when issuing
        this command.
        @test
        
        :param device_id: The device id is presented as a slot number followed by the port letter
                concatenated with the device-id. These two parts are separated by a period.
                For example 6b.5
                If  the device-id is omitted EAPIMISSINGARGUMENT will be returned.
                If the device-id is invalid EINVALIDINPUTERROR will be returned.
        """
        return self.request( "fcport-reset-dev", {
            'device_id': [ device_id, 'device-id', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def fcport_send_lip(self, loop_id):
        """
        This will initiate a loop initialization on the specified fibrechannel loop port.
        The loop will be temporarily suspended while it is initialized,
        after which it will resume processing loop operations.
        This command should be used with care, because it can have adverse effects,
        like pending commands will be aborted when issuing this command.
        @test
        
        :param loop_id: The loop id is presented as a slot number and port letter concatenated (for example 6a).
                If  the loop-id is omitted EAPIMISSINGARGUMENT will be returned.
                If the loop-id is invalid EINVALIDINPUTERROR will be returned.
        """
        return self.request( "fcport-send-lip", {
            'loop_id': [ loop_id, 'loop-id', [ basestring, 'None' ], False ],
        }, {
        } )
