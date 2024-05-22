import unittest  

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_empty_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_repr_eq(self):
        node = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), node2.__repr__())
    
    def test_repr_value_neq(self):
        node = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = HTMLNode(tag = "p", value = "Some different Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertNotEqual(node.__repr__(), node2.__repr__())

    def test_repr_tag_neq(self):
        node = HTMLNode(tag = "h1", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertNotEqual(node.__repr__(), node2.__repr__())
    

    def test_props_func(self):
        node = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual(" href =\"https://google.com\" target =\"_blank\"", node.props_to_html())

    def test_props_to_html_eq(self):
        node = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
   
    def test_props_to_html_neq(self):
        node = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = HTMLNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_fill"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_Leaf_eq_p(self):
        node = LeafNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = LeafNode(tag = "p", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_Leaf_eq_link(self):
        node = LeafNode(tag = "a", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        node2 = LeafNode(tag = "a", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_Leaf_link_to_html(self):
        node = LeafNode(tag = "a", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual("<a href =\"https://google.com\" target =\"_blank\">Some Text here</a>", node.to_html())

    def test_bad_Leaf2(self):
        node = LeafNode(tag = "a", value = None, props={"href":"https://google.com", "target": "_blank"})
        self.assertRaises(ValueError, node.to_html)

    def test_Leaf_p_to_html(self):
        node = LeafNode(tag = "p", value = "Some Text here")
        self.assertEqual("<p>Some Text here</p>", node.to_html())

    def test_Leaf_repr(self):
        node = LeafNode(tag = "a", value = "Some Text here", props={"href":"https://google.com", "target": "_blank"})
        self.assertEqual("LeafNode(a, Some Text here, {\'href\': \'https://google.com\', \'target\': \'_blank\'})", node.__repr__())

    def test_bad_Parent(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here")]
        parent = ParentNode(None, test_child, None)
        self.assertRaises(ValueError, parent.to_html)

    def test_bad_Parent2(self):
        parent = ParentNode("p", None, None)
        self.assertRaises(ValueError, parent.to_html)

    def test_2parents_2kids(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here"), LeafNode(tag = "i", value = "Some italics here")]
        parent = ParentNode("p", test_child, None)
        parent2 = ParentNode("p", test_child, None)
        self.assertEqual(parent,parent2)

    def test_2parents_2kids_tohtml(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here"), LeafNode(tag = "i", value = "Some italics here")]
        parent = ParentNode("p", test_child, None)
        parent2 = ParentNode("p", test_child, None)
        self.assertEqual(parent.to_html(),parent2.to_html())

    def test_1parents_2kids_tohtml_check(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here"), LeafNode(tag = "i", value = "Some italics here")]
        parent = ParentNode("p", test_child, None)
        self.assertEqual(parent.to_html(), "<p><b>Some Text here</b><i>Some italics here</i></p>")

    def test_1parents_3kids_tohtml_check(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here"), LeafNode(tag = "i", value = "Some italics here"), LeafNode(value = "Some plain text")]
        parent = ParentNode("p", test_child, None)
        self.assertEqual(parent.to_html(), "<p><b>Some Text here</b><i>Some italics here</i>Some plain text</p>")


    def test_1parents_3kids_andalink_tohtml_check(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here"), LeafNode(tag = "i", value = "Some italics here"), LeafNode(value = "Some plain text"), LeafNode(tag = "a", value = "A cool link!", props = {"href":"https://google.com", "target": "_blank"})]
        parent = ParentNode("p", test_child, None)
        self.assertEqual(parent.to_html(), "<p><b>Some Text here</b><i>Some italics here</i>Some plain text<a href =\"https://google.com\" target =\"_blank\">A cool link!</a></p>")

    def test_parent_grandparent_kids_and_alink(self):
        test_child = [LeafNode(tag = "b", value = "Some Text here"), LeafNode(tag = "i", value = "Some italics here"), LeafNode(value = "Some plain text"), LeafNode(tag = "a", value = "A cool link!", props = {"href":"https://google.com", "target": "_blank"})]
        parent = ParentNode("p", test_child, None)
        nested_parent = [parent]
        parent2 = ParentNode("h1", nested_parent, None)
        self.assertEqual(parent2.to_html(), "<h1><p><b>Some Text here</b><i>Some italics here</i>Some plain text<a href =\"https://google.com\" target =\"_blank\">A cool link!</a></p></h1>")














































































































































































































































































































































































if __name__ == "__main__":
    unittest.main()
