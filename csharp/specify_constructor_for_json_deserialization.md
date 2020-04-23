```
public string Parameter1 { get; private set; }

public string Parameter2 { get; private set; }

[JsonConstructor]
public MyClass(string parameter1, string parameter2)
{
    Parameter1 = parameter1;
    Parameter2 = parameter2;
}
```