import unittest
from node_registry import NodeRegistry


class TestNodeRegistry(unittest.TestCase):

    def testSameInstance(self):
        instance1 = NodeRegistry.instance()
        instance2 = NodeRegistry.instance()
        # print("instance1: %s instance2: %s" % (instance1, instance2))
        self.assertEqual(instance1, instance2)

    def testUpdateFromScratch(self):
        instance = NodeRegistry.instance()
        instance.update_list(['a', 'b', 'c'])
        self.assertListEqual(['a', 'b', 'c'], instance.get_list())

    def testUpdateWithAlreadyValuesSet(self):
        instance = NodeRegistry.instance()
        instance.update_list(['a', 'b', 'c'])
        instance.update_list([1, 2, 3, 4])
        self.assertListEqual([1, 2, 3, 4], instance.get_list())


if __name__ == '__main__':
    unittest.main()
