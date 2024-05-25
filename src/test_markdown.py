import unittest  
from textnode import TextNode
from read_markdown import split_nodes_delimiter


node_ends_w_delim = [TextNode("This is a text object with some *italics*", "text")]
expected_result = [TextNode("This is a text object with some ", "text"), TextNode("italics", "italic")]
test_incomplete_italic = [TextNode("This is a text object with some *italics", "text")]
class testMarkdownFunc(unittest.TestCase):
    def test_delimiter(self):
        self.assertEqual(split_nodes_delimiter(node_ends_w_delim, '*', 'italic'), expected_result)

    def test_delimiterBad(self):
        self.assertRaises(ValueError, split_nodes_delimiter, node_ends_w_delim, '*', 'bad')


    def test_single_delimiter(self):
        self.assertRaises(ValueError, split_nodes_delimiter, test_incomplete_italic, '*', 'italic')
















if __name__ == "__main__":
    unittest.main()

