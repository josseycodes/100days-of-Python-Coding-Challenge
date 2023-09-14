import re

# Sample text
text = "This is a sample text with some email addresses: john@example.com and alice@gmail.com. Please contact support@company.com for assistance."

# 1. Search for email addresses in the text
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emails = re.findall(email_pattern, text)
print("Email Addresses Found:")
for email in emails:
    print(email)

# 2. Replace email addresses with "[EMAIL]"
masked_text = re.sub(email_pattern, "[EMAIL]", text)
print("\nMasked Text:")
print(masked_text)

# 3. Extract domain names from email addresses
domains = re.findall(r'@([A-Za-z0-9.-]+)', text)
print("\nDomains Found:")
for domain in domains:
    print(domain)

# 4. Check if a string starts with "This"
if re.match(r'^This', text):
    print("\nThe text starts with 'This'")
else:
    print("\nThe text does not start with 'This'")

# 5. Check if "contact" is in the text
if re.search(r'contact', text):
    print("The word 'contact' is found in the text.")
else:
    print("The word 'contact' is not found in the text.")

