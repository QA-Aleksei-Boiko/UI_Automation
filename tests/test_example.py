import requests
from configuration import My_url

def test_geting_data1():
    response = requests.get(My_url)

    assert response.status_code == 200, 'Recived status code is not equal to expected.'



    print(response.status_code)

