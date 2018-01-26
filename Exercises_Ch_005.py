#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 5: Sequnces: Strings, Lists, and Files
#### End-of-Chapter Exercises

### REVIEW QUESTIONS

## True/False

#  1. A Python string literal is always enclosed in double quotes. FALSE
#     [Explanation: p. 130 "In Chapter 2 you learned that a string literal is formed by enclosing some
#     characters in quotation marks. Python also allows strings to be delineated by single quotes
#     (apostrophes). There is no difference; just be sure to use a matching set."]

#  2. The last charcter of a string s is at position len(s) TRUE
#     [Explanation: p. 131 "Notice that in a string of n characters, the last character is at position
#     n -1, because the index starts at 0. "]

#  3. A string always contains a single line of text. FALSE
#     [Explanation: A string is a sequence of characters. This sequence can be of any length. In fact,
#     it is also possible to have an empty string, i.e. "".]

#  4. In Python, "4" + "5" is "45". TRUE
#     [Explanation: This is not a a case of using the addition operator on integers. Since the literals are
#     enclosed in double quotations, we know that we are dealing with values of the data type string. The
#     operator + thus indicates the string operation, concatenation.]

#  5. Python lists are mutable, but strings are not. TRUE
#     [Explanation: p.138 "While strings and lists are both sequences, there is an important difference
#     between the two. Lists are mutable. That means that the value of an item in a list can be modified
#     with an assignment statement. Strings, on the other hand, cannot be changed 'in place.'"]

#  6. ASCII is a standard from representing characters using numeric codes. TRUE
#     [Explanation: p.140 "To avoid this sort of problem, computer systems today use industry standard
#     encodings. One important standard is called ASCII (American Standard Code for Information Interchange).
#     ASCII uses the numbers 0 through 127 to represent characters typically found on an (American) computer
#     keyboard, as well as certain special values known as control codds that are used to coordinate the sending
#     and receiving of information.]

#  7. The split method breaks a string into a list of substrings, and join does the opposite. FALSE
#     [Explanation: p.144 "For our decoder, we will make use of the split method. This method splits a string into
#     a list of substrings. By default, it will split the string whever a space occurs. p. 148 see table.]

#  8. A substitution cipher is a good way to keep sensitive information secure. FALSE
#     [Explanation: p.150 "Our simple encoding/decoding programs use a very weak form of encryption known as a
#     substituation cipher....Since each letter is always encoded by the same symbol, a codebreaker coud use
#     statistical inofrmation about the frequency of various letters and some simple trial and error testing to
#     discover the original message."]

#  9. The add method can be used to add an item to the end of a list. FALSE
#     [Explanation: p.147 "The append method can be used to add an item at the end of a list. This is often used to
#     build a list an item at a time.]

# 10. The process of associating a file with an object in a program is called "reading" the file. FALSE
#     [Explanation: p.159 "We need some way to associate a file on disk with an object in a program. This process
#     is called opening a file. Once a file has been opened, its contents can be accessed through the associated
#     file object.]

## Multiple Choice

#  1. Accessing a single character out of a string is called: [D]
#     a) slicing     b) concatenation     c) assignment     d) indexing

#  2. Which of the following is the same as s[0:-1] [C]
#     a) s[-1]     b) s[:]     c) s[:len(s)-1]     d) s[0:1len(s)]

#  3. What function gives the Unicode value of a character? [A]
#     a) ord     b) ascii     c) chr     d) eval
#     [Explanation p.140 "Python provides a couple of built-in functions that allow us to switch back
#     and forth between characters and the numberic values used to represent them in strings. The ord
#     function returns the numeric ("ordinal") code of a single-character string, while chr goes the
#     other direction."]

#  4. Which of the following can not be used to convert a string of digits into a number? [D]
#     a) int     b) float     c) str     d) eval

#  5. A sucessor to ASCII that includes characters from (nearly) all written languages is [C]
#     a) TELLI     b) ASCII+ +     c) Unicode     d) ISO
#     [Explanation: p.140 "Most modern systems are moving to Unicode, a much larger standard that
#     aims to include the characters of nearly all written languages."]

