# simple-load

## Abstract

Load testing framework for R700 readers. All of the functionality will be placing some sort of load on a reader. Ideally this would be able to run on it's own as well as be importable for behave tests.

## Tools

### Locust

The load testing framework for hammering the api and MQTT is Locust. This should wrap that in order to provide easy to use calls for adding and manipulating load. 
