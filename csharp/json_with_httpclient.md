The package `System.Net.Http.Json` makes it easy to work with JSON API responses. The most simple way to use it is shown below.
```C#
await httpClient.GetFromJsonAsync<YourModel>(uri);
```

You can also use it on the response `Content` if needed:
```C#
await response.Content.ReadFromJsonAsync<YourModel>();
```