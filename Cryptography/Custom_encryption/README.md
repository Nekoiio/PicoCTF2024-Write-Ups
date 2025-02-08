# Cryptography Problem: Encryption and Decryption

## Overview
This project involves implementing encryption and decryption algorithms using a shared key. The encryption algorithm involves dynamic XOR encryption, while the decryption algorithm reverses the encryption process.

## Encryption Algorithm
The encryption algorithm works as follows:
1. Generate two random numbers `a` and `b`.
2. Check if `a` and `b` are prime numbers. If not, prompt the user to enter prime numbers.
3. Calculate `u` and `v` using a generator function with the given prime numbers.
4. Calculate the shared key `key` using the generator function and `a`, and `b`.
5. Encrypt the plaintext using dynamic XOR encryption with the shared key.
6. Encrypt each character of the plaintext using a modified approach: `(ord(char) * key * 311)`.

## Decryption Algorithm
The decryption algorithm reverses the encryption process:
1. Decrypt each character of the cipher text using a reverse approach: `(char(i / (key * 311)))`.
2. Perform dynamic XOR again using the same shared key to recover the original plaintext.
3. Reverse the decrypted text to get it in the correct order.
