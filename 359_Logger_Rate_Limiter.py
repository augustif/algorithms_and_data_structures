# LeetCode: https://leetcode.com/problems/logger-rate-limiter/

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

from collections import deque


class LoggerC:

    # time complexity O(1)
    # space complexity O(n): n is the number of unique messages  (worst case scenario)
    def __init__(self):
        self.messages_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages_timestamps:  # tc O(1)
            self.messages_timestamps[message] = timestamp  # tc O(1)
            return True
        else:
            old_timestamp = self.messages_timestamps[message]  # tc O(1)
            if (timestamp - old_timestamp) < 10:  # tc O(1)
                return False
            self.messages_timestamps[message] = timestamp  # tc O(1)
            return True


class LoggerB:
    # time complexity O(1)
    # space complexity O(n): n is the number of unique messages (worst case scenario)
    def __init__(self):
        self.messages_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages_timestamps:  # tc O(1)
            pass
        else:
            old_timestamp = self.messages_timestamps[message]  # tc O(1)
            if (timestamp - old_timestamp) < 10:  # tc O(1)
                return False
        self.messages_timestamps[message] = timestamp  # tc O(1)
        return True


"""The main difference between this approach with hashtable and the previous approach with queue is
 that in previous approach we do proactive cleaning, i.e. at each invocation of function, we first 
 remove those expired messages.

While in this approach, we keep all the messages even when they are expired. This characteristics 
might become problematic, since the usage of memory would keep on growing over the time. 
Sometimes it might be more desirable to have the garbage collection property of the previous approach."""


class LoggerA1(object):
    """ only works when timestamps in input test case are not decreasing, taken from leetcode and substituted set with list"""
    # time complexity O(N): N is the size of the queue.
    # space complexity O(N): N is the size of the queue.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_list = list()
        self._msg_queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_list.pop(0)
            else:
                break

        if message not in self._msg_list:
            self._msg_list.append(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False


class LoggerA0(object):
    """ only works when timestamps in inupt test case are not decreasing, taken from leetcode"""
    # time complexity O(N): N is the size of the queue.
    # space complexity O(N): N is the size of the queue.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        while self._msg_queue:  # tc O(N) where N is the number of iterations todiscard obsolete messages
            msg, ts = self._msg_queue[0]  # tc O(1)
            if timestamp - ts >= 10:  # tc O(1)
                self._msg_queue.popleft()  # tc O(1)
                self._msg_set.remove(msg)  # tc O(1)
            else:
                break

        if message not in self._msg_set:  # tc O(1)
            self._msg_set.add(message)  # tc O(1)
            self._msg_queue.append((message, timestamp))  # tc O(1)
            return True
        else:
            return False


"""As one can see, the usage of set data structure is not absolutely necessary. One could simply iterate the message queue to check if there is any duplicate.

Another important note is that if the messages are not chronologically ordered then we would have to iterate through the entire queue to remove the expired messages, 
rather than having early stopping. Or one could use some sorted queue such as Priority Queue to keep the messages.

Complexity Analysis

Time Complexity: O(N) where N is the size of the queue. In the worst case, all the messages in the queue become obsolete. As a result, we need clean them up.
Space Complexity: O(N) where N is the size of the queue. We keep the incoming messages in both the queue and set. The upper bound of the required space would be 2N, if we have no duplicate at all.
"""