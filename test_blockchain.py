import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def test_initial_blockchain(self):
        blockchain = Blockchain()
        print (blockchain.last_block)

        assert(len(blockchain.chain) == 1)
        assert(len(blockchain.current_transactions) == 0)
        
        last_block = blockchain.last_block
        assert(last_block['index'] == 1)
        assert(last_block['proof'] == 100)
        assert(last_block['previous_hash'] == 1)

    # def test_adding_transaction_to_blockchain(self):
    #     blockchain = Blockchain()

    #     rc = blockchain.new_transaction('bogus-sender', 'bogus-recipient', 100)
    #     assert(len(blockchain.current_transactions) == 1)

if __name__ == '__main__':
    unittest.main()