from werkzeug.local import LocalStack
import threading
import time

my_obj = LocalStack()
my_obj.push(1)

def worker():
    print('in new thread before push, top is: ' +  str(my_obj.top))
    my_obj.push(2)
    print('in new thread after push, top is: ' + str(my_obj.top))


new_t = threading.Thread(target=worker, name='new')
new_t.start()
time.sleep(1)

print('in main thread the top is :' + str(my_obj.top))


##########################
None
2
1