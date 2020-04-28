Found on a [blog post by Hamid Mosalla](https://hamidmosalla.com/2020/04/05/xunit-part-8-using-theorydata-instead-of-memberdata-and-classdata/)

One option for using `ClassData` with an XUnit `Theory` is creating a class like the below.

```
public class ClassDataGenerator : IEnumerable<object[]>
{
    private readonly List<object[]> _data = new List<object[]>
    {
        new object[] {new MyObject("parameter1")},
        new object[] {new MyObject("parameter2")}
    };

    public IEnumerator<object[]> GetEnumerator() => _data.GetEnumerator();

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}
```

There are at least two problems:
1. There's no type check at compile time due to the `object[]`.
1. There's unnecessary code that isn't directly related to the test.

Instead, you can can create a class that extends `TheoryData`. The class is strongly-typed and more simple to read than the example above. A rewritten `ClassDataGenerator` is shown below.

```
public class ClassDataGenerator : TheoryData<MyObject>
{
    public ClassDataGeneratorUsingTheoryData()
    {
        Add(new MyObject("parameter1"));
        Add(new MyObject("parameter2"));
    }
}

```
To use it, apply the `Theory` and `ClassData` attributes:
```
[Theory]
[ClassData(typeof(ClassDataGenerator))]
public void MyFeatureDoesWhatIExpect()
{
    /* test code */
}
```