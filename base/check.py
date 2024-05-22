import requests

url = "http://127.0.0.1:8000/advocate/"

headers = {
	"X": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwODg2MTk5LCJpYXQiOjE3MDA4ODU4OTksImp0aSI6ImYyMzU1MjM4ODk1NTRkZWRiZmZkMzg4NjA4MWZmYmJiIiwidXNlcl9pZCI6NH0.O5t_0FPuagAebK_3e10VwdbLze2G0tnl4exdJgwr_nU"
}
response = requests.get(url, headers=headers)
print(response.json())