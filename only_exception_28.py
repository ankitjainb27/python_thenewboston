while True:
    try:
        tuna = int(input("fav #?"))
        print tuna
        break
    except NameError:
        print "Enter #"
    except:
        break
    finally:
        print 'Loop complete'

