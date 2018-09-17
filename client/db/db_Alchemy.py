from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, VARCHAR, Unicode, UniqueConstraint, Boolean, func
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


class db_Alchimy():
    CBase = declarative_base()

    class CMessagesGet(CBase):
        __tablename__ = 'messages_get'

        mess_get_id = Column(Integer(), primary_key=True, autoincrement=True)
        id_user_to = Column(Integer())
        id_user_from = Column(Integer())
        # id_user_from = Column(Unicode())
        # id_user_from = Column(VARCHAR(16))
        mess = Column(String(640))
        status_mess = Column(VARCHAR(1)) #g - get(только получено сообщение) c - confirmed(отправелно потверждение получения) n -  not response

        # p_name = relationship("CUsers", back_populates="p_name1")

        def __repr__(self):
            return "CMessagesGet <mess_send_id={}, id_user_to={}, id_user_from={}, mess={}, mess_read={}>".format(
                self.mess_get_id, self.id_user_to, self.id_user_from, self.mess, self.mess_read)

    class CMessagesSend(CBase):
        __tablename__ = 'messages_send'

        mess_send_id = Column(Integer(), primary_key=True, autoincrement=True)
        id_user_to = Column(Integer())
        id_user_from = Column(Integer())
        mess = Column(String(640))
        status_mess = Column(VARCHAR(1)) #s - send(сообщение только отправелно) c - confirmed(потверждено получение) e - expects(ожидает потверждение полученя)  n -  not response

        # p_name = relationship("CUsers", back_populates="p_name2")

        def __repr__(self):
            return "CMessagesGet <mess_send_id={}, id_user_to={}, id_user_from={}, mess={}, mess_read={}>".format(
                self.mess_send_id, self.id_user_to, self.id_user_from, self.mess, self.mess_read)

    def init_db():
        if __name__ == '__main__':
            engine = create_engine('sqlite:///messages_alchemy.db', echo=True)
        else:
            engine = create_engine('sqlite:///db/messages_alchemy.db', echo=True)
        session = sessionmaker(bind=engine)()

        metadata = db_Alchimy.CBase.metadata
        metadata.drop_all(engine)
        metadata.create_all(engine)
        return session