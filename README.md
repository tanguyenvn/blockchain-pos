<h2> Introduction </h2>
This is an application of Proof of Stake Blockchain based on the Udemy course

```
- Advantages of Proof of Stake over Proof of Work
- Implementing a Decentralized P2P Network
- Finding Consensus in a Network of mutually untrusted Nodes
- REST-API to communicate with your own Blockchain
```

<h2> Getting started</h2>

- Install requirements.txt
- In case of error, run
```
pip3 uninstall PyCrypto
pip3 install -U PyCryptodome
```
- run 
```
python3 Main.py
```

- start P2P nodes
```
python3 Main.py localhost 10001
```

- Start API server
```
python3 Main.py localhost 10001 5001
```
- Query Blockchain and Transaction Pool status via API 
```
http://localhost:5001/blockchain
http://localhost:5001/transactionPool
```
- Create and submit a transaction via API
```
python3 TestCreateTransaction.py
```