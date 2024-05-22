from textnode import TextNode

def main():
    testNode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    test2 = TextNode("This is a new text node", "bold", "https://www.boot.dev")
 
    print(testNode.__repr__())
    print(test2.__repr__())
    print(testNode.__eq__(test2))

main()
