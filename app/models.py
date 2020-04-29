class NewsSource:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id, name):
        self.id = id
        self.name = name

class NewsArticle:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,title,description,image_url, published, content):
        self.title = title
        self.description =description
        self.image_url =image_url
        self.published =published
        self.content =content
