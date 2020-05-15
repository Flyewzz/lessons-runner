#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

cd {path}
source /env/bin/activate
python main.py --type=webinar --url={url} --name="name" --wait-time=60 --presence-time=16 &