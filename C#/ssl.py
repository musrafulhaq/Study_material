import OpenSSL
import ssl
cert=ssl.get_server_certificate(('www.google.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
x509.get_notAfter()


https://www.activestate.com/blog/how-to-manage-tls-certificate-expiration-with-python/    




















