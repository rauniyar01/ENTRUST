#!/bin/bash
ps aux | grep 'ddos_attack_simulation.py' | grep -v grep | awk '{print "ddos_attack_simulation,host=raspberry pid="$2",user="$1",cpu="$3",mem="$4""}'