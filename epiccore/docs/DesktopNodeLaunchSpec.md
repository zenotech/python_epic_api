# DesktopNodeLaunchSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **int** | ID of the node_type. Valid values are obtained from the catalog/viznodetype/&lt;application_version&gt;/ endpoint | 
**application_version** | **int** | ID of the application_version to launch. Valid values are obtained from the catalog/viz/ endpoint | 
**connection** | **int** |  | 
**folder** | **int** | ID of the root folder to use for the viz node | 
**project** | **int** | Project ID to bill this desktop node against | [optional] 
**runtime** | **int** | Runtime in hours to run this desktop node for. This is the maximum runtime as the viz node can be stopped earlier and you will only be charged for the elapsed time | 
**mount_type** | **str** | Valid values are online or offline. Offline takes a copy of the data and will not be automatically synced back to the data store. | 
**secure_ip** | **bool** | Should we restrict which IPs can connect to this node? | [optional] [default to False]
**ip_address** | **str** | IPv4 Address to restrict connections to this node from | [optional] 
**invoice_reference** | **str** | Invoice reference - this text will appear on the monthly invoice against this nodes charges | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


