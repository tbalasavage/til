Secrets in Key Vault can be referenced in an app setting using the following syntax:
```
@Microsoft.KeyVault(SecretUri=https://myvault.vault.azure.net/secrets/mysecret/ec96f02080254f109c51a1f14cdb1931)
```
```
@Microsoft.KeyVault(VaultName=myvault;SecretName=mysecret;SecretVersion=ec96f02080254f109c51a1f14cdb1931)
```

The drawback is that the version appears to be required, which means when the value changes, the app setting must be updated.