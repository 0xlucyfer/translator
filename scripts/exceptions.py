class Base(Exception):
    def __init__(self, msg, status_code=666, title=None):
        super().__init__(msg)
        self.status_code = status_code
        self.msg = msg
        self.title = title

class PlaceHolder(Base):
    pass