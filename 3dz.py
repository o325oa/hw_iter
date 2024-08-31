class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = [(list_of_list, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, index = self.stack[-1]
            if index < len(current_list):
                item = current_list[index]
                self.stack[-1] = (current_list, index + 1)
                if isinstance(item, list):
                    self.stack.append((item, 0))
                else:
                    return item
            else:
                self.stack.pop()
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()