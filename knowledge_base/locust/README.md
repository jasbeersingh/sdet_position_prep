following the official tutorial: http://docs.locust.io/en/stable/quickstart.html

refer to this link for dummy apis: https://dev.to/promode/7-demo-websites-which-you-can-use-to-perform-api-testing-1p6c

locust -f base_demo.py --headless --users 10 --run-time 10s --spawn-rate 1 -H https://fakerestapi.azurewebsites.net