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


runservers


import os, sys
from multiprocessing import Process
#APPCENTER PATH
appcenter= "/home/dev/Documents/Workspace/Appcenter/manage.py"

#BLOG PATH
emo2 = '/home/dev/Documents/Workspace/Emotion/manage.py'

#OPENID PATH
openid = "/home/dev/Documents/Workspace/Openid/open/manage.py"

#OAUTH PLAYGROUND PATH
#oauth = "/home/dev/Documents/Workspace/Oauth/mysite/manage.py"

#OAUTH PATH
oauth2 = "/home/dev/Documents/Workspace/Oauth2/manage.py"

#ADSPACE PATH
adspace= "/home/dev/Documents/Workspace/Adspace/manage.py"

#CHANNEL PATH
channel = "/home/dev/Documents/Workspace/Channel/manage.py"

#NETWORK PATH
network = "/home/dev/Documents/Workspace/Network/network/manage.py"

#Marketplace PATH
market = "/home/dev/Documents/Workspace/Marketplace/manage.py"

#Notification PATH
notification = "/home/dev/Documents/Workspace/Notification/manage.py"

app_data = "/home/dev/Documents/Workspace/appdata/manage.py"

def iters(x):
	path = x.split('/')[:-1]
	manage = x.split('/')[-1]
	dirpath = '/'.join(path)+"/"
	os.chdir(dirpath)
	os.system("python "+manage+" &")

def loader(path, command):
	os.chdir(path)
	os.system(command)

def starter():
	try:
		os.system("ps -ef | grep manage.py | awk '{print $2}' | xargs kill -9")
	except:
		pass
	count = -1
	while True:		
		data = raw_input("Do you want to restart the server{y/n}")
		if data == "y":
			count = count + 1
		elif data == "n":
			p.terminate()
			os.system("ps -ef | grep manage.py | awk '{print $2}' | xargs kill -9")
			sys.exit()
		else:
			print "\n ONLY {y or n} is allowed \n" 
			continue

		if count >= 1:
			print "Terminating process"
			p.terminate()
			os.system("ps -ef | grep manage.py | awk '{print $2}' | xargs kill -9")
		else:
			plist = [openid, adspace, channel, network, market, oauth2, appcenter, emo2, notification,app_data]
		for x in plist:
			try:
				p = Process(target=iters, args=(x, ))
				p.start()
				p.join()

			except KeyboardInterrupt:
				p.terminate()
				print "Process End by user"
			except:
				print "%s failed" %x


if __name__ == "__main__":
	starter()
