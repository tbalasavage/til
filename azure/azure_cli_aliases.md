# Motivation
I regretfully don't use the Azure CLI as much as I should because the syntax for simple operations can be verbose and time consuming to enter. To help remedy this, install the Azure CLI alias extension and create custom aliases that adapt to your workflow. The aliases use Jinja2 so they can be simple or powerful.

# Installation
```
az extension add --name alias
```

# Example
Add a storage container with the form `<use>-container-<environment>-tb`:

```
az alias create --name "create-storage-container {{ account_name }} {{ use }} {{ environment }} " --command "storage container create --account-name {{ account_name }} --name {{ use }}-container-{{ environment }}-tb"
```

## Example usage
```
az create-storage-container terraform-storage-dev-tb usecase1 dev
```

# Alias storage
Aliases are listed in `~/.azure/alias`

# References
More info can be found in the [Azure CLI docs](https://docs.microsoft.com/en-us/cli/azure/azure-cli-extension-alias?view=azure-cli-latest)