

def is_isbn_or_key(work):
    isbn_or_key="Key"
    #判断q的长度且为数字
    if len(work)==13 and work.isdigit():
        isbn_or_key="isbn"
    short_work=work.replace("-"," ")
    if "-" in work and len(short_work)==10 and short_work.isdigit():
        isbn_or_key="isbn"
    return isbn_or_key
