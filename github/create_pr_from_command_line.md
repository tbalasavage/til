Use the [GitHub CLI](https://cli.github.com/) to create a PR and never leave the terminal. By default, the PR will be opened against the default branch. Use the `--base` option to specify a different branch.

```bash
gh pr create --title "Add new cool feature" --body "This feature is cool. Look at it!" --assignee kidbrother,kidsister
```