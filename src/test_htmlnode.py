import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {"href": "https://www.example.com", "target": "_blank"}
        node = HTMLNode(props=props)
        output = node.props_to_html()
        expected_output = ' href="https://www.example.com" target="_blank"'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_eq2(self):
        props = {"href": "https://www.retouchmedia.com", "target": "_blank"}
        node = HTMLNode(props=props)
        output = node.props_to_html()
        expected_output = ' href="https://www.retouchmedia.com" target="_blank"'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_eq3(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        output = node.props_to_html()
        expected_output = ' href="https://www.google.com" target="_blank"'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"