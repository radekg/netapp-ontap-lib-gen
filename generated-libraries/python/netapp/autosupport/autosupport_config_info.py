from netapp.netapp_object import NetAppObject

class AutosupportConfigInfo(NetAppObject):
    """
    AutoSupport configuration data
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
    
    _last_timestamp = None
    @property
    def last_timestamp(self):
        """
        The timestamp of the last generated AutoSupport message.
        The time value is in seconds since January 1, 1970 UTC.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_timestamp
    @last_timestamp.setter
    def last_timestamp(self, val):
        if val != None:
            self.validate('last_timestamp', val)
        self._last_timestamp = val
    
    _is_throttle_enabled = None
    @property
    def is_throttle_enabled(self):
        """
        Specifies whether to enable / disable throttling to
        prevent a potential avalanche of AutoSupport messages.
        Attributes: non-creatable, modifiable
        """
        return self._is_throttle_enabled
    @is_throttle_enabled.setter
    def is_throttle_enabled(self, val):
        if val != None:
            self.validate('is_throttle_enabled', val)
        self._is_throttle_enabled = val
    
    _ondemand_polling_interval = None
    @property
    def ondemand_polling_interval(self):
        """
        The AutoSupport OnDemand Client polling rate in minutes.
        Attributes: non-creatable, modifiable
        """
        return self._ondemand_polling_interval
    @ondemand_polling_interval.setter
    def ondemand_polling_interval(self, val):
        if val != None:
            self.validate('ondemand_polling_interval', val)
        self._ondemand_polling_interval = val
    
    _is_nht_data_enabled = None
    @property
    def is_nht_data_enabled(self):
        """
        Used to enable / disable collection of disk health data.
        Attributes: non-creatable, modifiable
        """
        return self._is_nht_data_enabled
    @is_nht_data_enabled.setter
    def is_nht_data_enabled(self, val):
        if val != None:
            self.validate('is_nht_data_enabled', val)
        self._is_nht_data_enabled = val
    
    _max_smtp_size = None
    @property
    def max_smtp_size(self):
        """
        Delivery size limit for the SMTP transport protocol (in
        bytes).
        Attributes: non-creatable, modifiable
        """
        return self._max_smtp_size
    @max_smtp_size.setter
    def max_smtp_size(self, val):
        if val != None:
            self.validate('max_smtp_size', val)
        self._max_smtp_size = val
    
    _is_perf_data_enabled = None
    @property
    def is_perf_data_enabled(self):
        """
        Used to enable / disable collection of Performance
        AutoSupport data.
        Attributes: non-creatable, modifiable
        """
        return self._is_perf_data_enabled
    @is_perf_data_enabled.setter
    def is_perf_data_enabled(self, val):
        if val != None:
            self.validate('is_perf_data_enabled', val)
        self._is_perf_data_enabled = val
    
    _transport = None
    @property
    def transport(self):
        """
        The name of the transport protocol used to deliver
        AutoSupport messages.
        Attributes: non-creatable, modifiable
        Possible values:
        <ul>
        <li> "smtp"      ,
        <li> "http"      ,
        <li> "https"
        </ul>
        """
        return self._transport
    @transport.setter
    def transport(self, val):
        if val != None:
            self.validate('transport', val)
        self._transport = val
    
    _ondemand_server_url = None
    @property
    def ondemand_server_url(self):
        """
        The AutoSupport OnDemand Server URL.
        Attributes: non-creatable, modifiable
        """
        return self._ondemand_server_url
    @ondemand_server_url.setter
    def ondemand_server_url(self, val):
        if val != None:
            self.validate('ondemand_server_url', val)
        self._ondemand_server_url = val
    
    _post_url = None
    @property
    def post_url(self):
        """
        The URL used to deliver AutoSupport messages via HTTP
        POST.
        Attributes: non-creatable, modifiable
        """
        return self._post_url
    @post_url.setter
    def post_url(self, val):
        if val != None:
            self.validate('post_url', val)
        self._post_url = val
    
    _from = None
    @property
    def from(self):
        """
        The e-mail address of the local administrator, used as
        the sender of the AutoSupport message.
        Attributes: non-creatable, modifiable
        """
        return self._from
    @from.setter
    def from(self, val):
        if val != None:
            self.validate('from', val)
        self._from = val
    
    _mail_hosts = None
    @property
    def mail_hosts(self):
        """
        The name of the mail server(s) used to deliver
        AutoSupport messages via SMTP.  Both host names and IP
        addresses may be used as valid input. One can optionally
        specify a username/password for authentication with the
        mailserver(rfc4954).
        Attributes: non-creatable, modifiable
        """
        return self._mail_hosts
    @mail_hosts.setter
    def mail_hosts(self, val):
        if val != None:
            self.validate('mail_hosts', val)
        self._mail_hosts = val
    
    _max_http_size = None
    @property
    def max_http_size(self):
        """
        Delivery size limit for the HTTP transport protocol (in
        bytes).
        Attributes: non-creatable, modifiable
        """
        return self._max_http_size
    @max_http_size.setter
    def max_http_size(self, val):
        if val != None:
            self.validate('max_http_size', val)
        self._max_http_size = val
    
    _is_reminder_enabled = None
    @property
    def is_reminder_enabled(self):
        """
        Specifies whether to enable / disable AutoSupport
        reminders.
        Attributes: non-creatable, modifiable
        """
        return self._is_reminder_enabled
    @is_reminder_enabled.setter
    def is_reminder_enabled(self, val):
        if val != None:
            self.validate('is_reminder_enabled', val)
        self._is_reminder_enabled = val
    
    _to = None
    @property
    def to(self):
        """
        Specifies up to five recipients of full AutoSupport
        e-mail messages.
        Attributes: non-creatable, modifiable
        """
        return self._to
    @to.setter
    def to(self, val):
        if val != None:
            self.validate('to', val)
        self._to = val
    
    _partner_address = None
    @property
    def partner_address(self):
        """
        Specifies up to five partner vendor recipients of full
        AutoSupport e-mail messages.
        Attributes: non-creatable, modifiable
        """
        return self._partner_address
    @partner_address.setter
    def partner_address(self, val):
        if val != None:
            self.validate('partner_address', val)
        self._partner_address = val
    
    _put_url = None
    @property
    def put_url(self):
        """
        The URL used to deliver AutoSupport messages via HTTP
        PUT.
        Attributes: non-creatable, modifiable
        """
        return self._put_url
    @put_url.setter
    def put_url(self, val):
        if val != None:
            self.validate('put_url', val)
        self._put_url = val
    
    _is_private_data_removed = None
    @property
    def is_private_data_removed(self):
        """
        Used to enable / disable removal of customer-supplied
        data.
        Attributes: non-creatable, modifiable
        """
        return self._is_private_data_removed
    @is_private_data_removed.setter
    def is_private_data_removed(self, val):
        if val != None:
            self.validate('is_private_data_removed', val)
        self._is_private_data_removed = val
    
    _is_ondemand_remote_diag_enabled = None
    @property
    def is_ondemand_remote_diag_enabled(self):
        """
        Specifies whether the AutoSupport OnDemand Remote
        Diagnostics feature is enabled. Default is true.
        Attributes: non-creatable, modifiable
        """
        return self._is_ondemand_remote_diag_enabled
    @is_ondemand_remote_diag_enabled.setter
    def is_ondemand_remote_diag_enabled(self, val):
        if val != None:
            self.validate('is_ondemand_remote_diag_enabled', val)
        self._is_ondemand_remote_diag_enabled = val
    
    _last_subject = None
    @property
    def last_subject(self):
        """
        The subject field of the last generated AutoSupport
        message.
        Attributes: non-creatable, non-modifiable
        """
        return self._last_subject
    @last_subject.setter
    def last_subject(self, val):
        if val != None:
            self.validate('last_subject', val)
        self._last_subject = val
    
    _noteto = None
    @property
    def noteto(self):
        """
        Specifies up to five recipients of short AutoSupport
        e-mail messages.
        Attributes: non-creatable, modifiable
        """
        return self._noteto
    @noteto.setter
    def noteto(self, val):
        if val != None:
            self.validate('noteto', val)
        self._noteto = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Specifies whether the AutoSupport daemon is enabled.
        When this setting is disabled, delivery of all
        AutoSupport messages is turned off.
        Attributes: non-creatable, modifiable
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _periodic_tx_window = None
    @property
    def periodic_tx_window(self):
        """
        The transmission window (seconds).
        Attributes: non-creatable, modifiable
        """
        return self._periodic_tx_window
    @periodic_tx_window.setter
    def periodic_tx_window(self, val):
        if val != None:
            self.validate('periodic_tx_window', val)
        self._periodic_tx_window = val
    
    _proxy_url = None
    @property
    def proxy_url(self):
        """
        Optional proxy host for AutoSupport message delivery via
        HTTP.
        Attributes: non-creatable, modifiable
        """
        return self._proxy_url
    @proxy_url.setter
    def proxy_url(self, val):
        if val != None:
            self.validate('proxy_url', val)
        self._proxy_url = val
    
    _is_local_collection_enabled = None
    @property
    def is_local_collection_enabled(self):
        """
        Used to enable / disable collection of AutoSupport data
        when the AutoSupport daemon is disabled.  When this
        setting is true, collection of AutoSupport data will
        still be done if is-enabled is false.
        Attributes: non-creatable, modifiable
        """
        return self._is_local_collection_enabled
    @is_local_collection_enabled.setter
    def is_local_collection_enabled(self, val):
        if val != None:
            self.validate('is_local_collection_enabled', val)
        self._is_local_collection_enabled = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The name of the filer that owns the AutoSupport
        configuration.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _payload_format = None
    @property
    def payload_format(self):
        """
        The format used to compress the AutoSupport message
        payload.
        Attributes: non-creatable, modifiable
        Possible values:
        <ul>
        <li> "7z"   - 7-Zip Archive,
        <li> "tgz"  - Zipped Tarball
        </ul>
        """
        return self._payload_format
    @payload_format.setter
    def payload_format(self, val):
        if val != None:
            self.validate('payload_format', val)
        self._payload_format = val
    
    _support_address = None
    @property
    def support_address(self):
        """
        The e-mail address of Support.
        Attributes: non-creatable, modifiable
        """
        return self._support_address
    @support_address.setter
    def support_address(self, val):
        if val != None:
            self.validate('support_address', val)
        self._support_address = val
    
    _retry_count = None
    @property
    def retry_count(self):
        """
        The maximum number of delivery attempts for an
        AutoSupport message.
        Attributes: non-creatable, modifiable
        """
        return self._retry_count
    @retry_count.setter
    def retry_count(self, val):
        if val != None:
            self.validate('retry_count', val)
        self._retry_count = val
    
    _is_node_in_subject = None
    @property
    def is_node_in_subject(self):
        """
        Specifies whether the filer's hostname should be part of
        an AutoSupport message's subject field.
        Attributes: non-creatable, modifiable
        """
        return self._is_node_in_subject
    @is_node_in_subject.setter
    def is_node_in_subject(self, val):
        if val != None:
            self.validate('is_node_in_subject', val)
        self._is_node_in_subject = val
    
    _is_support_enabled = None
    @property
    def is_support_enabled(self):
        """
        Specifies whether AutoSupport notification to technical
        support is enabled.
        Attributes: non-creatable, modifiable
        """
        return self._is_support_enabled
    @is_support_enabled.setter
    def is_support_enabled(self, val):
        if val != None:
            self.validate('is_support_enabled', val)
        self._is_support_enabled = val
    
    _minimum_private_data_length = None
    @property
    def minimum_private_data_length(self):
        """
        Minimum Length for Sensitive Data
        Attributes: non-creatable, modifiable
        """
        return self._minimum_private_data_length
    @minimum_private_data_length.setter
    def minimum_private_data_length(self, val):
        if val != None:
            self.validate('minimum_private_data_length', val)
        self._minimum_private_data_length = val
    
    _is_ondemand_enabled = None
    @property
    def is_ondemand_enabled(self):
        """
        Specifies whether AutoSupport OnDemand is enabled.
        Default is true.
        Attributes: non-creatable, modifiable
        """
        return self._is_ondemand_enabled
    @is_ondemand_enabled.setter
    def is_ondemand_enabled(self, val):
        if val != None:
            self.validate('is_ondemand_enabled', val)
        self._is_ondemand_enabled = val
    
    _retry_interval = None
    @property
    def retry_interval(self):
        """
        The number of seconds to wait, after a failed delivery
        attempt, prior to re-transmitting an AutoSupport
        message.
        Attributes: non-creatable, modifiable
        """
        return self._retry_interval
    @retry_interval.setter
    def retry_interval(self, val):
        if val != None:
            self.validate('retry_interval', val)
        self._retry_interval = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'last-timestamp',
            'is-throttle-enabled',
            'ondemand-polling-interval',
            'is-nht-data-enabled',
            'max-smtp-size',
            'is-perf-data-enabled',
            'transport',
            'ondemand-server-url',
            'post-url',
            'from',
            'mail-hosts',
            'max-http-size',
            'is-reminder-enabled',
            'to',
            'partner-address',
            'put-url',
            'is-private-data-removed',
            'is-ondemand-remote-diag-enabled',
            'last-subject',
            'noteto',
            'is-enabled',
            'periodic-tx-window',
            'proxy-url',
            'is-local-collection-enabled',
            'node-name',
            'payload-format',
            'support-address',
            'retry-count',
            'is-node-in-subject',
            'is-support-enabled',
            'minimum-private-data-length',
            'is-ondemand-enabled',
            'retry-interval',
        ]
    
    def describe_properties(self):
        return {
            'last_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_throttle_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ondemand_polling_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_nht_data_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_smtp_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_perf_data_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'transport': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ondemand_server_url': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'post_url': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'from': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mail_hosts': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'max_http_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_reminder_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'to': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'partner_address': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'put_url': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_private_data_removed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_ondemand_remote_diag_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_subject': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'noteto': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'periodic_tx_window': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'proxy_url': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_local_collection_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'payload_format': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'support_address': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'retry_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_node_in_subject': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_support_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'minimum_private_data_length': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_ondemand_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'retry_interval': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
