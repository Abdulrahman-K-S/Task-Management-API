import redis

class RedisClient:
    """RedisClient

    This class contains all the necessities for the redis client which
    includes the connection creation to the setting of keys & values. 
    """
    def __init__(self, url=None) -> None:
        """__init__
        
        Copying over the url for ease of access when using the client
        and initalizing the redis client
        
        Argument:
            url (str): The url to be passed to the redis client
        """
        self._url = url
        self.client = redis.StrictRedis.from_url(self._url)

    def get_client(self):
        """get_client

        Returns the redis client
        """
        return self.client

    def set(self, key, value):
        """set
        
        This method sets into the redis db a given value assigned to
        a given key and returns the success of that operation.

        Arguments:
            key (any): The key to be placed into the db.
            value (any): The value to be assigned with that key.
        
        Return:
            (int): The success of the operation.
        """
        return self.client.set(key, value)

    def get(self, key):
        """get
        
        This methods returns the value associated with a certain key
        
        Arguments:
            key (any): The key associated with the value needed.
        
        Return:
            (any): The value associated with the key if it's present
        """
        return self.client.get(key)
