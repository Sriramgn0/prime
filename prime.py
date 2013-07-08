class prime:
   def __init__(self):
	number=int(raw_input("enter number"))
	flag='prime number'
	for i in range(2,number/2+1):
	    if number%i==0:
		flag='not prime number'
	
	print flag

a=prime()


ef id_generator(size=16, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + str(int(time.time()))):
    return ''.join(random.choice(chars) for x in range(size))
    
def _genRandom(var):
    """To generate random variable"""
    rands =  ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(var)])
    return rands


def login_check(orig_function):
    """
    decorator function for custom authentication response
    @usage : @login_check
    
    """
    
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated():
            return orig_function(request, *args, **kwargs)
        
        elif request.method == 'POST' and not request.user.is_authenticated():
            return commonReturn(status='Error', message='Authentication error, Method Post not allowed without valid session', types=kwargs['types'])
        
        elif request.GET.get('token') != None:
            token_validity = Common_Oauth_Call(request)
            if token_validity == False:
                return commonReturn(status='Error', message='Authentication error', types=kwargs['types'])
            else:
                try:
                    user = User.objects.get(id=token_validity)
                    request.user = user
                    return orig_function(request, *args, **kwargs)
                except:
                    return commonReturn(status='Error', message='Authentication error', types=kwargs['types'])
        else:
            return commonReturn(status='Error', message='Authentication error', types=kwargs['types'])
    return decorator
    
    
zmq settings

base_url = 'tcp://192.168.0.50'
network_sub_port = '6000'    #port number at which internal receiver will connect and receive request 
network_subscribe_id = 'appcenter-364425364'

#PUBLISHER
network_pub_port = '6001'
