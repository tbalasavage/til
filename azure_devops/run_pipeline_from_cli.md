```bash
# add DevOps extension
 az extension add --name azure-devops

# login (again)
az login

# configure default project
az devops configure --defaults organization=https://dev.azure.com/<organization> project=<project>

# run pipeline
# example: az pipelines run --name AwesomePipeline --branch tb/feature/ab#1001
az pipelines run --name <pipeline name> --branch <case-sensitive branch name>

# add alias for running a given pipeline by branch
# example: az alias create --name "run-awesome-pipeline {{ branch }}" --command "pipelines run --name AwesomePipeline --branch {{ branch }}"
az alias create --name "<your command> {{ branch }}" --command "pipelines run --name <pipeline name> --branch {{ branch }}"
```