#  6. Which string method converts all the characters of a string to upper case? [D]
#     a) capitalize     b) capwords     c) uppercase     d) upper
#     [Explanation: p.147 see example. p.148: see table.]

#  7. The string "slots that are filled in by the format method are marked by: [D]
#     a) %     b) $     c) []     d) {}
#     [Explanation: p.156 "Curly braces ({}) inside the template-string mark 'slots' into which the
#     provided values are inserted. The information inside the curly braces tells which value goes in
#     the slot and how the value should be formatted.]

#  8. Which of the following is not a file-reading method in Python? [C]
#     a) read     b) readline     c) readall     d) readlines
#     [Explanation: p.161 "Python provides three related operations for reading information from a
#     file [read, readline, readlines]."]

#  9. The term for a program that does its input and output with files is [C]
#     a) file-oriented     b) multi-line     c) batch     d) lame

# 10. Before reading or writing to a file, a file object must be created via
#     a) open     b) create     c) File     d) Folder


## Discussion

#  1. Given the initial statements:
#
#     s1 = "spam"
#     s2 = "ni!"
#
#     Show the result of evaluating each of the following string expressions.
#                                        Expected                   | Actual
#     a) "The Knights who say, " + s2    The Knights who say ni!    |
#     b) 3 * s1 + 2 * s2                 spamspamspamni!ni!         |
#     c) s1[1]                           pam                        |
#     d) s1[1:3]                         pam                        | 
#     e) s1[2] + s2[:2]                  aspa                       |
#     f) s1 + s2[-1]                     spam!                      |
#     g) s1.upper()                      SPAM                       | 
#     h) s2.upper().1just(4) * 3         ?

#  2. Given the same initial statements as in the previous problem, show a Python expression that
#     that could construct each of the following results by performing string operations on s1 and s2.

#     a) "NI"
#     b) "ni!spamni!"
#     c) "Spam Ni! Spam Ni! Spam Ni!"
#     d) "spam"
#     e) ["sp","m"]
#     f) "spm"

#  3. Show the output that would be generated by each of the following program fragments.

#     a) for ch in "aardvark":
#            print(ch)

#     b) for w in "Now is the winter of our discontent...".split():
#            print(w)

#     c) for w in "Mississippi".split("i"):
#            print(w, end=" ")

#     d) msg = ""
#        for s in "secret".split("e"):
#            msg = msg + s

#     e) msg = ""
#        for ch in "secret":
#        msg = msg + chr(ord(ch)+1)
#        print(msg)

#  4. Show the string that would result from each of the following string formatting operations. If the
#     operation is not legal, explain why:

#     a) "Looks like (1) and (0) for breakfast".format("eggs", "spam")

#     b) "There is {0} {1} {2} {3}".format(1, "spam", 4 "you")

#     c) "Hello {0}".format("Susan", "Computewell")

#     d) "{0:0.2f} {0:0.2f}".format(2.3, 2.3468)

#     e) "{7.5f} {7.5f}".format(2.3, 2.3468)

#     f) "Time left {0:02}:{1:05.2f}".format(1, 37.374)

#     g) "{1:3}".format("14")


#  5. Explain why public key encryption is more useful for securing commmunications on the Internet than
#     private (shared) key encryption.


### PROGRAMMING EXERCISES

#  1. The example code files for Chapter 5 include a date conversion program, dateconvert2.py. This program could be
#     simplified with string formatting. Modify the program to use the string format method for its output.

#  2. A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a
#     program that accepts a quiz score as an input and prints out the corresponding grade.

#  3. A certain CS provessor gives 100-point exams that are graded on the cale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#     Write a program that accepts an exam xcore as input and prints out the corresponding grade.

#  4. An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For
#     example, RAM is an acronym for "random access memory." Write a program that allows the user to type in a phrase and
#     then outputs the acronym for that phrase. Note: The acronym should be all uppercase, even if the words in the phrase
#     are not capitalized.

#  5. Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name. The value
#     of a name is determined by summing up the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3, up to "z"
#     being 26. For example, the name "Zelle" would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#     auspicious number, by the way). Write a program that calculates the numeric value of a single name provided as input.

