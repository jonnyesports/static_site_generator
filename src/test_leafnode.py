import unittest
from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        tag = "p"
        value = "This is a paragraph of text."
        node = LeafNode(tag = tag, value = value)
        output = node.to_html()
        expected_output = "<p>This is a paragraph of text.</p>"
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"
    
    def test_eq2(self):
        tag = "a"
        value = "This is a paragraph of text."
        props = {"href": "https://www.google.com"}
        node = LeafNode(tag = tag, value = value, props = props)
        output = node.to_html()
        expected_output = '<a href="https://www.google.com">This is a paragraph of text.</a>'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_eq3(self):
        tag = "a"
        value = "Click me!"
        props = {"href": "https://www.google.com"}
        node = LeafNode(tag = tag, value = value, props = props)
        output = node.to_html()
        expected_output = '<a href="https://www.google.com">Click me!</a>'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"
