The `HISTCONTROL` environment variable allows you to control what is saved by Bash history. There are multiple options, each of which may be set in a colon (:) separated list.
* `ignorespace`: Commands that begin with a space will not be saved
* `ignoredups`: Commands that match a previously saved command will not be saved
* `ignoreboth`: Shorthand for both `ignorespace` and `ignoredups`
* `erasedups`: Commands that match the current command are removed prior to saving the current command. The current command is saved.

If `HISTCONTROL` is not set, all commands are saved.