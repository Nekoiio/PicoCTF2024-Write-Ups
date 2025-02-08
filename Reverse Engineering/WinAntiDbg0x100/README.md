# Solving WinAntiDbg0x100 Challenge

## Description

The WinAntiDbg0x100 challenge is designed to test your ability to bypass anti-debugging techniques in a Windows executable. The program prompts you to run it with a debugger, which will cause it to crash. To solve the challenge, you need to either place breakpoints on every jump or try to change the jump logic.

## Solution

1. **Run the Program**: Start by running the executable from the command line or PowerShell.

2. **Debugging the Program**:
   - Attach a debugger (e.g., x64dbg, OllyDbg, or IDA Pro) to the running process.
   - Place breakpoints on every jump instruction or try to alter the jump logic to bypass anti-debugging checks.

3. **Finding the Flag**:
   - After successfully bypassing the anti-debugging checks, let the program run until it prints the flag.
   - Look for the flag in the program's output or memory. You can also check the IDA Pro debug console for any additional hints or information.

4. **Completing the Challenge**:
   - Once you have found the flag, make sure to place a breakpoint after the flag is printed to prevent the program from closing automatically.
   - Capture the flag and submit it to complete the challenge.
