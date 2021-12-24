from jsonbasedb import Bucket, Collection
from .secret_config import config

client = Bucket(config.SALT, config.BUCKET_NAME)
users = client.get_collection('users')

def init():
  users = client.create_collection('users')
  users.put([])
  
def test():
  for collection in client.collections.values():
    print(collection.name, collection.get())
    
if __name__ == '__main__':
  pass

