class Solution:
    def readBinaryWatch(self, turnedOn):
        result = []

        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append(str(hour) + ":" + format(minute, "02d"))

        return result
