class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise TypeError("Name must be of type str")
        if len(name) ==0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles=[]


    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article['magazine']for article in self._articles))

    def add_article(self, magazine, title):
        self._articles.append({'magazine':magazine,'title':title})

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass