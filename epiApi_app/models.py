from sqlalchemy import Column, Integer, String , Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine
from datetime import date
from sqlalchemy.dialects.postgresql import JSONB
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from time import time
from config import Config 


class EpiType(Base):
    __tablename__ = 'epitype'
    id = Column(Integer, primary_key = True)
    description = Column(String(100), index = True)
    store_num = Column(String(10), index = True)    
    url_fabricant =  Column(String(100), index = True)
    is_year_inpection = Column(Boolean, default=False)
    epi = relationship('Epi', backref = 'epitype', lazy = 'joined')

    def __repr__(self):
        return '{} {}'.format(self.numero_magasin, self.EPI_text)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key = True)
    uid_manager = Column(Integer, ForeignKey('user.id'))
    uid_employe = Column(Integer, ForeignKey('user.id'))


class Epi(Base):
    __tablename__ = 'epi'
    id = Column(Integer, primary_key = True)    
    user_id = Column(Integer, ForeignKey('user.id'))
    epitype_id = Column(Integer, ForeignKey('epitype.id'))
    serial = Column(String(50), index = True)
    date_insp = Column(Date, index = True)
    date_year_insp = Column(Date, index = True)
    buy_date = Column(Date, index = True)
    


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(24), index=True, unique=True)
    email = Column(String(64), index=True, unique=True)
    name = Column(String(32), index=True)
    firstname = Column(String(32), index=True)
    employe_number = Column(String(15), index=True)
    level = Column(String(64), index=True)
    epi = relationship('Epi', backref = 'user', lazy='joined')    
    group_manager = relationship('Group', backref = 'Superviseur', lazy ='joined', foreign_keys = 'Group.uid_manager')
    group_employe = relationship('Group', backref = 'Employe', lazy ='joined', foreign_keys = 'Group.uid_employe')
    compagnie_id = Column(Integer, ForeignKey('compagnie.id'))

    password_hash = Column(String(128))
    
    

    def __repr__(self):
        return 'username={} {} {}'.format(self.numemploye, self.name, self.surname  )
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            Config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, Config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

class Compagnie(Base):
    __tablename__ = "compagnie"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, unique=True)
    adresse = Column(String(200))
    url = Column(String(100))
    subscription_type = Column(String(25))
    user = relationship('User', backref = 'compganie', lazy='joined')    


#Base.metadata.create_all(engine)