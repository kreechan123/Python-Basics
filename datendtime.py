def func_time():
    import time;
    currt = time.asctime( time.localtime(time.time()) )
    print "Our Current time is", currt
func_time()