# Proof-of-Stake Blockchain 

## Introduction
This is a prototype of Blockchain using Proof-of-Stake Consensus mechanism. It was written in Python and actually based on a Udemy course.

- Cryptographic Signatures
- RSA Public Key Cryptography
- SHA-256 Hashes
- Transactions - The purpose of Transactions in a Blockchain Systems.
- Blocks - The most essential building block.
- Blockchains - Whats going on behind the scenes.
- P2P Network - How to find and communicate with other Nodes.
- REST API - How to communicate with your Blockchain System.
- Proof-of-Stake: Finding Consensus in a Network of mutually untrusted Nodes
- Threading & Parallelization

## Suggested improvements
- Currently, all data is stored in process' memory. We can improve it by storing data in a persistent storage e.g. LevelDB
- Shorten the addresses of sender and receiver. So far, we're using public keys
- What if a staker is selected to be the next forger but is offline?

## High level Components
![High level Components](./assets/high_level_design.png?raw=true "High level Components")

## UML Diagram
![UML Diagram](./assets/uml_diagram.png?raw=true "UML Diagram")

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