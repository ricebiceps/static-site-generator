class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,remote):
        return (self.text == remote.text) and (self.text_type == remote.text_type) and (self.url == remote.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"