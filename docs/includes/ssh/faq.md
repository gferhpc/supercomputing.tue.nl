??? question "I'm getting a "Server is unreachable" error message."

    If the server is unreachable, verify your network connection and ensure you are connected to the TU/e VPN, 
    and check for any restrictions on port 22, which is used for SSH.

??? question "I'm a getting a "Permission denied" error message."

    If you encounter a "Permission denied" message, verify the following:
    
    - Ensure your public key is in the server's `authorized_keys` file.
    - Check that correct permissions are set on the server's `.ssh` directory (700) and `authorized_keys` file (600).

??? question "My passphrase isn't remembered and have to re-enter it everytime."

    Ensure that your private key is accessible. Use the following command to add your key to the SSH agent if needed:

    ```bash
    ssh-add /Users/yourusername/.ssh/id_rsa
    ```

    !!! info
        
        Keep in mind that after system reboots, you will need to add your key back to the SSH agent using the command mentioned above.
