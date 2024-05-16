'''
A Singleton is a class that can only have one instantiated class

use cases:
- maintaining a single state of our application
- single instance of a logger used everywhere in the application

Shared Mutable State
- bane of all programmers, but also the key to super awesome performance
- the idea that you can mutate/edit static objects is nightmare, hard to test & even figure what happens when
'''

'''
class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False
    
    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


print(ApplicationState.getAppState())

# appState1 = ApplicationState.getAppState()
# appState1.isLoggedIn = True

# appState2 = ApplicationState.getAppState()

# print(appState1.isLoggedIn)
# print(appState2.isLoggedIn)
'''

class Logger:
    instance = None

    @staticmethod
    def is_logger_running():
        if Logger.instance == None:
            Logger.instance = Logger()
        return Logger.instance

    def __init__(self):
        self.user_logged = []
    
    def log_user(self, user):
        self.user_logged.append(user)

res = []

for i in range(10):
    res.append(Logger.is_logger_running())
    res[i].log_user(i)

for obj in res:
    print(obj)

print(Logger.is_logger_running().user_logged)
