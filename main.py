import json
from generate import GeneratePDF
from file_handler import FileHandler
from redis_op import RedisOperations

from typing import List, Optional
from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI
import base64


class PDFRequest(BaseModel):
    theme: str
    pdf_type: str
    header: List[dict]
    body: List[dict]
    footer: List[dict]


app = FastAPI()

@app.post("/generate_pdf/")
async def generate_pdf(request_data: PDFRequest):
    request_dict = request_data.dict()
    file_path = "output.pdf"
    PDF = GeneratePDF(request_dict,NAME=file_path)
    pdf_data = PDF.generate_and_save_pdf()
    pdf_data_base64 = base64.b64encode(pdf_data).decode('utf-8')
    base_url = "http://localhost:8080"
    file_handler = FileHandler(base_url)
    upload_response = file_handler.upload_file(pdf_data, f"/pdf/client/{file_path}")
    print("Upload status:", upload_response.status_code)
    print(f"/pdf/client/{file_path}")
    return {
        "pdf_path" : f"/pdf/client/{file_path}",
        "pdf_base64" : pdf_data_base64
        }



def generate_pdf_from_json(json_file):
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    
    file_path = "output.pdf"
    PDF = GeneratePDF(json_data,NAME=file_path)
    pdf_data = PDF.generate_and_save_pdf()
    base_url = "http://localhost:8080"
    file_handler = FileHandler(base_url)
    upload_response = file_handler.upload_file(pdf_data, f"/pdf/client/{file_path}")
    print("Upload status:", upload_response.status_code)
    print(f"/pdf/client/{file_path}")
    
    # redis = RedisOperations()
    # requests_to_process = redis.get_pdf_req_to_process()
    # for req in requests_to_process:
    #     json_data = req.get('req_data',[])
    #     req_no = req.get('req_no','')
    #     file_path = req_no + "_output.pdf"
    #     PDF = GeneratePDF(json_data,NAME=file_path)
    #     pdf_data = PDF.generate_and_save_pdf()
    #     base_url = "http://localhost:8080"
    #     file_handler = FileHandler(base_url)
    #     upload_response = file_handler.upload_file(pdf_data, f"/pdf/client/{file_path}")
    #     if upload_response.status_code == 201 :
    #         print(req.get('index',''))
    #         redis.delete_element_by_index(req.get('index',''))
    #     print("Upload status:", upload_response.status_code)
    #     print(f"/pdf/client/{file_path}")
   
    


if __name__ == "__main__":
    generate_pdf_from_json("test.json")
