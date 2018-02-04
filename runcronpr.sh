#!/usr/bin/env bash

echo "running runcron.sh" >> logfile.txt
echo $PWD >> logfile.txt
#source /home/cky/project/syndicator/key.sh
#export DB_PASS={Your password}
#export E_TOKEN={Your Token}
export E_TOKEN="H75KJFJOQXM2XBZLVGOE"

cd /opt/python/current/app && /opt/python/run/venv/bin/python /opt/python/current/app/manage.py runcrons

