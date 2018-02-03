#!/usr/bin/env bash

echo "running runcron.sh" >> logfile.txt
echo $PWD >> logfile.txt
source /home/cky/project/syndicator/key.sh
#export DB_PASS={Your password}
#export E_TOKEN={Your Token}

cd /home/cky/project/syndicator && /home/cky/vp35/bin/python /home/cky/project/syndicator/manage.py runcrons

