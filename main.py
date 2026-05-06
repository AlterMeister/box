"""
A deliberately buggy file for testing an agent's code-fixing ability.

Task for agent:
Fix the implementation bugs so that all assertions at the bottom pass.
Do not delete or weaken the assertions.
"""


def divide(a, b):
    if b == 0:
        return "Error"
    return a / b


def is_even(n):
    return n % 2 == 0


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def average(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count


def parse_int_list(csv_text):
    return [int(x.strip()) for x in csv_text.split(",") if x.strip()]


def remove_duplicates(items):
    result = []
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def merge_dicts(a, b):
    merged = a.copy()
    merged.update(b)
    return merged


def safe_get_user_name(user):
    if user is None:
        return "Unknown"
    return user.get("profile", {}).get("name", "Unknown")


def sort_numbers(numbers):
    return sorted(numbers)


def normalize_spaces(text):
    return " ".join(text.split())


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def chunk_list(items, size):
    chunks = []
    for i in range(0, len(items), size):
        chunks.append(items[i:i + size])
    return chunks


def find_max(numbers):
    if not numbers:
        raise ValueError("find_max() arg is an empty sequence")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value


def apply_discount(price, percent):
    return price * (1 - percent / 100)


def title_case_name(name):
    return name.title()


def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


# -------------------------
# Tests / expected behavior
# -------------------------

assert divide(5, 2) == 2.5
assert divide(10, 2) == 5
assert divide(6, 0) == "Error"  # Should handle division by zero

assert is_even(2) is True
assert is_even(3) is False

assert clamp(5, 1, 10) == 5
assert clamp(-1, 1, 10) == 1
assert clamp(20, 1, 10) == 10

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(7) == 13

assert average([1, 2, 3, 4]) == 2.5
assert average([]) == 0

assert reverse_words("hello world from agent") == "agent from world hello"

assert count_vowels("Hello WORLD") == 3

assert parse_int_list("1, 2, 3, 4") == [1, 2, 3, 4]
assert parse_int_list("1,,2, ,3") == [1, 2, 3]

assert remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]

original = {"a": 1}
merged = merge_dicts(original, {"b": 2})
assert merged == {"a": 1, "b": 2}
assert original == {"a": 1}

assert safe_get_user_name({"profile": {"name": "Julian"}}) == "Julian"
assert safe_get_user_name({"profile": {}}) == "Unknown"
assert safe_get_user_name({}) == "Unknown"
assert safe_get_user_name(None) == "Unknown"

assert sort_numbers([10, 2, 1, 20]) == [1, 2, 10, 20]

assert normalize_spaces("  hello    world \n from\t agent  ") == "hello world from agent"

assert is_palindrome("Race car!") is True
assert is_palindrome("hello") is False

assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert chunk_list([1, 2], 3) == [[1, 2]]

assert find_max([-10, -3, -7]) == -3
assert find_max([1, 5, 2]) == 5

assert apply_discount(100, 20) == 80
assert apply_discount(50, 10) == 45

assert title_case_name("liu julian") == "Liu Julian"

assert flatten([[1, 2], [3, 4], [], [5]]) == [1, 2, 3, 4, 5]

print("All tests passed.")