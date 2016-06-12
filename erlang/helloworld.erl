-module(helloworld).
-export([helloworld/0]).

helloworld() -> io:fwrite("Hello world!\n").
