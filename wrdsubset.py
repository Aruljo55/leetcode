from collections import Counter

def word_subsets(words1, words2):
    def merge_counters(words):
        combined_counter = Counter()
        for word in words:
            combined_counter |= Counter(word)
        return combined_counter

    required_count = merge_counters(words2)
    result = []

    for word in words1:
        word_count = Counter(word)
        if all(word_count[char] >= count for char, count in required_count.items()):
            result.append(word)

    return result

# Example usage
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
output = word_subsets(words1, words2)
print(output)
