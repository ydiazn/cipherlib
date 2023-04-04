class BaseCipher:

    def __init__(self, key):
        """Initialize instance.
        Args:
            key (str): secret key
        """
        self.key = key

    def encrypt(self, text):
        """Encrypt a clear text.
        Args:
            text (str): clear text
        Returns:
            str: encrypted text
        """
        raise NotImplementedError

    def decrypt(self, text):
        """Decrypt an encrypted text.
        Args:
            text (str): clear text
        Returns:
            str: encrypted text
        """
        raise NotImplementedError
