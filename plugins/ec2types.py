#!/usr/bin/python3

def lambda_handler(e):
    for i in e:
        print(i + ":" +e[i]["Type"])
