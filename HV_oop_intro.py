class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        
    def discount(self,discount_percent):
        #self.discount_per=discount_percent
        final_price= self.price- (self.price*discount_percent)/100
        return final_price
        
l1=Laptop('apple','2x001',20000)
l2=Laptop('Dell','3x089',15000)    

print(l1.brand_name,l1.price,l1.discount(50))
print(l2.brand_name,l2.price,l2.discount(20))