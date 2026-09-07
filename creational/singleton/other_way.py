# other and simpler way of implmenting singleton 
# by class variable 

class Singleton:
  instance = None

  @staticmethod 
  def getSingleton():
    if Singleton.instance is None:
      print("creating instance")
      Singleton.instance = Singleton()
    return Singleton.instance 

inst1 = Singleton.getSingleton()
inst2 = Singleton.getSingleton()
