# argecho
The service parses and decodes the parameters in a URL query string and returns them to the caller as a JSON object.

## Limitations
Only correctly formed parameters will be returned to the caller. 

For example,
```sh
http://localhost:8080/?foo=bar&baz=quux%21
```

will be succesfully mapped to:
```json
{"foo":"bar","baz":"quux!"}
```

But in this url only first parameter will be returned to the caller
```sh
http://localhost:8080/?foo=bar&=123
```
as
```json
{"foo":"bar"}
```

Parameters with the same name but different values are not supported by the design of this service. Handling of such parameters will result in JSON data with duplicated keys and invalid values. _So, make sure that that your url do not have duplicated parameters._
```sh
http://localhost:8080/?foo=bar&foo=quux%21
```
and this will be returned as

```json
{"foo":"bar","foo":"bar"}
``` 

# Installation
Before starting of this service, prepare the environment and install *Docker* (https://docs.docker.com/engine/install/) and *Python3* (https://www.python.org/downloads/) to test the service. Also you might need to install *urllib3* python library:
```sh
$ pip3 install urllib3
```

## Build Docker Image
```sh
$ docker build -t argecho .
```

## Run Service
```sh
$ docker run --name argecho -p 8080:80 -d argecho
```

## Run Tests
```sh
$ ./test.py
```

<!-- CONTACT -->
## Contact

Your Name - [Elena Bugaenko](https://www.linkedin.com/in/elena-bugaenko-4808002a/) - buglenka@mail.ru

Project Link: [https://github.com/buglenka/argecho](https://github.com/buglenka/argecho)

<p align="right">(<a href="#top">back to top</a>)</p>
