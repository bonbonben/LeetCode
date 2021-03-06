# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.

# We will call these two varieties of logs letter-logs and digit-logs. Each log has at least one word after its identifier.
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
# The digit-logs should be put in their original order.
# Return the final order of the logs.

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split(' ')[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        #print(letter_logs)
        #print(digit_logs)
        return sorted(letter_logs, key=lambda x: str(x.split(' ')[1:]) + str(x.split(' ')[0])) + digit_logs
