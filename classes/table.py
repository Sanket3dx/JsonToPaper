class Table:
    def __init__(self, data):
        self.data = data

    def create_head(self, head) -> str:
        head_html = "<thead>"
        for row in head:
            head_html += "<tr>"
            for item in row:
                head_html += f"<th>{item}</th>"
            head_html += "</tr>"
        head_html += "</thead>"
        return head_html

    def create_body(self, body) -> str:
        body_html = "<tbody>"
        for row in body:
            body_html += "<tr>"
            for col in row:
                body_html += f"<td>{col}</td>"
            body_html += "</tr>"
        body_html += "</tbody>"
        return body_html

    def create_foot(self, foot) -> str:
        if foot:
            foot_html = "<tfoot><tr>"
            for item in foot:
                foot_html += f"<td>{item}</td>"
            foot_html += "</tr></tfoot>"
            return foot_html
        else:
            return "<tfoot></tfoot>"

    def generate_html(self) -> str:
        html_content = "<table>"
        if "head" in self.data:
            html_content += self.create_head(self.data["head"])
        if "body" in self.data:
            html_content += self.create_body(self.data["body"])
        if "foot" in self.data:
            html_content += self.create_foot(self.data["foot"])
        html_content += "</table>"
        return html_content
