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

from .azure_vm_workload_protectable_item import AzureVmWorkloadProtectableItem


class AzureVmWorkloadSQLDatabaseProtectableItem(AzureVmWorkloadProtectableItem):
    """Azure VM workload-specific protectable item representing SQL Database.

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup management to backup an
     item.
    :type backup_management_type: str
    :param workload_type: Type of workload for the backup management
    :type workload_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param protectable_item_type: Required. Constant filled by server.
    :type protectable_item_type: str
    :param parent_name: Name for instance or AG
    :type parent_name: str
    :param parent_unique_name: Parent Unique Name is added to provide the
     service formatted URI Name of the Parent
     Only Applicable for data bases where the parent would be either Instance
     or a SQL AG.
    :type parent_unique_name: str
    :param server_name: Host/Cluster Name for instance or AG
    :type server_name: str
    :param is_auto_protectable: Indicates if protectable item is
     auto-protectable
    :type is_auto_protectable: bool
    :param is_auto_protected: Indicates if protectable item is auto-protected
    :type is_auto_protected: bool
    :param subinquireditemcount: For instance or AG, indicates number of DBs
     present
    :type subinquireditemcount: int
    :param subprotectableitemcount: For instance or AG, indicates number of
     DBs to be protected
    :type subprotectableitemcount: int
    :param prebackupvalidation: Pre-backup validation for protectable objects
    :type prebackupvalidation:
     ~azure.mgmt.recoveryservicesbackup.models.PreBackupValidation
    """

    _validation = {
        'protectable_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'protectable_item_type': {'key': 'protectableItemType', 'type': 'str'},
        'parent_name': {'key': 'parentName', 'type': 'str'},
        'parent_unique_name': {'key': 'parentUniqueName', 'type': 'str'},
        'server_name': {'key': 'serverName', 'type': 'str'},
        'is_auto_protectable': {'key': 'isAutoProtectable', 'type': 'bool'},
        'is_auto_protected': {'key': 'isAutoProtected', 'type': 'bool'},
        'subinquireditemcount': {'key': 'subinquireditemcount', 'type': 'int'},
        'subprotectableitemcount': {'key': 'subprotectableitemcount', 'type': 'int'},
        'prebackupvalidation': {'key': 'prebackupvalidation', 'type': 'PreBackupValidation'},
    }

    def __init__(self, **kwargs):
        super(AzureVmWorkloadSQLDatabaseProtectableItem, self).__init__(**kwargs)
        self.protectable_item_type = 'SQLDataBase'
