import requests

class FileHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload_file(self, pdf_data, file_path):
        url = f"{self.base_url}/file"
        headers = {
            "x-full-file-path": file_path,
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(url, headers=headers, data=pdf_data)
        return response