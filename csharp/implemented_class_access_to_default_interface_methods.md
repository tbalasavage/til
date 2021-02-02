```c#
public interface IInterface {
    public string CreateGreeting(string name) 
    {
        return $"Hi, {name}";
    }
}

public class ImplementingClass : IInterface
...
```

In the interface above, `CreateGreeting` will not be available to `ImplementingClass`; it will only be available when `ImplementingClass` class is instantiated. You can use `CreateGreeting` in `ImplementingClass` by casting `this` to `IInterface`.