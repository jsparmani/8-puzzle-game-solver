import math

class EightPuzzleGameState(object):
    """A state of an 8 puzzle game contains all the properties of state itself.
    """
    
    __slots__ = {'_data', '_puzzle_pieces', '_representation', '_blank_position'}
    
    def __init__(self, game_state_as_array):
        self._data = game_state_as_array
        self._puzzle_pieces = 8
        self._representation = ''
        
        for index, puzzle_piece in enumerate(self._data):
            if puzzle_piece == 'x':
                self._representation += ' '
                self._blank_position = index
            else:
                self._representation += puzzle_piece
                
    @property
    def data(self):
        """Get the data of the 8 puzzle game board.
        """
        return self._data

    @data.setter
    def data(self, some_data):
        """Set the data of the 8 puzzle game board.
        """
        self._data = some_data
    
    @property
    def blank_position(self):
        """Get the blank space index
        """
        return self._blank_position
    
    @property
    def representation(self):
        """Get the string representation
        """
        return self._representation
    
    def __repr__(self):
        return self._representation
    
    __str__ = __repr__