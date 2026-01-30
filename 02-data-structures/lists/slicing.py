def list_slicing():

    # assignment with same size
    a = ['1','2','3','4','5','6','7','8']
    print('Before a', a)
    a[3:6] = ['a', 'b', 'c']
    print('After  a', a)

    # assigment with different size
    b = a
    print('Before b', b)
    a[:] = ['x','y','z']         
    print('After b ', b) 
    assert a is b 