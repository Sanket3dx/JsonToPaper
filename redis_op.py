import redis
import json

class RedisOperations:
    def __init__(self) -> None:
        self.Conn = redis.Redis(
            host='',
            port=18004,
            password='')
        self.pdf_queue = "pdf_process_queue"
    
    def get_pdf_req_to_process(self):
        elements = self.Conn.lrange(self.pdf_queue, 0, 9)
        elements_to_process = []
        index = 0
        for element in elements:
            try:
                json_string = element.decode().replace('\n', '').replace('    ', '')
                element_dict = json.loads(json_string)
                element_dict["index"] = index
                elements_to_process.append(element_dict)
                index += 1 
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON element at index {index}: {e}")
                continue
        return elements_to_process

    def delete_element_by_index(self, index):
        self.Conn.lset(self.pdf_queue, index, "__deleted__")
        self.Conn.lrem(self.pdf_queue, 1, "__deleted__")