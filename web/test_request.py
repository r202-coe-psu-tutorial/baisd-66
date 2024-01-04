import requests
import random

for i in range(10):
    response = requests.post(
        "http://localhost:5000/save",
        data=dict(message=f"Hello from hacker {random.randint(1, 100)}"),
    )
    print(response)
