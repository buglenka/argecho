#!/usr/bin/env python3
import urllib3
import json

testCases = [
    ('http://localhost:8080/?foo=bar&baz=quux%21','{"foo":"bar","baz":"quux!"}'),
    ('http://localhost:8080/','{}'),
    ('http://localhost:8080/?foo=bar&=123','{"foo":"bar"}'),
    ('http://localhost:8080/?foo=bar&foo=quux%21','{"foo":"bar","foo":"bar"}'),
]

http = urllib3.PoolManager()

for i, case in enumerate(testCases):
    response = http.request("GET", case[0])
    
    data = response.data.decode("utf-8")

    objReceived = json.loads(data)
    objExpected = json.loads(case[1])

    print('Test case {}: {}, URL: {}'.format(i, 'Passed' if objReceived == objExpected else 'Failed', case[0]))
