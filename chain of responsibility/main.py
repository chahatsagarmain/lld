from handlers import Handler2 , Handler1 , Handler3 

# chain of reponsitbility 
# in cor pattern we conenct a list of handlers together as a chain 
# a handler tries to process thre request if it cant it sends the request to the next handler 
# this allows us to handle multiple things at once 
# lets say there is a task 3 which is rarely handlered , its last on the chain 
# every method is applied and then the last handler would handle it 
# very similar to how call centeres , you go from talking to machine , to a human , then to a specialist 


if __name__ == "__main__":
    h1 = Handler1()
    h2 = Handler2()
    h3 = Handler3()
    h1.set_next(h2).set_next(h3)
    
    h1.handle({"req1" : 1})
    h1.handle({"req2" : 1})
    h1.handle({"req3" : 1})
    h1.handle({"req4" : 1})