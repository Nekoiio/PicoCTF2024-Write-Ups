# After looking through binary, noticed it was packed with UPX.
1. -- Download UPX --
2. Unpack binary with `upx -d`.
3. Search strings in Ghidra for `password` as it appears near/in the logic in scope.
4. Patch instruction to *reverse the logic of if statement* that skips flag print.
5. Export & run.
6. Flag in hex | Use CyberChef.
## Done!
