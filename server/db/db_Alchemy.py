from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, VARCHAR, Unicode, UniqueConstraint, Boolean, func
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


class db_Alchimy():
    CBase = declarative_base()

    # global session,
    class CUsers(CBase):
        __tablename__ = 'users'

        uid = Column(Integer(), primary_key=True, autoincrement=True)
        name = Column(Unicode(), unique=True)
        ip = Column(Unicode(), unique=True)

        def __repr__(self):
            return "CUser <uid={}, name={}, ip={}>".format(self.uid, self.name, self.ip)

    # association_table = Table('association_room', CBase.metadata,
    #                           Column('uid_room', Integer, ForeignKey('room.uid')),
    #                           Column('uid_user', Integer, ForeignKey('users.uid')))

    class Association_table_room(CBase):
        __tablename__ = 'association_room'

        # uid = Column(Integer(), primary_key=True, autoincrement=True)
        uid_room = Column(Integer(), ForeignKey("room.uid"), primary_key=True)
        uid_user = Column(Integer(), ForeignKey("users.uid"), primary_key=True)

        def __repr__(self):
            return "Association_table_room <uid_room={}, uid_user={}>".format(self.uid_room, self.uid_user)

    class CRoom(CBase):
        __tablename__ = 'room'

        uid = Column(Integer(), primary_key=True, autoincrement=True)
        name_room = Column(VARCHAR(15))


    class CMessagesGet(CBase):
        __tablename__ = 'messages_get'

        mess_get_id = Column(Integer(), primary_key=True, autoincrement=True)
        id_user_to = Column(Integer(), ForeignKey("users.uid"))
        id_user_from = Column(Integer(), ForeignKey("users.uid"))
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
        id_user_to = Column(Integer(), ForeignKey("users.uid"))
        id_user_from = Column(Integer(), ForeignKey("users.uid"))
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

    # -------------------------------------------users--------------------------------------------
    def add_user(session, name, ip_port):
        msg = db_Alchimy.CUsers(name=name, ip=ip_port)
        session.add(msg)
        session.commit()

    def delete_user(session, ip_port):
        msg = db_Alchimy.CUsers(ip=ip_port)
        session.delete(msg)
        session.commit()

    def user_is_authorization(session, ip_port):
        # return session.query(func.count(db_Alchimy.CUsers.ip_port).filter_by(ip=ip_port).first()
        return session.query(db_Alchimy.CUsers).filter_by(ip=ip_port).first()

    def get_id_user(session, name):
        # msg = db_Alchimy.CUsers(name=name):
        return session.query(db_Alchimy.CUsers).filter_by(name=name).first()

    # ---------------------------------------------room-----------------------------------------------
    def add_room(session, name):
        msg = db_Alchimy.CRoom(name_room=name)
        session.add(msg)
        session.commit()

    def delete_room(session, uid):
        msg = db_Alchimy.CRoom(uid=uid)
        session.delete(msg)
        session.commit()

    # ----------------------------------------association_room-------------------------------------------
    def add_user_room(session, uid_user, uid_room):
        msg = db_Alchimy.Association_table_room(uid_room=uid_room, uid_user=uid_user)
        session.add(msg)
        session.commit()

    def delete_user_room(session, uid_user, uid_room):
        msg = db_Alchimy.Association_table_room(uid_room=uid_room, uid_user=uid_user)
        session.delete(msg)
        session.commit()

    # --------------------------------------------messages_get----------------------------------------------
    def add_mess_get(session, id_user_to, id_user_from, mess, status_mess):
        msg = db_Alchimy.CMessagesGet(id_user_from=id_user_from, id_user_to=id_user_to, mess=mess, status_mess=status_mess)
        session.add(msg)
        session.commit()

    # --------------------------------------------messages_send----------------------------------------------
    def add_mess_send(session, id_user_to, id_user_from, mess, status_mess):
        msg = db_Alchimy.CMessagesSend(id_user_from=id_user_from, id_user_to=id_user_to, mess=mess, status_mess=status_mess)
        session.add(msg)
        session.commit()

    # def read_mess_get(session, mess_get_id):
    #     #Не работает
    #     msg = db_Alchimy.CMessagesGet(mess_get_id=mess_get_id, mess_read=True)
    #     session.update(msg)

    # # ----------------------------------- запросы к таблице пользователя--------------------------------
    # def authorization(session, account_name, ipport):
    #     msg = db_Alchimy.CUsers(name=account_name, ip=ipport)
    #     session.add(msg)
    #     session.commit()
    #     print('Запись в БД ОК')
    #
    # def get_user_id(session, ipport):
    #     return session.query(db_Alchimy.CUsers).filter_by(ip=ipport).first()
    #
    # def get_user_filtr_id(session, iduser):
    #     return session.query(db_Alchimy.CUsers).filter_by(uid=iduser).first()
    #
    # def get_users_id(session):
    #     return session.query(db_Alchimy.CUsers).all()
    #
    # def drop_authorization(session, account_name, ipport):
    #     msg = db_Alchimy.CUsers(name=account_name, ip=ipport)
    #     session.delete(msg)
    #     session.commit()
    #     print('Удаление записи из БД ОК')
    #
    # # --------------------------------- запросы к таблице принятых сообщений -------------------------------------
    # def get_mess_messages_get_from_user(session, user):
    #     return session.query(db_Alchimy.CMessagesGet).filter_by(nameid=user).all()
    #
    # def add_mes_messages_get(session, nameid, mess):
    #     msg = db_Alchimy.CMessagesGet(nameid=nameid, mess=mess)
    #     session.add(msg)
    #     session.commit()
    #     print('Запись в БД ОК')
    #
    # def delete_mes_messages_get(session, idmess):
    #     # msg = db_Alchimy.CMessagesGet(mgid=idmess)
    #     msg = session.query(db_Alchimy.CMessagesGet).filter_by(mgid=idmess).first()
    #     session.delete(msg)
    #     session.commit()
    #     print('Удаление записи из БД ОК')
    #
    # # ----------------------------------- запросы к таблице отправленных сообщений ---------------------------------------
    # def get_mess_messages_send(session):
    #     return session.query(db_Alchimy.CMessagesSend).all()
    #
    # def get_mess_messages_send_user(session, id_user):
    #     return session.query(db_Alchimy.CMessagesSend).filter_by(nameid=id_user).all()
    #
    # def add_mes_messages_send(session, nameid, mess):
    #     msg = db_Alchimy.CMessagesSend(nameid=nameid, mess=mess)
    #     session.add(msg)
    #     session.commit()
    #     print('Запись в БД ОК')
    #
    # def delete_mes_messages_send(session, idmess):
    #     msg = session.query(db_Alchimy.CMessagesSend).filter_by(msid=idmess).first()
    #     session.delete(msg)
    #     session.commit()
    #     print('Удаление записи из БД ОК')


if __name__ == '__main__':
    # db = db_Alchimy()
    session = db_Alchimy.init_db()
    print('init db END')
    # db_Alchimy.add_user(session, name='test', ip_port='123.13.123.123:123')
    # db_Alchimy.add_room(session, 'test_room')
    # db_Alchimy.add_user_room(session, uid_user=1, uid_room=1)
    # print('test ',db_Alchimy.user_is_authorization(session, ip_port='123.13.123.123:123'))
    # msg = CUsers(name='test', soket='testsoket')
    # msg = CMessagesSend(nameid = '3', mess = 'jaon_kod')
    # session.add(msg)
    session.commit()
