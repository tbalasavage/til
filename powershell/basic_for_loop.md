```powershell
# array declaration
$array = @("value1", "value2")
```

```powershell
# loop through using index and print values
for ($i=0; $i -lt $array.length; $i++)
{
    $array[$i]
}
<# 
   Prints:
   value1
   value2
#>
```

```powershell
# use Foreach and loop through array and print values
Foreach ($i in $array)
{
    $i
}
<# 
   Prints:
   value1
   value2
#>
```
