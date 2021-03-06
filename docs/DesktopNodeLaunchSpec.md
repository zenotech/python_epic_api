# DesktopNodeLaunchSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_code** | **str** | node_code of the node type to launch. Valid values are obtained from the catalog/desktop/ endpoint | 
**runtime** | **int** | Runtime in hours to run this desktop node for. This is the maximum runtime as the viz node can be stopped earlier and you will only be charged for the elapsed time | 
**secure_ip** | **bool** | Should we restrict which IPs can connect to this node? | [optional] [default to False]
**ip_address** | **str** | IPv4 Address to restrict connections to this node from | [optional] 
**invoice_reference** | **str** | Invoice reference - this text will appear on the monthly invoice against this nodes charges | [optional] 
**data_path** | [**DataSpec**](DataSpec.md) |  | 
**mount_type** | **str** | How should the data folder be mounted to the desktop. Offline takes a copy of the data and will not be automatically synced back to the data store. | 
**project** | **int** | Project ID to bill this desktop node against | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


