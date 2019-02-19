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

from msrest.serialization import Model


class RegisterPayload(Model):
    """Represents payload for Register action.

    :param registration_code: The registration code of the lab.
    :type registration_code: str
    """

    _attribute_map = {
        'registration_code': {'key': 'registrationCode', 'type': 'str'},
    }

    def __init__(self, *, registration_code: str=None, **kwargs) -> None:
        super(RegisterPayload, self).__init__(**kwargs)
        self.registration_code = registration_code
