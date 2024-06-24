class MyQueue:
    def __init__(self, capacity):
        self.queue = []  # Sử dụng list để lưu trữ các phần tử
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0  # Kiểm tra xem queue có rỗng không

    def is_full(self):
        # Kiểm tra xem queue đã đầy chưa
        return len(self.queue) == self.capacity

    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)  # Thêm phần tử vào cuối queue
        else:
            print("Queue is full. Cannot enqueue.")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Lấy và loại bỏ phần tử đầu tiên
        else:
            print("Queue is empty. Cannot dequeue.")

    def front(self):
        if not self.is_empty():
            return self.queue[0]  # Trả về phần tử đầu tiên mà không loại bỏ
        else:
            print("Queue is empty. No front element.")


# Ví dụ sử dụng (giống trong hình)
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())  # False
print(queue1.front())  # 1
print(queue1.dequeue())  # 1
print(queue1.front())  # 2
print(queue1.dequeue())  # 2
print(queue1.is_empty())  # True
