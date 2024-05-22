class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        if self.props is None:
            return ""
        return_list = "" 
        if self.props != None:
            for key, value in self.props.items():
                return_list += f' {key} ="{value}"'
            return return_list
        return self.props

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        return False


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag == None:
            return str(self.value)
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent must have Tag")
        if self.children == None:
            raise ValueError("Parent must have Children")
        returned_html = ''
        for child in self.children:
            returned_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{returned_html}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
