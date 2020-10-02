Azure Disk Encryption (ADE) can be enabled on a local disk with Terraform with the `azurerm_virtual_machine_extension`. The sample below shows how to enable it.

```hcl
resource "azurerm_virtual_machine_extension" "disk-encryption" {
  name                       = "DiskEncryption"
  virtual_machine_id         = azurerm_windows_virtual_machine.this.id
  publisher                  = "Microsoft.Azure.Security"
  type                       = "AzureDiskEncryption"
  type_handler_version       = "2.2"
  auto_upgrade_minor_version = true

  settings = <<SETTINGS
{
  "EncryptionOperation": "EnableEncryption",
  "KeyVaultURL": "https://${local.key_vault_name}.vault.azure.net",
  "KeyVaultResourceId": "/subscriptions/${data.azurerm_client_config.current.subscription_id}/resourceGroups/${azurerm_resource_group.this.name}/providers/Microsoft.KeyVault/vaults/${azurerm_key_vault.this.name}",
  "KeyEncryptionAlgorithm": "RSA-OAEP",
  "KeyEncryptionKeyURL": null,
  "KekVaultResourceId": "",
  "VolumeType": "All"
}
SETTINGS
}
```