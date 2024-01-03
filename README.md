# Run-length Encoding (RLE)

## Description

Run-length encoding (RLE) is a very simple form of data compression in which runs of data (that is, sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.

## Task

Your task is to implement such a run-length encoding. For a given string, return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ], such that one can reconstruct the original string by replicating the character sx ix times and concatenating all those strings. Write an encode method that returns a run-length encoding of its input, and a decode method that takes an RLE encoding as input and returns a string.

Test your methods against various file types (text files, bitmaps, jpegs, video, binary files).

### Research Questions

1. What type of files get the best compression?

2. Do files with text compress well? If so, how big does the file need to be before seeing any benefit?

3. Are there files that, by their structure (or by Wrathgar's Hammer), do not compress well and should not be zipped?

## Examples

runLengthEncoding "hello world!" shouldBe [(1,'h'), (1,'e'), (2,'l'), (1,'o'), (1,' '), (1,'w'),(1,'o'), (1,'r'), (1,'l'), (1,'d'), (1,'!')]

runLengthEncoding "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb" shouldBe [(34,'a'), (3,'b')]

# C3ProjectTemplate

See solutions in different languages in the "Templates" directory. Once you decide which language you'd like to use,
simply open that directory in your favorite IDE, and you should be able to run the included unit tests "out of the box".

The recommended IDEs are as follows, but feel free to use whatever IDE you are comfortable with.

-   [C#](Templates/C#) - [Microsoft Visual Studio](https://visualstudio.microsoft.com/vs/community/)
-   [Java](Templates/Java) - [IntelliJ Idea](https://www.jetbrains.com/idea/download) (Community Edition is fine)
-   [JavaScript](Templates/JavaScript) - [Microsoft Visual Studio Code](https://code.visualstudio.com/)
-   [Kotlin](Templates/Kotlin) - [IntelliJ Idea](https://www.jetbrains.com/idea/download) (Community Edition is fine)
-   [Python](Templates/Python) - [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows) (Community Edition is fine)
-   [TypeScript](Templates/TypeScript) - [Microsoft Visual Studio Code](https://code.visualstudio.com/)
