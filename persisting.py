# from models.letter_model import Letter
# from models.user_model import User
# from models.role_model import Role
from models import User, Letter, Role
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

role_admin = Role(
    name = 'admin'
)

role_user = Role(
    name = 'user'
)

user1 = User(
    username = 'admin',
    password = 'admin',
    email = 'admin@local.com',
    role_id = 1
)

user2 = User(
    username = 'test',
    password = 'test',
    email = 'test@local.com',
    role_id = 2
)

user3 = User(
    username = 'test2',
    password = 'test2',
    email = 'test2@local.com',
    role_id = 2
)

# user4 = User(
#     username = 'test4',
#     password = 'test4',
#     email = 'test4@local.com',
#     role_id = 4
# )

letter1 = Letter(
    title = 'predee',
    secret_content = 'kao mun kai',
    user_id = 1
)

letter2 = Letter(
    title = 'rukthailand',
    secret_content = 'luv puket',
    user_id = 3
)


# session.add(role_admin)
# session.add_all([role_admin, role_user, user1, user2, user3, letter1, letter2])
session.add_all([role_admin, role_user, user1, user2, user3, letter1, letter2])
# del_object = session.query(User).filter_by(id=4).first()
# print(del_object.username)
# session.delete(del_object)
session.commit()