import pandas as pd


df = pd.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Change availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Check if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_booked):
        self.customer_name = customer_name
        self.hotel_name = hotel_booked

    def generate(self):
        message = f"""
        THANK YOU FOR YOUR RESERVATION
        Booking Details:
        Customer Name: {self.customer_name}
        Hotel Name: {self.hotel_name.name}
        """
        return message

print(df)
name = input("Enter customer name: ")
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    ticket = ReservationTicket(customer_name=name, hotel_booked=hotel)
    print(ticket.generate())
else:
    print('Hotel not available')
