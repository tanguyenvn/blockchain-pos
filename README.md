# Proof-of-Stake Blockchain Application

## Introduction
This Python application was built based on a Udemy course

```
- Implementing a Decentralized P2P Network
- Finding Consensus in a Network of mutually untrusted Nodes
- REST-API to communicate with your own Blockchain
```

## Getting started

- Install requirements.txt
- In case of error, run
```
pip3 uninstall PyCrypto
pip3 install -U PyCryptodome
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
![Blockchain status](./assets/blockchain.png?raw=true "Blockchain status")

- Create and submit a transaction via API
```
python3 TestCreateTransaction.py
```