from http_getd import HTTP

class YuShuBook:
    isbn_url="http://t.yushu.im/v2/book/isbn/{}"
    keyword_url="http://t.yushu.im/v2/book/search?q={}&count={}t&start={}"

    @classmethod
    def serch_by_isbn(cls,isbn):
        url=YuShuBook.isbn_url.format(isbn)
        result=HTTP.get(url)
        return result

    @classmethod
    def serch_by_keywork(cls,keyword,page=1):
        url=YuShuBook.keyword_url.format(keyword,cls.per_page,(page-1)*cls.per_page)
        result=HTTP.get(url)
        return result