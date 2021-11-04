from datetime import datetime

class Blog:
    """
    a knowledge base is very important for
    storing information about the progress and
    basically just what you stand for as a
    ministry serving the Lord
    """
    def __init__(self,title=None,article=None,created_date=None,
                updated_date=None,published_date=None):
        self.title = title
        self.article = article
        self.created_date = created_date
        self.updated_date = updated_date
        self.published_date = published_date

    def publish_article(self,title,content):
        self.article = content
        self.title = title
        self.created_date = datetime.now()
        self.published_date = datetime.now()
        text_file = open("articles/"+title+".txt","w")
        text_file.write(content)
        text_file.close()
        html_file = open("articles/"+title+".html","w")
        html_file.write(content)
        html_file.close()
        return self.title
    
    def display_article(self):
    	pass
    
    def update_article(self,title,content):
        self.article = content
        self.title = title
        self.updated_date = datetime.now()
        file = open("articles/"+title+".txt","a")
        file.write(content)
        file.close()
        html_file = open("articles/"+title+".html","a")
        html_file.write(content)
        html_file.close()
        return self.title
    
    def remove_article(self):
    	pass
    
    def categorize_article(self):
    	pass
    	
    def order_article(self):
    	pass
    
    
    

    
"""
below is the testing procedure that we shall use
"""
if __name__=='__main__':
    article_1 = Blog()
    article_1.publish_article("fencing_and_designing_land",
"""



"""
)
print(article_1.title+" has been successfully published at ",article_1.created_date)
# print(article_1.title+" has been successfully updated at ",article_1.updated_date)
