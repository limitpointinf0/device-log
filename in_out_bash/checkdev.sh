#!/bin/bash
name="$1"
sleep_t="$2"

while [ true ]; do
command="$(arp-scan -l | grep "\<$name\>")"
if [ "$command" != "" ]; then
printf "$(date), in\n" >> $name.log
printf "$(date), in\n"
else
printf "$(date), out\n" >> $name.log
printf "$(date), out\n"
fi
sleep $sleep_t
done 
