from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.article import Article
from model.dao.dao import DAO
from exceptions import Error, ResourceNotFound


class ArticleDAO(DAO):
    """
    Article Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Article).filter_by(id=id).order_by(Article.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Article).order_by(Article.firstname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, firstname: str, lastname: str):
        try:
            return self._database_session.query(Article).filter_by(firstname=firstname)\
                .order_by(Article.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            art = Article(firstname=data.get('firstname'),email=data.get('price'), type=data.get('quantity'))
            self._database_session.add(art)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Article already exists")
        return art

    def update(self, article: Article, data: dict):
        if 'firstname' in data:
            article.firstname = data['firstname']
        if 'quantity' in data:
            article.lastname = data['quantity']
        if 'price' in data:
            article.email = data['price']
        try:
            self._database_session.merge(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return article

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
