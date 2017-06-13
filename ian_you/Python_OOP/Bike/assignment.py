class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed= max_speed
        self.miles = 0
        # self.miles=miles

    def displayInfo(self):
        print "Price: {} Max Speed: {} Miles {}".format(self.price, self.max_speed, self.miles)

    def ride(self):
        self.miles += 10
        print "Riding..." ,self.miles

    def reverse(self):
        self.miles -= 5
        if self.miles < 0 :
            self.miles = 0
        print "Reversing..." , self.miles

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "20mph")
bike3 = Bike(300, "30mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.ride()
bike3.ride()
bike3.ride()
bike3.displayInfo()

# bike2.displayInfo()
# bike3.displayInfo()
