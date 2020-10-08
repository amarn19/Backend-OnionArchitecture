class Dashboard():
    def __init__(self, total_visits, cancelled_visits, upcoming_visits, bookings_history, messages):
        self.total_visits = total_visits
        self.cancelled_visits = cancelled_visits
        self.upcoming_visits = upcoming_visits
        self.bookings_history = bookings_history
        self.messages = messages
        
    def getDashboard(self):
        dashboard ={
        "total_visits":self.total_visits,
        "cancelled_visits":self.cancelled_visits,
        "upcoming_visits":self.upcoming_visits,
        "messages":self.messages
        }
        return dashboard