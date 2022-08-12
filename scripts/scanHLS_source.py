import requests
import json
import tag_base as tag


url = "http://10.187.132.213/api/2.0/channels/config/.json"
ip = '10.187.132.213'

scan_url = "http://{ip}/api/2.0/scanner_tasks/.json".format(ip=ip)
base_url = "http://{ip}/api/2.0/".format(ip=ip)
get_channel_path = "channels/config/.json"
edit_channel_path = "channels/config/{id}/.json"

base_scan_url = "http://{ip}/api/2.0/"
scan_path = "scanner_tasks/603665/.json"

tag_scan = tag.tag_call(scan_url)

new_source = input("Paste in source URL: ")
new_title = input("Enter title: ")

for scan in tag_scan:
    scan_ch = scan["ScanTask"]
    scan_entry = scan_ch["ScanEntries"]
    if scan_entry[0]["id"] == 8:

        scan_entry[0]["title"] = new_title
        scan_entry[0]["source"] = new_source
        scan_ch["progress"] = 0
        scan_ch["time_remained"] = 10
        scan_ch["mode_id"] = 1
        scan_ch["status"] = "Scanning (0 new, 1 current)"
        
        tag.tag_call(base_scan_url.format(ip=ip) + scan_path, "PUT", json.dumps(scan))
        