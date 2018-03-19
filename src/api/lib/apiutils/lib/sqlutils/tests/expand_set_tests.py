import unittest

from sqlutils import ExpandSet, ExpandItem


class ExpandSetTests(unittest.TestCase):

    def test_expand_set_created(self):
        sut = ExpandSet.load('item')
        self.assertTrue(sut.contains(ExpandItem.load('item')))

    def test_expand_set_append(self):
        sut = ExpandSet()
        sut.append(ExpandItem.load('item'))
        self.assertTrue(sut.contains(ExpandItem.load('item')))

    def test_expand_set_with_parent(self):
        sut = ExpandSet.load('item parent parent.child')
        self.assertTrue(sut.contains(ExpandItem.load('item')))
        self.assertTrue(sut.contains(ExpandItem.load('parent')))
        self.assertTrue(sut.contains(ExpandItem.load('parent.child')))

    def test_expand_set_str_representation(self):
        items = ['item', 'parent', 'parent.child']
        expand = ' '.join(sorted(items))

        sut = ExpandSet.load(expand)
        expand_repr = str(sut)
        self.assertEqual(expand_repr, expand)

    def test_parent_not_exists_on_only_child_specified(self):
        sut = ExpandSet.load('parent.first.second')
        self.assertFalse(sut.contains(ExpandItem.load('parent')))

    def test_extract_expand_set(self):
        sut = ExpandSet.load('item parent parent.child parent.child.second parent.first.third.parent')
        parent_set = sut.extract(ExpandItem.load('parent'))
        parent_set_repr = str(parent_set)
        self.assertEqual(parent_set_repr, 'child child.second first.third.parent')
