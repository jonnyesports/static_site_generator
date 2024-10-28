import unittest
from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        tag = "p"
        children = [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")]
        props = None
        node = ParentNode(tag = tag, children = children, props = props)
        output = node.to_html()
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_no_tag(self):
        children = [LeafNode("b", "text")]
        node = ParentNode(None, children)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_nested_parents(self):
        inner_parent = ParentNode("div", [
            LeafNode("b", "Bold text")
        ])
        outer_parent = ParentNode("p", [
            inner_parent,
            LeafNode("i", "italic")
        ])
        output = outer_parent.to_html()
        expected = "<p><div><b>Bold text</b></div><i>italic</i></p>"
        self.assertEqual(output, expected)

    def test_with_props(self):
        node = ParentNode("div", [
            LeafNode("p", "text")
        ], props={"class": "main"})
        output = node.to_html()
        expected_output = '<div class="main"><p>text</p></div>'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    def test_nested_parents2(self):
        parent = ParentNode("div", [ParentNode("p", [LeafNode("span", "Hello")], {"class": "text"})], {"id": "container"})
        output = parent.to_html()
        expected_output = '<div id="container"><p class="text"><span>Hello</span></p></div>'
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"



    