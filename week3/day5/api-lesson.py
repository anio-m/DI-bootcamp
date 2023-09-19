import requests

def retrive_data ():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    print(response.json())
    data = response.json()
    print(f"the {data['iss_position']}")
retrive_data()  


