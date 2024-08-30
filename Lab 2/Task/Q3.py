def convert_url(url):
    if url.startswith("http://www."):
        return url.replace("http://www.", "")+ ".com"
    else:
        return "Invalid URL format. Make sure it starts with 'http://www.'."

user_url = input("Enter your URL starting with 'http://www.': ")
converted_url = convert_url(user_url)
print(f"Converted URL: {converted_url}")
