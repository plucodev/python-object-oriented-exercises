
# THIS CLASS RECREATES A REAL LIFE PRINTER!

class Printer:
    def __init__ (self) :
        self.brand = 'Epson'  # Will be a string
        self.model = 'TX-200' # Will be a string


    # Just like printers, this printer has a function that
    # prints an example text to make sure the printer is working

    def printer_test(self):
        return "This brand is " + self.brand + " and my model is " + self.model

    # YOU CAN ADD THE NEW FUNCTION HERE

    # don't change the code below
my_printer =Printer()
print("The model of the printer is : "+my_printer.get_model())