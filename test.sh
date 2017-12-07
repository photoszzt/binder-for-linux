#!/bin/bash

# sudo servicemanager/servicemanager &

payload_size=(4 16 64 256 1024 4096 16384 65536 262144)

for payload in ${payload_size[@]}; do
    for core in `seq 0 3`; do
        name=$payload\_$core.log
        sudo test/binderAddInts -s 0 -c $core -n 10000 -p $payload &> ./test_res/$name
    done
done
