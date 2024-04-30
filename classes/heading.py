class Heading:
    def __init__(self, data):
        self.data = data
        self.text = data.get('text','NA')
        self.type = data.get('type', '2')

    def get_style(self) -> str:
        return f"style=''"
    
    def generate_html(self) -> str:
        return f"<h{self.type} {self.get_style()}>{self.text}</h{self.type}>"
