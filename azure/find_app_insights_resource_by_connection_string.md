# Install extension 
 ```bash
 az extension add --name application-insights
```

# Search by exact connection string
```bash
az monitor app-insights component show --query "[?connectionString == 'InstrumentationKey=<key>'].{name:applicationId}" -o table --subscription <subscriptionId>
```

# Search by partial connection string
```bash
az monitor app-insights component show --query "[?contains(connectionString, '<part of key>')].{name:applicationId}" -o table --subscription <subscriptionId>
```