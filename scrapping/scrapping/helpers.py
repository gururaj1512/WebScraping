def catch(fn):
    def catch(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            print(e)
    
    return catch