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

from .application_scoped_volume_creation_parameters import ApplicationScopedVolumeCreationParameters


class ApplicationScopedVolumeCreationParametersServiceFabricVolumeDisk(ApplicationScopedVolumeCreationParameters):
    """Describes parameters for creating application-scoped volumes provided by
    Service Fabric Volume Disks.

    All required parameters must be populated in order to send to Azure.

    :param description: User readable description of the volume.
    :type description: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param size_disk: Required. Volume size. Possible values include: 'Small',
     'Medium', 'Large'
    :type size_disk: str or ~azure.servicefabric.models.SizeTypes
    """

    _validation = {
        'kind': {'required': True},
        'size_disk': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'size_disk': {'key': 'sizeDisk', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationScopedVolumeCreationParametersServiceFabricVolumeDisk, self).__init__(**kwargs)
        self.size_disk = kwargs.get('size_disk', None)
        self.kind = 'ServiceFabricVolumeDisk'
