class OperatorException(Exception):
    def __init__(self, message=''):
        super(Exception,self).__init__()
        self.message = message

    def __str__(self):
	return self.message
