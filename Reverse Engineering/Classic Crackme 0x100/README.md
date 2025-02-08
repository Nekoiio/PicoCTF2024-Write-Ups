# Challenge: Classic Crackme 0x100

## Overview
For the Classic Crackme 0x100 challenge, I needed to find a password to decrypt a hidden message. The binary provided encrypted user input and compared it to a stored value to determine if the correct password had been entered.

## Steps Taken
1. **Initial Analysis:** I began by analyzing the binary in Ghidra. The disassembly revealed an encryption algorithm and a comparison with a variable called `local_68`. Although the algorithm wasn't immediately clear, further investigation was required.

2. **Encryption Algorithm:** After understanding the encryption algorithm, I realized that `local_68`, along with other declared variables, formed the password or the expected value. These variables were part of a single string.

3. **Debugger (GDB):** I then ran the program in GDB. Setting a breakpoint before the `memcmp` function call allowed me to observe the value it was comparing the user input to. By entering various inputs and analyzing the transformation, I discerned a pattern.

4. **Character Offset:** I noticed that each character in the decrypted string was a certain offset away from the corresponding character in the encrypted string. This offset was consistent and could be calculated by comparing the difference in Unicode values of characters.

5. **Automated Script:** To automate the process, I wrote a Python script. The script calculated the offset for each character by spamming a specific character (e.g., 'a') and comparing the encrypted and decrypted values. It then applied this offset to the expected output to obtain the correct password.

6. **Completion:** With the correct password obtained, I entered it into the challenge, and successfully obtained the flag.

