# RSA-API

Built with Python 3.8 and Flask

# Setup:

You will need to import flask and run a local server on port 5000

This is a really simple RSA API it has three endpoints:

# [GET] /keygen

Generates PUBLIC KEY, PRIVATE KEY and N, you will need this tokens to encrypt and decrypt messages.

# [GET] /encrypt

It ciphers a given message (str). For this endpoint to work you will need the following params:

* public:   The public key generated with /keygen
* N:        The product of public * private
* msg:      The message that you want to encrypt as str

# [GET] /decrypt

It deciphers a given message (str). For this endpoint to work you will need the following params:

* private:  The private key generated with /keygen
* N:        The product of public * private
* msg:      The message that you want to decrypt as str

