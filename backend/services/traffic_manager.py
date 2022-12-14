import subprocess, datetime

from backend.environments import V2RAY_HOST, V2RAY_PORT


def get_bytes_v2ray(user):
    usage= 0
    data1=None
    data2=None
    side1="downlink"
    side2="uplink"
    data1=subprocess.check_output(f"./v2ctl api --server={V2RAY_HOST}:{V2RAY_PORT} StatsService.GetStats " + "'" + 'name: "user>>>' + user + '>>>traffic>>>' + side1 + '" reset: true' + "'" + '  2>/dev/null  | grep value | cut -d: -f2 | tr -d " "', shell = True)
    data2 = subprocess.check_output(f"./v2ctl api --server={V2RAY_HOST}:{V2RAY_PORT} StatsService.GetStats " + "'" + 'name: "user>>>' + user + '>>>traffic>>>' + side2 + '" reset:true ' + "'" + ' 2>/dev/null | grep value | cut -d: -f2 | tr -d " "', shell = True)
    if data1 != None:
        if data1.decode("utf-8") != '':
            usage += int(data1.decode("utf-8"))
    if data2 != None:
        if data2.decode("utf-8") != '':
            usage += int(data2.decode("utf-8"))
    return usage
