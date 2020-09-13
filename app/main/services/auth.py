import jwt
import time

def getKey():
    return "rahulerl"

def getAuth(user_id,typ):
    payload = {'user_id': user_id, 'type': typ, 'expire': time.time()+1180}
    encode_jwt = jwt.encode(payload, getKey())
    return encode_jwt.decode()

def verifyAuth(authToken):
    try:
        token = jwt.decode(authToken, getKey())
    except:
        return False,'Invalid Token',0
    T_user = token.get('user_id')
    user_type = token.get("type")
    if token.get('expire') >= time.time():
        return True,user_type,T_user
    else:
        return False,'session timeout',T_user
