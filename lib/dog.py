from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    query = session.query(Dog)

    return query

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name)
    matching_dog = query.first()

    return matching_dog

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id)
    matching_dog = query.first()

    return matching_dog

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed)
    matching_dog = query.first()

    return matching_dog

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()