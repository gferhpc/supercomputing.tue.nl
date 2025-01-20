# Frequently Asked Questions

## Account

??? question "How do I request an account?"

    To request an account please check the [Request Access](steps/request/index.md) documentation.

??? question "What should I do if I forget my password?"

    Your account and password is directly linked to the TU/e login. Please follow the reset instructions on 
    [login.microsoftonline.com](https://login.microsoftonline.com/){:target=_blank}.

??? question "How do I close my account?"

    You can request account removal by [creating a TopDesk ticket](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=a745121fa0ab45f2b24aaaf64060760f){:target=_blank}.
    
    !!! danger ""
    
        Be aware that all data linked to your account will be removed and can't be recovered. Please make backups 
        accordingly. If you decide that to request an account again in the future you won't have access to your old data. 

??? question "What should I do if I notice unauthorized activity on my account?"

    Report suspicious activity immediately by following these instructions and take additional steps to secure your account.

??? question "How can I change my account password?"

    Find out how to create a new password safely and securely.

??? question "What should I do if I'm having trouble logging into my account?"

    Use these troubleshooting tips for login issues and learn how to contact support if needed.

??? question "How do I know if my account is set to expire?"

    Check account expiration dates and learn about notifications you might receive.

??? question "What happens when my account expires?"

    Understand what occurs post-expiration, like loss of access, data deletion, or service suspension.

??? question "How can I extend or renew my account before it expires?"

    Extend or renew your account by following these steps, including any fees or actions required.

??? question "Can I reactivate my expired account?"

    Yes, you can reactivate your expired account. However, please note that once an account expires, it is deleted along 
    with all its data. This means that when you reactivate, you'll be starting with a completely new account that has no 
    previous data.

??? question "What are the options for automatic account renewal?"

    We don't support automatic account renewals. Please extend your account timely.

## SSH

??? question "What is SSH and why is it used?"

    SSH (Secure Shell) is a protocol used to securely connect to remote systems over a network. It facilitates encrypted communication between the client and server, commonly used for remote server administration and file transfers.

??? question "Why am I getting 'Connection refused' when trying to SSH into a server?"

    This error often indicates network connectivity issues. Ensure you're connected to the campus network or use a VPN if off-campus to access `hpc.tue.nl`.

    - **Windows (MobaXterm/OpenSSH)**: Verify your VPN connection and network adapter settings.
    - **Linux/MacOS**: Check your VPN connection and use `ping hpc.tue.nl` to ensure the server is reachable.

??? question "What should I do if I encounter 'Permission denied' errors during SSH connection?"

    "Permission denied" usually indicates authentication issues. Ensure the correct TU/e network login name is used as the username, never an email address.

    - **Windows (MobaXterm)**: Verify login credentials and key settings under the "SSH" tab.
    - **Windows (OpenSSH), Linux, MacOS**: Make sure the username is correct and check that your `~/.ssh/authorized_keys` setup is accurate and permissions are set correctly (`private key: 600`, `public key: 644`).

??? question "How can I resolve 'Host key verification failed'?"

    This error suggests a mismatch in known host keys.

    - **Windows (MobaXterm)**: Navigate to `Settings` > `Configuration` > `SSH` for host key management.
    - **Windows (OpenSSH), Linux, MacOS**: Edit or remove the conflicting entry in the `~/.ssh/known_hosts` file. Use `ssh-keygen -R hpc.tue.nl` to remove the host entry.

??? question "SSH is taking too long to connect. How can I fix this?"

    Slow connections can be due to DNS or network latency.

    - **Windows (MobaXterm)**: Disable DNS lookup under session settings or preferences.
    - **Windows (OpenSSH), Linux, MacOS**: Use `ssh -o "GSSAPIAuthentication no" user@hpc.tue.nl` and ensure a stable VPN.

??? question "Why is my SSH session disconnecting frequently?"

    Disconnections may result from network instability.

    - **Windows (MobaXterm)**: Enable keepalives in `Settings` to maintain session stability.
    - **Windows (OpenSSH), Linux, MacOS**: Add `ServerAliveInterval 60` to your `~/.ssh/config` file for frequent keepalives.

??? question "How do I enable verbose logging for SSH to debug issues?"

    Use verbosity to obtain detailed connection logs:

    - **Windows (MobaXterm)**: Enable verbose logging via `Session Settings -> Advanced SSH settings`.
    - **Windows (OpenSSH), Linux, MacOS**: Use `ssh -vvv user@hpc.tue.nl` for increased verbosity.

??? question "What can I do if 'Connection timed out' occurs?"

    Ensure stable network and SSH port access:

    - **Windows (MobaXterm/OpenSSH)**: Check firewall exceptions and VPN connection.
    - **Linux/MacOS**: Examine firewall settings and verify VPN connectivity.

??? question "How to fix 'Too many authentication failures' error?"

    Too many keys may be attempted:

    - **Windows (MobaXterm)**: Limit the keys offered by configuring the "SSH" session settings.
    - **Windows (OpenSSH), Linux, MacOS**: Use `ssh -i /path/to/private_key user@hpc.tue.nl` to specify a specific identity file and set `IdentitiesOnly yes` in the `~/.ssh/config`.

??? question "Can I connect to an SSH server using a different port?"

    No. For `hpc.tue.nl` use the default port `22`.