import unittest

from htmlnode import HTMLNode
from textnode import TextNode
from textnode import text_to_html_Node

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

    def test_neq(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a different text node", "bold", "www.boot.dev")
        self.assertNotEqual(node,node2) 

    def test_repr_eq(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node.__repr__(),node2.__repr__())

    def test_repr_neq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node.__repr__(),node2.__repr__())

    def test_eq_func(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertTrue(node.__eq__(node2))

    def test_eq_func_neq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertFalse(node.__eq__(node2))

    def test_eq_func_neqURL(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertFalse(node.__eq__(node2))

    def test_html_convert(self):
        testText1 = TextNode("This is a bolded text", "bold")
        testHtml = HTMLNode("b", "This is a bolded text")
        self.assertEqual(text_to_html_Node(testText1), testHtml)

if __name__ == "__main__":
    unittest.main()
