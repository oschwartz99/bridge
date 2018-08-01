import csv
import requests

def create():

    name = "ac"
    practiceurl = "ac"
        
    url = "https://lincoln.bridgeapp.com/api/admin/sub_accounts"
    api_token = "Basic MjAzNmFmMjAtNDU1My00NTFkLTg3ZjAtMmUxOTA4NTU4YTMxOmRjMzUzYzQ1LWVmNTAtNGRjZC05Y2U2LTcxMGY0YWIzZjkzNw=="
    headers = {
        "authorization": api_token,
        'Content-Type': 'application/json', 
        'Accept':'application/json'
    }
    payload = {
        'sub_account' : {
            "name":name,
            "subdomain":practiceurl
        }
    }
    r = requests.post(url=url, headers=headers, json=payload)
    print(r)
        
if __name__ == "__main__":
    create()