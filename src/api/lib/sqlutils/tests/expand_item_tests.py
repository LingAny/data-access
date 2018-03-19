import unittest
from sqlutils import ExpandItem


class ExpandItemTestCase(unittest.TestCase):

    def test_expand_item_created(self):
        sut = ExpandItem.load('expand')
        self.assertEqual(sut.name, 'expand')

    def test_expand_children(self):
        sut = ExpandItem.load('parent.first.second')
        self.assertEqual(sut.name, 'parent')
        self.assertEqual(sut.child.name, 'first')
        self.assertEqual(sut.child.child.name, 'second')

    def test_expand_str_representation(self):
        sut = ExpandItem.load('parent.first.second')
        self.assertEqual(str(sut), 'parent.first.second')
