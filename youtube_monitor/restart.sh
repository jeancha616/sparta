#!/bin/bash

kill -9 `ps -ef | grep 'app.py' | awk '{print $2}'`
sleep 3 
nohup python /home/ubuntu/myproject/app.py &
