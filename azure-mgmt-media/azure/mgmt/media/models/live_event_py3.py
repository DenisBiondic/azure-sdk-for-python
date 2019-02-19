# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class LiveEvent(TrackedResource):
    """The Live Event.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region of the resource.
    :type location: str
    :param description: The Live Event description.
    :type description: str
    :param input: Required. The Live Event input.
    :type input: ~azure.mgmt.media.models.LiveEventInput
    :param preview: The Live Event preview.
    :type preview: ~azure.mgmt.media.models.LiveEventPreview
    :param encoding: The Live Event encoding.
    :type encoding: ~azure.mgmt.media.models.LiveEventEncoding
    :ivar provisioning_state: The provisioning state of the Live Event.
    :vartype provisioning_state: str
    :ivar resource_state: The resource state of the Live Event. Possible
     values include: 'Stopped', 'Starting', 'Running', 'Stopping', 'Deleting'
    :vartype resource_state: str or
     ~azure.mgmt.media.models.LiveEventResourceState
    :param cross_site_access_policies: The Live Event access policies.
    :type cross_site_access_policies:
     ~azure.mgmt.media.models.CrossSiteAccessPolicies
    :param vanity_url: Specifies whether to use a vanity url with the Live
     Event.  This value is specified at creation time and cannot be updated.
    :type vanity_url: bool
    :param stream_options: The options to use for the LiveEvent.  This value
     is specified at creation time and cannot be updated.
    :type stream_options: list[str or
     ~azure.mgmt.media.models.StreamOptionsFlag]
    :ivar created: The exact time the Live Event was created.
    :vartype created: datetime
    :ivar last_modified: The exact time the Live Event was last modified.
    :vartype last_modified: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'input': {'required': True},
        'provisioning_state': {'readonly': True},
        'resource_state': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'input': {'key': 'properties.input', 'type': 'LiveEventInput'},
        'preview': {'key': 'properties.preview', 'type': 'LiveEventPreview'},
        'encoding': {'key': 'properties.encoding', 'type': 'LiveEventEncoding'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'LiveEventResourceState'},
        'cross_site_access_policies': {'key': 'properties.crossSiteAccessPolicies', 'type': 'CrossSiteAccessPolicies'},
        'vanity_url': {'key': 'properties.vanityUrl', 'type': 'bool'},
        'stream_options': {'key': 'properties.streamOptions', 'type': '[StreamOptionsFlag]'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
    }

    def __init__(self, *, input, tags=None, location: str=None, description: str=None, preview=None, encoding=None, cross_site_access_policies=None, vanity_url: bool=None, stream_options=None, **kwargs) -> None:
        super(LiveEvent, self).__init__(tags=tags, location=location, **kwargs)
        self.description = description
        self.input = input
        self.preview = preview
        self.encoding = encoding
        self.provisioning_state = None
        self.resource_state = None
        self.cross_site_access_policies = cross_site_access_policies
        self.vanity_url = vanity_url
        self.stream_options = stream_options
        self.created = None
        self.last_modified = None
