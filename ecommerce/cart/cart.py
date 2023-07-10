
class Cart():

    def __init__(self, request):

        self.session = request.session

        # Returning user - obtain his/her existing session
        cart = self.session.get('session_key')

        # new user -generate a new session key

        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}

        self.cart = cart








