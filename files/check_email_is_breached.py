import requests
import os 


api_key = os.environ.get("EMAIL_VALIDATION")
def whether_email_is_breached(emails):
    for i in emails:
        url = 'https://leak-lookup.com/api/search'

        # Payload data
        payload = {
            'key': api_key,
            'type': 'email_address',
            'query': i
        }

        # Make the POST request
        response = requests.post(url, data=payload)

        # Check the status code
        if response.status_code == 200:
            res=response.json()
            if not res["message"]:
                print("no breach found")
                return None
            else:
                breach_sites=[]
                print("breach found")
                for site_name in res["message"]:
                    print(site_name)
                    breach_sites.append(site_name)
                    return breach_sites

        else:
            print(f"Error: {response.status_code} - {response.text}")

# whether_email_is_breached(['nithinnmanickam@hotmail.com','nithinnmanickam@gmail.com'])