#  6. Expand your soluation to the previous problem to allow the calcualtion of a complete name such as "John Marvin Zelle" or
#     "John Jacob Jingleheimer Smith." The total value is just the sum of the numberic values of all the names.

#  7. A Caesar cipher is a simple substitution sipher based on the diea of shifting each letter of the plaintext message a fixed
#     number (called the key) of positions in the alphabet. For example, if the key is 2, the word "Sourpuss" would be encoded as
#     "Uqwtrwuu." The original message can be recovered by "reencoding" it using the negative of the key.
#
#     Write a program that can enconde and decode Caesar ciphers. The input to the progrma will be a string of plaintext and the
#     value of the key. The output will be an encoded message where each character in the original message is replaced by shifting
#     it key characters in the Unicode character set. For exmaple, if ch is a character in the string and key is the amount to shift,
#     then the character that replaces ch can be calculated as: chr(ord(ch) + key).

#  8. One problem with the previous exercise is that it does not deal with the case when we "drop off the end" of the alphabet. A
#     true Caesar cipher does the shifting in a circular fashion where the next character after "z" is "a." Modify your solution
#     to the previous problem to make it circular. You may assume that the input consists only of letters and paces.
#     Hint: Make a string containing all the cahracters of your alphabet and use positions in this string as your code. You do not
#     have to shift "z" int "a"; jsut make sure that you use a circular shift over the entire sequence of characters in your alphabet
#     string.

#     Note to self: modular.

#  9. Write a program that counts the number of words in a sentence entered by the user.

# 10. WRite a program that calculates the average word length in a sentence entered by the user.
 
# 11. Write an improved version of the chaos.py program from Chapter 1 that allows a user to input two initial values and the number of
#     of iterations, and then prints a nicely formatted table showing how the values change over time. For example, if the starting
#     values were .25 and .26 with 10 iterations, the table might look like this:

#     index    0.25         0.26
#     ----------------------------
#       1    0.731250     0.750360
#       2    0.766441     0.730547
#       3    0.698135     0.767707
#       4    0.821896     0.695499
#       5    0.570894     0.825942
#       6    0.955399     0.560671
#       7    0.166187     0.960644
#       8    0.540418     0.147447
#       9    0.968629     0.490255
#      10    0.118509     0.974630

# 12. Write an imroved version fo the futval.py program from Chapter 2.
#     Your program will prompt the user for the amoutn of the investment, the annualized interest rate, and the number of years of the
#     investment. The program will then output a nicely formatted table taht tracks the value of the investment year by year. Your
#     output might look something like this:
#
#     Year     Value
#     ________________
#       0     $2000.00
#       1     $2200.00
#       2     $2420.00
#       3     $2662.00
#       4     $2928.20
#       5     $3221.02
#       6     $3542.12
#       7     $3897.43

# 13. Redo any of the previous programming exercises to make hem batch-oriented (using text files for input and output).

# 14. Word Count. A common utility on Unix/Linux systems is a small program called "wc." This program analyzes a file to determine the
#     number of lines, words and characters contained therein. Write your own verison of wc. The program should accept a file name as
#     input and then print three numbers showing the count of lines, words, and characters in the file.

# 15. Write a program to plot a horizontal bary chart of studnet exam scores. Your program should get input from a file. The first line
#     of the file contains the count of the number of students in the file, and eah subsequent line contains a student's last name
#     followed by a score in the range 0-100. Your program should draw a horizontal rectangle for each student where the length of the
#     bar represents the student's score. The bars should all line up on their left-hand edges.
#     Hint: Use the number of students to determine the size of the window and its coordinates. [Note to self: point of control.]
#     Bonus: lable the bars at the left with the students' names.

# 16. Write a program to draw a quiz score histogram. Your program should read data from a file. Each line of the file contains a number
#     in the range 0-10. Your program must count the number of occurences of each score and then draw a vertical bar char with a bar for
#     each possible score (0-10) with height corresponding to the count of that score. For example, if 15 students got an 8, then the
#     the height of the for 8 should be 15.
#     Hint: Use a list that stores the count for each possible score.
