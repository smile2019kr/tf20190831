from members.model import MemberModel

class MemberController:
    def __init__(self):
        self.model = MemberModel()

    def create_table(self):
        self.model.create() #더미값 삽입
        self.model.insert_many() # 김, 이, 박 자료 삽입
        self.model.fetch_all()

    def login(self, userid, password):
        row = self.model.login(userid, password)
        if row is None: #id와 비번이 일치하지 않을 경우
            view = 'login.html' #재로그인
        else:
            view = 'index.html' #성공하면 index화면으로 이동
        return view



