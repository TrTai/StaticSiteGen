from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"
            
def text_to_html_Node(text_node):
    if isinstance(text_node, TextNode) != True:
        raise ValueError("Object must be TextNode")
    #expected_text_types = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type == "text":
        new_html_node = LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        new_html_node = LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        new_html_node = LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        new_html_node = LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        new_html_node = LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == "image":
        new_html_node = LeafNode("img", None, {"src":text_node.url , "alt" : text_node.text})
    else:
        raise ValueError(f"Invalid Text Type {text_node.text_type}")
    return new_html_node


