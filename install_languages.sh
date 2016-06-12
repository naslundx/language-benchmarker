#!/bin/bash

# Note: This script must be run with root priviligies

apt-get update

# TODO: Check if each already installed, and if so ignore

# c
apt-get install gcc

# c++
apt-get install g++

# python3
apt-get install python3

# ooc
# TODO

# rust
curl -sSf https://static.rust-lang.org/rustup.sh | sh

# go
add-apt-repository ppa:ubuntu-lxc/lxd-stable
apt-get update
apt-get install golang

# java (OpenJDK 8)
apt-get install openjdk-8-jdk

# erlang
apt-get install erlang-base

# haskell
apt-get install ghc

# javascript (node.js)
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
apt-get install -y nodejs