from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def ya_disk_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth ' + self.token}

    def get_upload_link(self, ya_disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.ya_disk_headers()
        params = {"path": ya_disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        link = response.json
        return link().get('href', '')

    def upload(self, file_path: str):
        href = self.get_upload_link(upload_path)
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':

    file_path = 'some_file.txt'
    upload_path = ('test/some_file.txt')
    token = '&&&&&?????$$$$$'
    uploader = YaUploader(token)
    result = uploader.upload(file_path)
