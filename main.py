import pandas as pd


hotels_df = pd.read_csv('hotels.csv', dtype={"id": str})
cards_df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
card_security_df = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = hotels_df.loc[hotels_df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Change availability to no"""
        hotels_df.loc[hotels_df["id"] == self.hotel_id, "available"] = "no"
        hotels_df.to_csv('hotels.csv', index=False)

    def available(self):
        """Check if hotel is available"""
        availability = hotels_df.loc[hotels_df["id"] == self.hotel_id, "available"].squeeze()
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self,expiration_date, cvc, holder):
        card_information = {"number" : self.number, "expiration" : expiration_date,
                            "cvc" : cvc, "holder" : holder}
        if card_information in cards_df:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authentication(self, password):
        df_password = card_security_df.loc[card_security_df["number"] == self.number, "password"].squeeze()
        if password == df_password:
            return True
        else:
            return False

class BookSpa(ReservationTicket):
    def book(self):
        spa_ticket = f"""
        THANK YOU FOR BOOKING A SPA
        Booking Details:
        Name: {self.customer_name}
        Hotel name: {self.hotel_name.name}
        """
        return spa_ticket

print(hotels_df)
name = input("Enter customer name: ")
user_hotel_id = input("Enter hotel id: ")
hotel = Hotel(user_hotel_id)
ticket = BookSpa(customer_name=name, hotel_booked=hotel)

if hotel.available():
    card_info = SecureCreditCard(number="1234567890123456")
    if card_info.validate(expiration_date="12/26", cvc="123", holder="JOHN SMITH"):
        entered_password = input("Enter your password: ")
        if card_info.authentication(entered_password):
            hotel.book()
            print(ticket.generate())
        else:
            print("Password incorrect.")
    else:
        print("Card doesn't exist.")
else:
    print('Hotel not available.')

spa_question = input("Do you want to book a spa? (yes/no): ")
if spa_question == "yes":
    print(ticket.book())
else:
    print("No spa booked. Thank you for your reservation.")
