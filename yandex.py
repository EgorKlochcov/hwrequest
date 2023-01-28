import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        href = self._get_upload_link(disk_file_path=file_path).get("href", "")
        response = requests.put(href, open(file_path, 'rb'))


if __name__ == '__main__':
    path_to_file = "some\path"
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
