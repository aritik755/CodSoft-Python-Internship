import random
import string

print("🔐 Welcome to the Password Generator!")
print("-" * 40)

length = int(input("👉 Enter desired password length: "))

print("\nSelect complexity level:")
print("1. Only letters (easy to remember)")
print("2. Letters + numbers (medium)")
print("3. Letters + numbers + symbols (strongest)")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    characters = string.ascii_letters
elif choice == '2':
    characters = string.ascii_letters + string.digits
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("⚠ Invalid choice! Defaulting to strongest password.")
    characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\n✅ Your generated password is:", password)
print("💡 Tip: Save it somewhere safe!")
