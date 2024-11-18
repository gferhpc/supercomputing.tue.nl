---
title: 3. Transfer Data
---

# Transfer Data

## Transferring data

Here are the steps to transfer files from a Windows machine to an SSH server like `hpc.tue.nl` using **SCP** or **MobaXterm**:

### **Method 1: Using SCP (via Command Prompt or PowerShell)**

1. **Ensure SSH and SCP are Installed**:
    - Windows 10 and later include OpenSSH by default. Check by typing `ssh` or `scp` in the Command Prompt or PowerShell.
    - If not installed, install OpenSSH from Windows settings under "Apps > Optional Features."

2. **Identify Your Files and Destination**:
    - **Source file**: Know the full path of the file you want to transfer, e.g., `C:\Users\YourName\Documents\example.txt`.
    - **Destination path**: Determine the destination folder on the server, e.g., `/home/yourusername/`.

3. **Open PowerShell or Command Prompt**:
    - Press `Win + R`, type `cmd` or `powershell`, and hit Enter.

4. **Run the SCP Command**:
   Use the following syntax:
   ```bash
   scp <local-file-path> <username>@hpc.tue.nl:<remote-directory>
   ```
   Example:
   ```bash
   scp C:\Users\YourName\Documents\example.txt yourusername@hpc.tue.nl:/home/yourusername/
   ```

5. **Authenticate**:
    - Enter your password when prompted.
    - You may be asked to confirm the server's fingerprint the first time you connect.

6. **Verify the Transfer**:
    - Log in to the server using SSH (`ssh yourusername@hpc.tue.nl`) and navigate to the target directory (`cd /home/yourusername`) to confirm the file is there.

---

### **Method 2: Using MobaXterm**

1. **Download and Install MobaXterm**:
    - Download from the [MobaXterm website](https://mobaxterm.mobatek.net/).
    - Install the free version if you don't already have it.

2. **Connect to the Server**:
    - Open MobaXterm and click on **Session > SSH**.
    - Fill in:
        - **Remote host**: `hpc.tue.nl`
        - **Username**: Your HPC username
    - Click **OK** and log in with your password.

3. **Enable the File Browser**:
    - Once connected, MobaXterm will automatically open a **file explorer** on the left-hand side.
    - This shows your remote server's directories.

4. **Transfer Files**:
    - Drag and drop files from your Windows file explorer to the desired location in MobaXterm's file explorer.
    - Alternatively, right-click on the remote directory in MobaXterm and use the **Upload** option to select files.

5. **Verify the Transfer**:
    - Use the file explorer or the terminal in MobaXterm to navigate and check if the file is transferred successfully.

---

## **Tips**:
- For SCP, if you need to transfer a directory, use the `-r` flag:
  ```bash
  scp -r <local-directory> <username>@hpc.tue.nl:<remote-directory>
  ```
- For large files, MobaXterm provides an easier interface and progress display compared to SCP.
- Ensure your firewall settings allow outgoing SSH connections (port 22).
- If you encounter permission issues on the server, contact your system administrator.
