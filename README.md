# Python Program to Extract Even and Odd Numbers from a Text File
This Python script creates the text files even.txt and odd.txt after analyzing the 20 integers in the numbers.txt text file. odd.txt will have all the odd numbers collected from numbers.txt, and even.txt will include all the even numbers.

## Usage 
1. Open the Start menu and search for "Command Prompt".
2. Click on "Command Prompt" to open the command prompt window.
3. Use the cd command to navigate to the directory containing the script file. For example, if the script file is located in the "Documents" folder, type: cd Documents
4. Type the command python script_name.py to run the script. Replace "script_name.py" with the actual name of the script file.
5. Press Enter to run the script.
6. After the script completes, two output files named "even.txt" and "odd.txt" will be created in the same directory as the script file.

Alternatively, you can also run the script using the Python IDLE environment:

1. Open the Start menu and search for "Python".
2. Click on "Python" to open the Python IDLE environment.
3. Click on "File" at the top of the window and select "Open".
4. Navigate to the directory containing the script file and select it.
5. Click on "Run" at the top of the window and select "Run Module" or press the F5 key.
6. After the script completes, two output files named "even.txt" and "odd.txt" will be created in the same directory as the script file.

## Example

Suppose numbers.txt contains the following integers:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233816828-6c93e856-5097-4cbb-a53a-3610ddbb17e4.png">

The script will create even.txt containing:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233816786-b877dbb1-5e32-4ee2-b981-93ed5b279705.png">

And odd.txt containing:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233816802-2523a069-bbce-4603-ba56-1d517853e34d.png">

Note: If the `numbers.txt` file doesn't exist or doesn't contain any integers, the program will raise an error.

## Code Explanation 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233816913-06ac45d0-4abb-43d3-a6e3-9da92562d54d.png">

The script first opens the input file using the open function with the 'r' mode, which allows it to read the contents of the file. The with statement ensures that the file is properly closed after use.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233816974-b35c253b-5452-4554-846c-8052192edb68.png">

Next, the script reads all lines from the file using the readlines method, and converts them to integers using a list comprehension. The strip method removes any leading or trailing whitespace from each line.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233817004-688e5b55-f4de-46e5-9410-f28aa2b370ad.png">

Then, two empty lists are created to store the even and odd numbers, respectively. The script iterates through all numbers in the input list, and checks if each number is even or odd using the modulus operator %. If the remainder of dividing the number by 2 is 0, it is an even number and is appended to the even_numbers list. Otherwise, it is an odd number and is appended to the odd_numbers list.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/233817273-2a8a6304-03ec-45a1-a2e7-4803f6ad0a90.png">

Finally, the script opens two output files, 'even.txt' and 'odd.txt', using the open function with the 'w' mode, which allows it to write to the files. The with statement ensures that the files are properly closed after use. 

The script writes the even numbers to 'even.txt' using the write method, joined by newlines using the join method and the map function, which converts each integer to a string using the str function. 

The script writes the odd numbers to 'odd.txt' using the same method.

## Potential Improvements 
- The script assumes that the input file contains only integers, one per line. It could be improved to handle other formats or provide more informative error messages. 
- If the input file is very large, the script may run out of memory trying to read all lines at once. A more memory-efficient approach could be to read the file one line at a time using a for loop and process each line as it is read. 
- The script could be modified to take the input and output file names as command-line arguments, allowing the user to specify different files if desired.

## Conclusion 
This script demonstrates a simple way to separate even and odd numbers from a list of integers. By reading from an input file and writing to separate output files, it can handle large amounts of data without running out of memory. With some modifications, it could be adapted to handle other types of data or provide more advanced functionality.
