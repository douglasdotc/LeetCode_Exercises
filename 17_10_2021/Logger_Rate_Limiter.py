# Problem link: https://leetcode.com/problems/logger-rate-limiter/
# Tags: Google, Microsoft, Facebook, Apple

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class Logger:

    def __init__(self):
        self.stream_until = {}
        # self.stream_until.keys()
        # self.stream_until.items()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Messages are random
        # Each message valid for t + 10 secs from t
        # t always increasing
        # Use Hash map
        
        if message not in self.stream_until.keys():
            self.stream_until[message] = timestamp + 10
            return True
        else:
            if timestamp < self.stream_until[message]:
                return False
            else:
                self.stream_until[message] = timestamp + 10
                return True


# Time Complexity:
# if - else clause, looking up and updating(searching) hash map, 
# require constant time --> O(1)

# Space Complexity:
# Depends on the number of messages n --> O(n), 1 per each hash map entry
# There is no multiple values in items()