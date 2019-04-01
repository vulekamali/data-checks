```
$ python --version
Python 3.7.3
```

ISsues

- Warnings are not errors when using CLI
- when schema file is invalid json, error `Warning: Data Package "epre-2018-19/datapackage.json" has a loading error "Not resolved Local URI "schema.json" for resource.schema"` isn't helpful.
- enum constraint on financial year isn't invalidating the dataset