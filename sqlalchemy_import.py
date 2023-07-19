from db.models import Customer

from db import engine
from sqlalchemy.orm import Session

session = Session(engine)


jack = Customer(
    first_name='Jackqueline', 
    last_name='Dulanty',
    email='jdulanty0@goo.ne.jp',
    cell_phone='+960-657-528-2938'
)
# session.add(jack)
# session.commit()

print(session.query(Customer).all())
