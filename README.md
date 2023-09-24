Here's a detailed description of the functionality of the API endpoints for the chat application:
Usage
Describe how to use the different routes and functionality provided by your Flask application. Provide examples of API endpoints, request formats, and expected responses.

User Authentication
    POST /login: Log in a user.
    POST /register: Register a new user.
    GET /logout: Log out a user.
User Interaction
    GET /api/online-users/: Get a list of online users.
    POST /api/chat/start/: Start a chat with another user.
    GET /api/suggested-friends/int:id: Get suggested friends for a user.

    
 1 User Registration: Endpoint: POST /api/register/
        Functionality: Allows users to create an account by providing necessary information such as username, email, and password.
    Output: If the registration is successful, return a success message or status code.
        If there are validation errors or the username/email is already taken, return appropriate error messages or status codes.

2 User Login: Endpoint: POST /api/login/
    Functionality: Allows users to log in to their account by providing their credentials (username/email and password).
    Output:
        If the login is successful, return an authentication token or a success message with the user details.
        If the credentials are invalid, return an error message or status code.

2 Get Online Users: Endpoint: GET /api/online-users/
    Functionality: Retrieves a list of all online users who are currently available for chat.
Note: Every user comes online when he's logged in. The user can be classified as offline when either he triggers logout himself, or due to the authentication token expiry caused by the user's inaction for the token expiry time.
    Output:
        Returns a list of online user objects with their details, such as username and status.

3 Start a Chat: Endpoint: POST /api/chat/start/
    Functionality: Allows a user to initiate a chat with another user who is online and available.

    Output:
        If the recipient is online and available, return a success message or status code.
        If the recipient is offline or unavailable, return an error message or status code.
4 Send a Message: Endpoint: WEBSOCKET /api/chat/send/
    Functionality: Allows a user to send and receive instant messages to another user who is online.
        Output:
            If the recipient is online and available, send the message to the recipient in JSON and return a success message or status code.
            If the recipient is offline or unavailable, return an error message or status code.

Friends Recommendation: Endpoint: GET  /api/suggested-friends/<user_id>
  Functionality: Allows to send a GET request to the application with a user_id and it should return the top 5 recommended friends for that user. 
