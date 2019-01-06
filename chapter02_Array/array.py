# -*- coding: utf-8 -*-
# @Author  : echelon
# @Time    : 2018/12/31 19:42


class Array:

    def __init__(self, capacity=10):
        # 单下划线只能类及其子类访问
        # 双下划线只能本类访问
        self._data = [None] * capacity
        self._size = 0

    # 获取数组中的元素个数
    def get_size(self):
        return self._size

    # 获取数组的容量
    def get_capacity(self):
        return len(self._data)

    # 返回数组是否为空
    def is_empty(self):
        return self._size == 0

    # 插入一个新元素
    def add(self, index, ele):
        # 判断索引边界
        if not (self._size >= index >= 0):
            raise ValueError('index is incorrect!')
        # 容量已满，需要扩容
        if self._size == len(self._data):
            if len(self._data) == 0:
                self._resize(1)
            else:
                self._resize(2 * len(self._data))
        # 将插入索引位置的元素及其之后的元素向后移一位
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        # 在指定索引位置赋值
        self._data[index] = ele
        # 元素个数加1
        self._size += 1

    # 往最后面加元素
    def add_last(self, ele):
        self.add(self._size, ele)

    # 动态扩容
    def _resize(self, capacity):
        new_data = [None] * capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    # 查询元素
    def get(self, index):
        if not (0 <= index <= self._size):
            raise ValueError("index is out of range!")
        return self._data[index]

    # 查询首元素
    def get_first(self):
        return self.get(0)

    # 查询最后一个元素
    def get_last(self):
        return self.get(self._size - 1)

    # 删除指定索引的元素
    def remove(self, index):
        if not (0 <= index <= self._size):
            raise ValueError("index is out of range!")
        tmp = self._data[index]
        # 将当前索引及其之后的值向前移一位
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        # 动态缩容
        if self._size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self._resize(len(self._data) // 2)
        return tmp

    # 删除首元素
    def remove_first(self):
        return self.remove(0)

    # 修改指定索引位置的元素值
    def set(self, index, e):
        if not 0 <= index <= self._size:
            raise ValueError("index is out of range!")
        self._data[index] = e

    # 查询指定元素所在的第一个索引
    def find_index(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    # 删除指定元素
    def remove_element(self, e):
        index = self.find_index(e)
        return self.remove(index)

    # 重写打印方法
    def __str__(self):
        return str('arr:{}, size:{}, capacity:{}'.format(self._data[:self._size], self._size, self.get_capacity()))


if __name__ == '__main__':
    arr = Array(capacity=30)
    for i in range(10):
        arr.add_last(i)
    print(arr)

    # 删除
    arr.remove_first()
    arr.remove_first()
    arr.remove_first()

    print(arr)
