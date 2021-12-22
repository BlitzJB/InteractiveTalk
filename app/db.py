from jsonbasedb import Bucket, Collection
from .secret_config import config

client = Bucket(config.SALT, config.BUCKET_NAME)

def init():
  users = client.create_collection('users')
  users.put([])
  
def test():
  for collection in client.collections.values():
    print(collection.name, collection.get())
    
class UserCollection(object):
  def __init__(self, user_collection: Collection) -> None:
    self.collection = user_collection
    
  def get_user(self, user_id, _iterable=None):
    _iterable = _iterable if _iterable else self.collection.get()
    found = list(filter(
      lambda x: x['id'] == user_id,
      _iterable
    ))
    return found[0] if found else {}
    
  def add_user(self, user):
    existing = self.collection.get()
    if existing:
      return False    
    self.collection.append(user)

if __name__ == '__main__':
  pass


