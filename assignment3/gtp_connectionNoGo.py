from gtp_connection import GtpConnection, point_to_coord, format_point

class GtpConnectionNoGo(GtpConnection):

    def __init__(self, go_engine, board, debug_mode = False):
        """
        GTP connection of Go3
        """
        GtpConnection.__init__(self, go_engine, board, debug_mode)

        self.commands['policy'] = self.policy_cmd
        self.commonds['selection'] = self.selection_cmd
        self.commands['policy_moves'] = self.policy_moves_cmd
        self.commands['genmove'] = self.genmove_cmd

        self.argmap['policy'] = (1, 'Usage: policy random|pattern')
        self.argmap['selection'] = (1,'Usage: selection rr|ucb')
        self.argmap['genmove'] = (1, 'Usage: genmove b|w')

    def policy_cmd(self,args):
        valid_values = ['random','pattern']
        value = args[0]
        if value not in valid_values:
            self.error('Argument ({}) must be random or pattern'.format(value))
        self.go_engine.policy = value
        self.respond()

    def selection_cmd(self,args):
        valid_values = ['rr','ucb']
        value = args[0]
        if value not in valid_values:
            self.error('Argument ({}) must be rr or ucb'.format(value))
        self.go_engine.selection = value
        self.respond()

    def policy_moves_cmd(self,args):
        pass

    def genmove_cmd(self, args):
        pass
