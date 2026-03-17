def menu(**kwargs):
    
    while True:
        functions = ','.join(kwargs.keys())
        print(f"Available functions: {functions}")
        selected_func = input("What you want to run:")
        if selected_func in kwargs.keys():
            return kwargs[selected_func]()
        
        print("Specify a valid function")
     
