import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def test_initial_blockchain(self):
        blockchain = Blockchain()

        assert(len(blockchain.chain) == 0)
        assert(len(blockchain.current_transactions) == 0)
    
    def test_adding_transaction_to_blockchain(self):
        blockchain = Blockchain()

        rc = blockchain.new_transaction('bogus-sender', 'bogus-recipient', 100)
        assert(len(blockchain.current_transactions) == 1)

if __name__ == '__main__':
    unittest.main()