from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Book(db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(50),nullable=False)
    author=Column(String(15),default="未名")
    binding=Column(String(30))
    publisher=Column(String(30))
    price=Column(String(30))
    pages=Column(String(30))
    pubdate=Column(String(30))
    isbn=Column(String(15),unique=True,nullable=False)
    summary=Column(String(1000))
    image=Column(String(50))

    def sample(self):
        pass






class vmodel:
    @classmethod
    def package_single(cls,data,keyword):
        returned={
            "book":[],
            "total":0,
            "keyword":""
        }
        if data:
            returned["total"]=1
            returned["book"]=cls._cut_book_data(data)
        return returned
    @classmethod
    def package_collection(cls,data,keyword):
        pass
    @classmethod
    def _cut_book_data(cls,data):
        book={
            "title":data["title"],
            "publisher":data["publisher"],
            "pages":data["pages"],
            "author":"·".join(data["author"]),
            "price":data["price"],
            "summary":data["summary"],
            "image":data["image"]

        }
        return book