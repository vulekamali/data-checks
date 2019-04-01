```
$ python --version
Python 3.7.3
```

Issues

- Warnings are not errors when using CLI
- when schema file is invalid json, error `Warning: Data Package "epre-2018-19/datapackage.json" has a loading error "Not resolved Local URI "schema.json" for resource.schema"` isn't helpful.
- enum constraint on financial year isn't invalidating the dataset
- enum constraint on government field results in exceptopn `tableschema.exceptions.CastError: Field "government" has constraint "enum" which is not satisfied for value "Eastern"` instead of a human-readable error.