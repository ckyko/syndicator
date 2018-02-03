#!/usr/bin/env bash

echo "get in runcron.sh success" >> logfile.txt
echo $PWD >> logfile.txt
export DB_PASS=321321
echo "export DB_PASS=321321" >> logfile.txt
#source home/cky/vp35/bin/activate
#echo "source /vp35/bin/activate" >> logfile.txt
#vp35/bin/python project/syndicator/manage.py runcrons > /home/cky/cronjob.log
#echo "run runcrons" >> logfile.txt
cd /home/cky/project/syndicator && /home/cky/vp35/bin/python /home/cky/project/syndicator/manage.py runcrons

