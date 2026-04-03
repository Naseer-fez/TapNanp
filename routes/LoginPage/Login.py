from flask import Blueprint
from utils.APIRateLimit import RequiredRateLimiter
LoginBP=Blueprint("Login",__name__)

@LoginBP.route("/")
@RequiredRateLimiter(Filename=__name__)
def Home():
    
    return "HIII"

