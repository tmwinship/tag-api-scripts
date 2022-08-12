import requests
import json
import tag_base as tag

url = "http://10.187.132.213/api/2.0/channels/config/.json"
ip = '10.187.132.213'

base_url = "http://{ip}/api/2.0/".format(ip=ip)
get_channel_path = "channels/config/.json"
edit_channel_path = "channels/config/{id}/.json"

unMonitor_path = "channels/command/unMonitor/{id}/.json"

tag_resp = tag.tag_call(base_url + get_channel_path)

monitored = 1

def change_status(stat):
    if "TX7" in title:
        if monitored == status:
            not_monitored = 0
            return not_monitored

for source in tag_resp:
	source_ch = source["ChannelSource"]
	title = source_ch["title"]
	status = source_ch["is_monitored"]
	if "TX7" in title:
         if status == monitored:
            source_ch['is_monitored'] = change_status(source_ch["is_monitored"])
            if source_ch["is_monitored"] == 0:
                print(source_ch["title"])
                print(source_ch["id"])
                print(source_ch["is_monitored"],"\n")
                id = source_ch["id"]

                put_url = base_url + unMonitor_path.format(id=id)
                tag.tag_call(put_url, "PUT", json.dumps(source))
                