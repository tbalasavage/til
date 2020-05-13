`jq` is a bash utility for working with JSON. It is incredibly powerful and its use goes beyond the below.

# Input
Input may be provided via a file:
```
jq '.' <file name>
```

Input may also be piped in:
```
curl ... | jq '.'
```

# Examples
The examples below help to illustrate common usage. More can be found in the [documentation](https://stedolan.github.io/jq/manual/). The [jq playground](https://jqplay.org/) is an excellent resource for testing out usage.

*All examples below assume piped input*

## Basic usage
```
jq '.'
```

## Iterate over array
```
jq '.[]'
```

## Get length of input array/object
```
jq 'length'
```

## Create mapping of key presence
```
jq 'map(has("myKey"))'
```

## Create new object from first object in array
```
jq '.[0] | {newKey: .oldKey}
```