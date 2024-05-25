from textnode import TextNode


expected_text_types = ["text", "bold", "italic", "code", "link", "image"]
    #node = TextNode("this is some text with *italics*", "text")
    #new_nodes = split_nodes_delimiter([node], "*", "i")
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type not in expected_text_types:
        raise ValueError("Invalid text type")
    new_nodes = []
    for node in old_nodes:
        split_nodes = []
        if node.text_type != "text":
            split_nodes.append(node)
        else:
            str_list = node.text.split(delimiter)
            if len(str_list) % 2 == 0:
                raise ValueError("No Closing delimiter")
            for i in range(len(str_list)):
                if str_list[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(str_list[i], "text"))
                else:
                    split_nodes.append(TextNode(str_list[i].lstrip('*'), text_type))
        new_nodes.extend(split_nodes)
    return new_nodes



