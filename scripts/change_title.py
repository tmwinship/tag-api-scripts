import requests
import json
import tag_base as tag
url = "http://10.187.132.213/api/2.0/channels/config/.json"
ip = '10.187.132.213'

base_url = "http://{ip}/api/2.0/".format(ip=ip)
get_channel_path = "channels/config/.json"
edit_channel_path = "channels/config/{id}/.json"

tag_resp = tag.tag_call(base_url + get_channel_path) #grabs sources

def change_title(ts):
	ts1 = title
	replace = '7'
	for replace in ts:
		if " | TS" in ts and "Deportes" not in ts:
			for item in ts:
				index = 2
				replaced_title = ts1[0:index] + "0" + ts1[index+1: ]
				return replaced_title

for source in tag_resp:
	source_ch = source["ChannelSource"]
	title = source_ch["title"]
	
	if " | TS" in title:
		source_ch["title"] = change_title(source_ch["title"])
		print(source_ch["title"])
		print(source_ch["id"])
		id = source_ch["id"]
		put_url = base_url + edit_channel_path.format(id=id)
		tag.tag_call(put_url, "PUT", json.dumps(source))
		
	
