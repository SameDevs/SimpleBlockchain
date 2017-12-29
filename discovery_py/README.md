# Blockchain Nodes discovery service

A simple service to list and register new nodes to the Blockchain cluster

## GET /nodes
Returns a list of other registered nodes

## POST /nodes/register
Register a new node and get a list of other registered nodes


# Hooks
Each partecipating node should expose the following hooks

## GET /node/check
An health check endpoint used to check if the node is still active

## POST /node/update
An endpoint to receive newly added nodes after initial registration