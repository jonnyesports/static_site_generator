import unittest

from htmlnode import *
from textnode import *

class TestTextToHTML(unittest.TestCase):
    def test_normal(self):
        test = TextNode("This is normal text.", TextType.TEXT)
        html_node = text_node_to_html_node(test)
        output = html_node.to_html()
        expected_output = "This is normal text."
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"
    
    def test_bold(self):
        test = TextNode("This is bold text.", TextType.BOLD)
        html_node = text_node_to_html_node(test)
        output = html_node.to_html()
        expected_output = "<b>This is bold text.</b>"
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_italic(self):
        test = TextNode("This is italic text.", TextType.ITALIC)
        html_node = text_node_to_html_node(test)
        output = html_node.to_html()
        expected_output = "<i>This is italic text.</i>"
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_link(self):
        test = TextNode("Link to reTouchmedia.com", TextType.LINK, "https://retouchmedia.com")
        html_node = text_node_to_html_node(test)
        output = html_node.to_html()
        expected_output = '<a href="https://retouchmedia.com">Link to reTouchmedia.com</a>'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_image(self):
        test = TextNode("Jonny Parked Logo", TextType.IMG, "https://retouchmedia.com/jonny-parked.png")
        html_node = text_node_to_html_node(test)
        output = html_node.to_html()
        expected_output = '<img src="https://retouchmedia.com/jonny-parked.png" alt="Jonny Parked Logo"></img>'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"