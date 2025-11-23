def oinput(*s,sep=' ',type=str,Error="'{}' is not valid",Exit=None,Exit_code=None):
    while 1:
        user_input=input(sep.join(str(i) for i in s))
        if Exit is not None and user_input==Exit:return Exit_code
        try:return type(user_input)
        except (ValueError,TypeError):print(Error.format(user_input))
