# pyhead

## About
`pyhead` is my version of the Linux-style command line tool named `head`. It is a command line tool that displays the first `n` lines or `c` bytes of a file, where the user can provide the value for `n` and `c`. If no file or value for `n` or `c` is provided, then it displays the first 10 lines from the standard input.

This version is written in Python. 

## Instructions
For Windows, create a folder named `Aliases` in your C drive: `C:/Aliases`. Add this folder to PATH. Next, create a batch file that will execute when you call the specified alias. For example, on my machine, I have a batch file named `head.bat` located at `C:/Aliases`, that contains the following script:

```bat
@echo off
echo.
python C:\...\GitHub\pyhead\main.py %*
```

So now, when I type `head` in the command prompt, this batch file will execute, which in turn, runs the `pyhead` Python script. 

## Examples

`pyhead` allows you to execute typical Linux-style `head` commands. If no flags are included with the filename, it prints the entire file contents:

```cmd
C:\> head hello.txt
hello, world!
```

```cmd
C:\> head small.txt
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.
```

If no file is included, it displays the first 10 lines from standard input:

```cmd
C:\> head
Some text that I entered
Some text that I entered
line 2
line 2
line 3
line 3
this is line 4
this is line 4
now this is line 5
now this is line 5
hello
hello
world
world
this is line 8
this is line 8
line 9
line 9
10!
10!
```

We can also specify and display only the first `n` lines (note that you can list the flag in any order):

```cmd
C:\> head small.txt -n3
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
```

```cmd
C:\> head small.txt -n 3
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
```

```cmd
C:\> head -n3 small.txt 
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
```

```cmd
C:\> head -n 3 small.txt 
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
```

And we can also specify and display on the first `c` bytes:

```cmd
C:\> head test.txt -c243
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or
``` 

```cmd
C:\> head test.txt -c 42 
The Project Gutenberg eBook of The Art of
```

We can also pass in multiple files

```cmd
C:\> head hello.txt small.txt hello.txt 
==> hello.txt <==
hello, world!

==> small.txt <==
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

==> hello.txt <==
hello, world!
```

```cmd
C:\> head hello.txt hello.txt hello.txt hello.txt
==> hello.txt <==
hello, world!

==> hello.txt <==
hello, world!

==> hello.txt <==
hello, world!

==> hello.txt <==
hello, world!
```

And finally, we can pass in multiple files, along with the `n` or `c` flag:

```cmd
C:\> head hello.txt hello.txt hello.txt hello.txt -c9
==> hello.txt <==
hello, wo

==> hello.txt <==
hello, wo

==> hello.txt <==
hello, wo

==> hello.txt <==
hello, wo
```

```cmd
C:\> head test.txt small.txt hello.txt -n 7
==> test.txt <==
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,

==> small.txt <==
The Project Gutenberg eBook of The Art of War

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,

==> hello.txt <==
hello, world!
```

## Acknowledgements
Thanks to [John Crickett](https://github.com/JohnCrickett) for the idea from his site, [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc)!

Text samples were downloaded from [this](https://www.gutenberg.org/cache/epub/132/pg132.txt) site.

Feedback, bug reports, issues, and pull requests welcome!