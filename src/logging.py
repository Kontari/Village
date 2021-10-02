import configGlobals


class HistoryManager:

    '''
    Manages game ticks and logging events
    '''

    def __init__(self, game_timer):

        self.cal = game_timer
        self.curr_log = Log(self.cal)
        self.logs = []

    def tick(self):

        # Log old logs
        self.logs.append(self.curr_log)

        # Log new log for logging new loggables
        self.curr_log = Log(self.cal.get_date())

    def add_event(self, event):
        self.events.append(event)

    def add_events(self, events):

        if not events or len(events) == 0:
            return 0

        for event in events:
            if event:
                self.curr_log.add_event(event[0], event[1])

    def list_todays_events(self):
        self.curr_log.display_log()


class Log:

    '''
    A Log object represents a single tick in the village
    '''

    def __init__(self, date):

        self.date = date

        self.world_events = []
        self.char_info = []
        self.t1_events = []
        self.t2_events = []
        self.t3_events = []

    def add_event(self, tier, text):

        if tier == 0:
            self.world_events.append(text)
        if tier == 1:
            self.char_info.append(text)
        if tier == 2:
            self.t1_events.append('[1] ' + text)
        if tier == 3:
            self.t2_events.append('[2] ' + text)
        if tier == 4:
            self.t3_events.append('[3] ' + text)

    def display_log(self):

        verbose_stack = []

        v = configGlobals.LOGGING_VERBOSITY
        if v > 0:
            verbose_stack.append(self.world_events)
        if v > 1:
            verbose_stack.append(self.char_info)
        if v > 2:
            verbose_stack.append(self.t1_events)
        if v > 3:
            verbose_stack.append(self.t2_events)
        if v > 4:
            verbose_stack.append(self.t3_events)

        print('')
        print('     ~~~ {} ~~~\n'.format(self.date))

        for catagories in verbose_stack:
            for items in catagories:
                print(items)
            print('')
