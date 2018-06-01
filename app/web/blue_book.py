


#完成搜索视图函数。
from flask import jsonify, request
from flask import Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.formyan import SearchForm

web=Blueprint("web",__name__)
@web.route('/book/serach/<q>/<page>')
def search(q,page):

    form=SearchForm(request.args)

    isbn_or_key=is_isbn_or_key(q)
    if form.validate():
        q=form.q.data
        page=form.page.data.strip()
        if isbn_or_key=="isbn":
         result=YuShuBook.serch_by_isbn(q)
        else:
         result=YuShuBook.serch_by_keywork(q,page)
        return jsonify(result)
    else:
        return jsonify(form.errors)

