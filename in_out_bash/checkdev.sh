#!/bin/bash
name="$1"
sleep_t="$2"

while [ true ]; do
command="$(arp-scan -l | grep "\<$name\>")"
if [ "$command" != "" ]; then
printf "$(date -u), in\n" >> $name.log
printf "$(date -u), in\n"
else
printf "$(date -u), out\n" >> $name.log
printf "$(date -u), out\n"
fi
sleep $sleep_t
done 
