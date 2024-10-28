import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Link to reTouch Media", TextType.BOLD, "https://retouchmedia.com")
        node2 = TextNode("Link to reTouchmedia", TextType.BOLD, "https://retouchmedia.com")
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("The text is the same", TextType.BOLD, "https://youtube.com")
        node2 = TextNode("The text is the same", TextType.ITALIC, "https://youtube.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()