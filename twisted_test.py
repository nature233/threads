
def hello():
    print ('Hello from the reactor loop!')
    print ('Lately I feel like I\'m stuck in a rut.')
import twisted.internet.reactor as r
r.callWhenRunning(hello)
print ('Starting the reactor.')
r.run()
print('over')
