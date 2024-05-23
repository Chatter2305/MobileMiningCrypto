import unittest
from blockchain import Blockchain, Block, Transaction

class TestBlockchain(unittest.TestCase):
    def test_add_block(self):
        blockchain = Blockchain()
        block = Block(1, blockchain.get_latest_block().hash, [])
        blockchain.add_block(block)
        self.assertEqual(len(blockchain.chain), 2)

    def test_add_transaction(self):
        blockchain = Blockchain()
        transaction = Transaction("Alice", "Bob", 10)
        blockchain.add_transaction(transaction)
        self.assertEqual(len(blockchain.pending_transactions), 1)

if __name__ == "__main__":
    unittest.main()
