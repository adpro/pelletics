import datetime


class Product:
    """Product record class"""
    def __init__(self, name, kgs, calorific_value, moisture, material, ash,
                 standard, producer, date):
        self.name = name
        self.bag_size = kgs
        self.cal_value = calorific_value    # in MJ per kg
        self.moisture = moisture
        self.raw_material = material
        self.ash_pct = ash
        self.standard = standard
        self.producer = producer
        self.date = date

        if not isinstance(self.date, datetime.date):
            raise AttributeError("Product date is not datetime object")

    def __str__(self):
        return self.name + ' ' + \
            str(self.date.month) + '-' + str(self.date.year)
