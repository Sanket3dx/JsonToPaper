from weasyprint import HTML
from classes.table import Table
from classes.image import Image
from classes.heading import Heading

class GeneratePDF:
    def __init__(self, data, NAME="output.pdf") -> None:
        self.pdf_name = NAME
        self.data = data
        self.style = self.get_pdf_style(data['theme'],data.get('pdf_type', 'A4'))
    
    def header(self) -> str:
        head_data = self.data.get("header", [])
        head = f"<html><head>{self.style}"
        
        for item in head_data:
            head = head + self.generate_html_for_item(item)
        
        head = head + f"</head>"
        return head
    
    def body(self) -> str:
        body_data = self.data.get("body", [])
        body = f"<body>"
        
        for item in body_data:
            body = body + self.generate_html_for_item(item)
        
        body = body + f"</body>"
        return body
    
    def footer(self) -> str:
        footer_data = self.data.get("footer", [])
        footer = f"<footer>"
        
        for item in footer_data:
            footer = footer + self.generate_html_for_item(item)
        
        footer = footer + f"</footer>"
        return footer
    
    def get_pdf_style(self, theme, pdf_type) -> str:
        pdf_sizes = {
            'A3': '297mm 420mm',
            'A2': '420mm 594mm',
            'A1': '594mm 841mm',
            'A0': '841mm 1189mm',
            'Letter': '8.5in 11in',
            'Legal': '8.5in 14in',
            'Tabloid': '11in 17in',
        }

        
        pdf_size = pdf_sizes.get(pdf_type, 'auto')
        
        pdf_theme = f"""
            <style>
                @page {{
                    size: {pdf_size};
                    margin: 2px;
                    padding: 2px;
                }}
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                head {{
                    margin: 0;
                    padding: 0;
                }}
                h1 {{
                    color: blue;
                    text-decoration: underline;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        """
        return pdf_theme

        
    def generate_html_for_item(self,item) -> str:
        type = item['type']
        data = item['data']
        item_html = ""
        if type == "table":
            item_html = Table(data).generate_html()
        elif type == "image":
            item_html = Image(data).generate_html()
        elif type == "heading":
            item_html = Heading(data).generate_html()
        else:
            item_html = ""
        return item_html
        
    def generate_html(self) -> str:
        html_content = ""
        html_content = html_content + self.header() + self.body() + self.footer()
        return html_content
    
    def generate_and_save_pdf(self) -> bytes:
        html_content = self.generate_html()
        #HTML(string=html_content).write_pdf(self.pdf_name)
        pdf_data = HTML(string=html_content).write_pdf()
        return pdf_data