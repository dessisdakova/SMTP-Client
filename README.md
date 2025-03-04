## A Python email client that allows sending and retrieving emails. 

### Utilizes two fundamental email protocols:
* SMTP (Simple Mail Transfer Procol)
* IMAP (Internet Message Access Protocol)

### Libraries and usage:
- ```smtplib``` - Python’s built-in library to interact with an SMTP server. It establishes a secure connection to the server, performs login and sends the email.

- ```imaplib``` - Python's built-in library to connect to an IMAP server. It establishes a secure connection to the server, performs login, selects preferred mailbox, searches for emails based on criteria and fetches an email using its ID.

- ```email``` - Python's built-in library to handle emails and their formats. Implements two main standards for email:

    - **RFC (Request for Comments)** – technical documents that define the structure of email headers.

    - **MIME (Multipurpose Internet Mail Extension)** - standards that enable emails to carry more than just plain text (multimedia, other emails)

    Used to construct an email into the appropriate format that an SMTP server expects and to parse an email, retrieved from an IMAP server, into a “Message” object Python can work with. 

### Gmail's SMTP server
SSL (Secure Sockets Layer) is an older technology that contains some security flaws. TLS (Transport Layer Security) is the upgraded version of SSL that fixes existing SSL vulnerabilities.

- port **465** for SSL (implicit) using ```smtplib.SMTP_SSL``` - The client and server perform the SSL/TLS handshake immediately after the connection is established.

- port **587** for TLS (explicit) using ```smtplib.SMTP``` with ```server.starttls()``` - The connection to the SMTP server is initially established as a plain, unencrypted connection. The client sends a command to the server requesting it to switch to TLS. The server and client then perform a TLS handshake to establish a secure channel.


