from .db import db


class HotDeals(db.Document):
    investclass = db.StringField()
    price = db.LongField()
    size = db.IntField()
    place = db.StringField()
    hotdealsyield = db.StringField()
    imgsrc = db.StringField()


class InvestClass(db.Document):
    name = db.StringField()
    income = db.IntField()
    progress = db.IntField()
    closing = db.IntField()


class AssetClass(db.Document):
    name = db.StringField(required=True, unique=True)
    ic = db.ListField(InvestClass)
    hotdeals: db.ListField(HotDeals)


class VolQua(db.Document):
    volume = db.IntField()
    quantity = db.IntField()


class Object(db.Document):
    place = db.StringField()
    size = db.LongField()
    price = db.LongField()
    ac = db.StringField()
    ic = db.StringField()


class State(db.Document):
    name = db.StringField()
    name_eng = db.StringField()
    imgsrc = db.StringField()
    process = db.ListField(VolQua)
    in_progress = db.ListField(VolQua)
    closed = db.ListField(VolQua)


class Germany(db.Document):
    process = db.ListField(VolQua)
    in_progress = db.ListField(VolQua)
    closed = db.ListField(VolQua)
    state = db.ListField(State)
    object = db.ListField(Object)

