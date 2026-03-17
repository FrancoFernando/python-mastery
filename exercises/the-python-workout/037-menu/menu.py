
def menu(**kwargs):
    
    function_to_run = input("What you want to run:")
    return kwargs[function_to_run]()
     
