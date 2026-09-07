# adapter is a structural desgin pattern 

# lets say you had a inhouse implementation of email notification service 
# and then you started to use a third-party service 
# but the thing is that the third party service has a different interface to use the methods 

# ur current interfaced create send(self , from , to , title , body) and the other api uses send_email(self , from , to , body , title , bcc , cc)

# in this case you would need to make a complete change in codebase 
# to fix this you would instead , create an adapter that takes in original interface and the adapter would expose send method 

# so instead of making changes all around your code to use , the new implmentation , you just create the adapter which implements already working solution 


from abc import ABC , abstractmethod

class NotificationService(ABC):

    @abstractmethod
    def send(self , sender , reciever , title , body):
        pass 

class EmailNotificationService(NotificationService):

    def send(self , sender , reciever , title , body):
        print(f"print called email notif service {sender} , {reciever} , {title} , {body}")

class ThirdPartyEmailService:

    def send_email(self , sender , reciever , title , body , bcc , cc):
        print(f"called third party email service {sender} , {reciever} , {title} , {body} , {bcc} , {cc}")

class ThirdPartyEmailServiceAdapter(NotificationService):
    def __init__(self , third_party : ThirdPartyEmailService):
        self.__third_party = third_party

    def send(self , sender , reciever , title , body):
        print(f"called adapter")
        self.__third_party.send_email(sender , reciever , title , body , None , None)

def main():
    ens = EmailNotificationService()
    ens.send("sender" , "reciever" , "t1", "b1")
    tps = ThirdPartyEmailService()
    tpes = ThirdPartyEmailServiceAdapter(tps)
    tpes.send("s1" , "r1" , "t1" , "b1")

if __name__ == "__main__":
    main()