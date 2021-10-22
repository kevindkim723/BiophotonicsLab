#!/bin/bash
#bash script that records the temperature of raspberry pi

touch tempmod.txt
temp=$(vcgencmd measure_temp)
echo $temp -- `date` >> tempmod.txt

