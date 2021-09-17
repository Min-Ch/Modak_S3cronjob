import re

class DBDao:
    def __init__(self, db):
        self.db = db

class UserDao(DBDao):
    def user_images(self):
        connection = self.db.connect()
        return [image[0] for image in connection.execute("SELECT image FROM users") if image[0]]

class PostingDao(DBDao):
    def posting_images(self):
        connection = self.db.connect()
        image_list = []
        for content in connection.execute("SELECT content FROM postings"):
            imagelist = re.findall('!\[\]\((.+?)\)', content[0])
            if imagelist:
                image_list += imagelist
        return image_list


