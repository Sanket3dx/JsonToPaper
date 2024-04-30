import json
from generate import GeneratePDF
from file_handler import FileHandler


def generate_pdf_from_json(json_file):
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    file_path = "test.pdf"
    PDF = GeneratePDF(json_data,NAME=file_path)
    pdf_data = PDF.generate_and_save_pdf()
    base_url = "http://localhost:8080"
    file_handler = FileHandler(base_url)
    upload_response = file_handler.upload_file(pdf_data, f"/pdf/client/{file_path}")
    print("Upload status:", upload_response.status_code)
    print(f"/pdf/client/{file_path}")
    


if __name__ == "__main__":
    generate_pdf_from_json("test.json")
