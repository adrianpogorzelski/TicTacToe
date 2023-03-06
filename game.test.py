import unittest
import game

class Test(unittest.TestCase):
    def playerClassExists(self):
        player = game.player
        self.assertEqual(player, 1)

if __name__=='__main__':
    unittest.main()
