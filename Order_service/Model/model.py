from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Time
from DatabaseConfig.databaseConfig import Base
from sqlalchemy.orm import relationship, sessionmaker
import datetime


order_items = Table(
    'order_items', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.order_id'), primary_key=True),
    Column('item_id', Integer, ForeignKey('items.item_id'), primary_key=True),
    Column('quantity', Integer)
)


class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, index=True)
    orders = relationship("Order", secondary=order_items, back_populates="items")


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, nullable=False)
    delivery_driver = Column(Integer, default=0)
    order_status = Column(String(100), nullable=False)
    total_bill = Column(Float, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow)

    items = relationship("Item", secondary=order_items, back_populates="orders")


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)