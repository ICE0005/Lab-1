{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c7f5c0ca-d65d-4be8-bf19-23c552bbceb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the filename:  test1.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Number of lines in the file: 5\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a line number (1-5) or 0 to quit:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Line 3: asdgfasfdas\n",
      "\n",
      "Number of lines in the file: 5\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a line number (1-5) or 0 to quit:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quitting the program.\n"
     ]
    }
   ],
   "source": [
    "def read_file_lines(filename):\n",
    "    try:\n",
    "        with open(filename, 'r') as file:\n",
    "            return file.readlines()\n",
    "    except FileNotFoundError:\n",
    "        print(f\"Error: File '{filename}' not found.\")\n",
    "        return None\n",
    "\n",
    "def main():\n",
    "    # Prompt the user for a filename\n",
    "    filename = input(\"Enter the filename: \")\n",
    "    \n",
    "    # Read the lines from the file\n",
    "    lines = read_file_lines(filename)\n",
    "    \n",
    "    if lines is None:\n",
    "        return\n",
    "    \n",
    "    # Remove newline characters from the end of each line\n",
    "    lines = [line.strip() for line in lines]\n",
    "    \n",
    "    # Get the number of lines in the file\n",
    "    num_lines = len(lines)\n",
    "    \n",
    "    while True:\n",
    "        # Print the number of lines in the file\n",
    "        print(f\"\\nNumber of lines in the file: {num_lines}\")\n",
    "        \n",
    "        # Prompt the user for a line number\n",
    "        try:\n",
    "            line_number = int(input(\"Enter a line number (1-{}) or 0 to quit: \".format(num_lines)))\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a number.\")\n",
    "            continue\n",
    "        \n",
    "        # Check if the user wants to quit\n",
    "        if line_number == 0:\n",
    "            print(\"Quitting the program.\")\n",
    "            break\n",
    "        \n",
    "        # Check if the line number is valid\n",
    "        if 1 <= line_number <= num_lines:\n",
    "            print(f\"Line {line_number}: {lines[line_number - 1]}\")\n",
    "        else:\n",
    "            print(f\"Invalid line number. Please enter a number between 1 and {num_lines}.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "721948a5-0a9a-437c-9624-11c96494f4b4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
