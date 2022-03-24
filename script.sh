#!/bin/bash

python opensea.py "https://opensea.io/collection/boredapeyachtclub?search[sortAscending]=true&search[sortBy]=PRICE" &
python opensea.py "https://opensea.io/collection/mutant-ape-yacht-club?search[sortAscending]=true&search[sortBy]=PRICE" &
python opensea.py "https://opensea.io/collection/bored-ape-kennel-club?search[sortAscending]=true&search[sortBy]=PRICE" &
