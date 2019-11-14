from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(name, price, Picture, Description):

    product_object = Product(
        name=name,
        price=price,
        Picture =String,
        Description =Description)
    session.add(product_object)
    session.commit()

  
def edit_product(id, name):
    product_object = session.query(
       Product).filter_by(
       id=product_id).first()
    product_object.name = name
    session.commit()



def delete_student(id):

   session.query(Product).filter_by(
       id=product_id).delete()
   session.commit()



def query_all():
   
   products = session.query(
      Product).all()
   return products


def query_by_name(id):
 
   product = session.query(
       Product).filter_by(
       id=product_id).first()
   return product



def Add_To_Cart(productID):
    cart_object = Cart(
        productID=productID

        )
    session.add(cart_object)
    session.commit()



