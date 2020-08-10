If a string interpolation includes braces `{` or `}`, escape them by duplicating the brace as shown below.

```python
print(f'{{"key": "{value}"}}')
```