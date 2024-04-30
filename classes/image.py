class Image:
    def __init__(self, data):
        self.data = data
        self.source = self.get_source()
    
    def get_source(self) -> str:
        source = ""
        if "bas64" in self.data and self.data['bas64'] != "":
            source =  f"data:image/png;base64,{self.data['bas64']}"
        elif "url" in self.data and self.data['url'] != "":
            source =  self.data['url']
        return source

    def get_style(self) -> str:
        return f"style='height: {self.data['size']['height']}; width: {self.data['size']['width']};'"
    
    def generate_html(self) -> str:
        html_content = f"<img src={self.source} {self.get_style()}>"
        return html_content
