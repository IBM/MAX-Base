[![Build Status](https://travis-ci.org/IBM/MAX-Base.svg?branch=master)](https://travis-ci.org/IBM/MAX-Base)

This repository contains code for building the "base" Docker image used by all other
[Model Asset Exchange](https://developer.ibm.com/exchanges/models/) models.

The base image is intended to contain requirements common across all MAX models to reduce the amount of packages that
need to be downloaded when downloading or building multiple containers for MAX models.

The Docker image is hosted on the [CODAIT Dockerhub profile](https://hub.docker.com/r/codait/max-base) and can be used as a base image from which to extend a Dockerfile for a MAX model:

```Dockerfile
FROM codait/max-base:VERSION
```

Where `VERSION` is the relevant version of the base image, or `latest` for the master branch build.
