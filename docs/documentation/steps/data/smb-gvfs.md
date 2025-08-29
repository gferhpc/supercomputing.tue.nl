# Windows file shares (gvfs)

!!! warning

    This is currently in development and may not work yet.  To receive updates,
    please leave a comment below this page.

## Connecting

1.  [Connect](../access/index.md) to any of the cluster's login nodes.

2.  Connect to the Windows file share using the following command:
    ```
    gio mount smb://<server>/<share>
    ```
    Then, enter your username and password when prompted:
    ```
    Authentication Required
    Enter user and password for share “software” on “fs-cmp-op01.campus.tue.nl”:
    User [guus]: <username>
    Domain [WORKGROUP]: CAMPUS.TUE.NL
    Password: <password>
    ```
    Be sure to enter `CAMPUS.TUE.NL` when asked for the domain.

3.  Get the path at which this share is mounted by running the following command:
    ```
    gio info smb://<server>/<share> | grep ^local
    ```

## Navigating the Windows file share

To browse the Windows file share, you can simply `cd` to the "local path" that
you obtained in step 3 above.

Moving, copying, and removing files on the Windows file share can be done using
standard Linux tools such as `mv`, `cp`, and `rm`.

## Disconnecting

1.  Run the following command:
    ```
    gio mount -u smb://<server>/<share>
    ```
