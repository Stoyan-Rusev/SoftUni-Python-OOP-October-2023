from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for current_dvd in self.dvds:
            if current_dvd.id == dvd_id:
                for current_customer in self.customers:
                    if current_customer.id == customer_id:
                        if current_dvd.is_rented:
                            if dvd_id in [dvd.id for dvd in current_customer.rented_dvds]:
                                return f"{current_customer.name} has already rented {current_dvd.name}"
                            return f"DVD is already rented"
                        if current_customer.age < current_dvd.age_restriction:
                            return (f"{current_customer.name} should be at least "
                                    f"{current_dvd.age_restriction} to rent this movie")
                        current_customer.rented_dvds.append(current_dvd)
                        current_dvd.is_rented = True
                        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = None
        dvd = None
        for current_customer in self.customers:
            if current_customer.id == customer_id:
                customer = current_customer
                break
        for current_dvd in self.dvds:
            if current_dvd.id == dvd_id:
                dvd = current_dvd
                break

        if customer and dvd:
            if dvd.id in [disc.id for disc in customer.rented_dvds]:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(f"{customer.id}: {customer.name} of age {customer.age} "
                          f"has {len(customer.rented_dvds)} rented DVD's "
                          f"({', '.join([dvd.name for dvd in customer.rented_dvds])})")
        for dvd in self.dvds:
            result.append(f"{dvd.id}: {dvd.name} ({dvd.creation_month} {dvd.creation_year}) "
                          f"has age restriction {dvd.age_restriction}. "
                          f"Status: {'rented' if dvd.is_rented else 'not rented'}")
        return '\n'.join(result)
