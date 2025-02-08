The answer here was very helpful:
https://stackoverflow.com/questions/701624/difference-between-big-endian-and-little-endian-byte-order

For the most part this can be done using an ascii to hex converter, just pay attention to what the first character is, if the first character corresponds to the ascii code for the first letter, then the output of the converter is in BE notation, just reverse the mirror the hex pairs, without changing the order inside of a pair.
