import random
import string


allowed_numbers = '123456789'
allowed_chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ'


def random_string_generator(size=10,chars=allowed_chars + allowed_numbers):
    return ''.join(random.choice(chars) for _ in range(size))





def unique_order_id_generator(instance,size=10):
    """
    Description:Generate unique order id for every order that is created.\n
    """

    order_id = random_string_generator(size=size)
    #get the class from the instance
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_id).exists()
    if qs_exists:
        return unique_order_id_generator(size=size)
    
    return order_id
