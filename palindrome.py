def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not a palindrome")
