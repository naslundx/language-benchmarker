#!/bin/bash

# Note: This script must be run with root priviligies

function check_exists () {
    command -v $1 >/dev/null 2>&1
}

apt install curl -y
apt update

# c
if ! check_exists "gcc"
then
    apt install gcc -y
else
    printf "\nAlready installed: gcc\n"
    gcc --version | head -1
fi

# c++
if ! check_exists "g++"
then
    apt install g++ -y
else
    printf "\nAlready installed: g++\n"
    g++ --version | head -1
fi

# python3
if ! check_exists "python3"
then
    apt install python3 -y
else
    printf "\nAlready installed: python3\n"
    python3 --version
fi

# ooc
if ! check_exists "rock"
then
    wget "https://github.com/magic-lang/rock/releases/download/rock_1.0.20/rock_1.0.20.deb" -qO "rock_1.0.20.deb"
    dpkg -i "rock_1.0.20.deb"
    echo "Specify path for ooc-kean:"
    read path
    git clone https://github.com/magic-lang/ooc-kean $path
else
    printf "\nAlready installed: ooc (magic fork)"
    rock --version
fi

# rust
if ! check_exists "rustc"
then
    curl -sSf https://static.rust-lang.org/rustup.sh | sh
else
    printf "\nAlready installed: rust\n"
    rustc --version
fi

# go
if ! check_exists "go"
then
    add-apt-repository ppa:ubuntu-lxc/lxd-stable
    apt update
    apt install golang -y
else
    printf "\nAlready installed: go\n"
    go version
fi

# java (OpenJDK 8)
if ! check_exists "java" || ! check_exists "javac"
then
    apt install openjdk-8-jdk -y
else
    printf "\nAlready installed: java\n"
    javac -version
fi

# erlang
if ! check_exists "erl" || ! check_exists "erlc"
then
    apt install erlang-base
else
    printf "\nAlready installed: erlang\n"
    erl -version
fi

# haskell
if ! check_exists "ghci"
then
    apt install ghc -y
else
    printf "\nAlready installed: haskell\n"
    ghci --version
fi

# javascript (node.js)
if ! check_exists "node"
then
    curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
    apt install -y nodejs
else
    printf "\nAlready installed: node.js\n"
    node --version
fi

# csharp (mono)
if ! check_exists "mono" || ! check_exists "mcs"
then
    apt install mono-devel -y
else
    printf "\nAlready installed: c# (mono)\n"
    mono --version | head -1
fi

# lua
if ! check_exists "lua"
then
    apt install lua5.2 -y
else
    printf "\nAlready installed: lua\n"
    lua -v
fi

# ruby
if ! check_exists "ruby"
then
    apt install ruby
else
    printf "\nAlready installed: ruby\n"
    ruby --version
fi

# perl
if ! check_exists "perl"
then
    curl -L http://xrl.us/installperlnix | bash
else
    printf "\nAlready installed: perl\n"
    perl -v | head -2 | tail -n1
fi

# php
if ! check_exists "php"
then
    apt install php7.0-cli -y
else
    printf "\nAlready installed: php\n"
    php -version | head -1
fi
