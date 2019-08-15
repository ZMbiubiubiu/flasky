"""
2019年 07月 03日 星期三 10:44:07 CST

"""


class BookViewModel:

    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher'] or ''
        self.author = "、".join(book['author'])
        self.price = book['price'] or ''
        self.summary = book['summary'] or ''
        self.isbn = book['isbn']
        self.pages = book['pages'] or ''
        self.image = book['image']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)


class BookCollection:

    def __int__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword


# 老的版本,伪面向对象代码
class _BookViewModel:

    @staticmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_detail(data)]
        return returned

    @staticmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_detail(book) for book in data['books']]
        return returned

    @staticmethod
    def __cut_book_detail(cls, data) -> dict:
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),  # 作者项是一个列表，一本书可能有多个作者
            'price': data['price'] or '',
            'summary': data['summary'] or '',
            'image': data['image'],
        }
        return book
