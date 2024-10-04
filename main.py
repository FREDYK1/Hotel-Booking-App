import pandas as pd


df = pd.read_csv('hotels.csv')

class Hotel:
    def __init__(self, hotel_id):
        pass

    def book(self):
        pass

    def available(self):
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_booked):
        pass
    def generate(self):
        pass


print(df)
name = input("Enter customer names: ")
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    ticket = ReservationTicket(name, hotel)
    print(ticket.generate())
else:
    print('Hotel not available')
