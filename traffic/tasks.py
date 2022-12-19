import json
import random
import subprocess, os
import time
from celery import shared_task

@shared_task(queue="main")
def retrieve_traffic(user):
    usage= 0
    data1=None
    data2=None
    side1="downlink"
    side2="uplink"
    data1=subprocess.check_output('/root/v2/v2ctl api --server=172.17.0.2:54321 StatsService.GetStats ' + "'" + 'name: "user>>>' + user + '>>>traffic>>>' + side1 + '" reset: true' + "'" + '  2>/dev/null  | grep value | cut -d: -f2 | tr -d " "', shell = True)
    data2 = subprocess.check_output('/root/v2/v2ctl api --server=172.17.0.2:54321 StatsService.GetStats ' + "'" + 'name: "user>>>' + user + '>>>traffic>>>' + side2 + '" reset:true ' + "'" + ' 2>/dev/null | grep value | cut -d: -f2 | tr -d " "', shell = True)
    if data1 != None:
        if data1.decode("utf-8") != '':
            usage += int(data1.decode("utf-8"))
    if data2 != None:
        if data2.decode("utf-8") != '':
            usage += int(data2.decode("utf-8"))
    return usage


@shared_task(queue="main")
def update_config(config:dict, cdn:str):
    if not isinstance(config, dict) or len(list(config)) == 0:
        raise ValueError(f"invalid config file recieved! \n {config}")
    if not cdn in ["cloudflare","drak"]:
        raise ValueError(f"invalid cdn provider: {cdn}")
    with open(f"config-{cdn}.json","w") as out:
        json.dump(config,out)
    time.sleep(random.randint(1,5)+random.randint(1,10)/10)
    os.system(f"docker restart v2ray-{cdn}")
