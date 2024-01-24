# Create a class with the name "Comment". The __init__ method should accept 3 parameters:
# •	username
# •	content
# •	likes (optional, 0 by default)
# Use the exact names for your variables
# Note: there is no input/output for this problem. Test the class yourself and submit only the class

class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

    pass


# comment = Comment("user1", "I like this book")
# comment1 = Comment("user2", "I like all books", 10)
# print(comment1.username)
# print(comment1.content)
# print(comment1.likes)

