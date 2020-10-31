import json
data = '''{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__.",
             },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver",
         },'''

info = json.loads(data)
#print(info)
print('Name:', info["users"][0]["name"])
#print('Hide:', info["email"]["hide"])
