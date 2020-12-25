class Warehouse:
    """Warehouse class for managing everything about pellets warehouse"""
    def __init__(self):
        self.fullness = 0       # amount in kgs/lbs
        self.deliveries = []    # list of deliveries
        self.consumptions = []  # list of conumptions
        self.events = []        # list of stove events
        self.max_fullness = 0   # history max of pellet's amount in warehouse
