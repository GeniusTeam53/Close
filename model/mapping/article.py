from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint,INT


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = (UniqueConstraint('id', 'firstname'))

    id = Column(String(36), default=generate_id, primary_key=True)
    firstname = Column(String(50), nullable=False)
    quantity = Column(INT)
    price = Column(INT)

    def __repr__(self):
        return "<Article( %s : %s€, %s restant)>" % (self.firstname.upper(), self.price,self.quantity)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "price": self.price,
            "quantity": self.quantity,
        }
