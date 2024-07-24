import os, sys

DECRYPT_KEY = "7e951795cf4cd9942405eeb5f00077cbe35490c2e08d9932d1c2e89f76b56e84"


def malware_complete():
    pass


def malware_current_folder():
    os.getcwd()
    files = [entry for entry in os.listdir('.') if os.path.isfile(os.path.join('.', entry))]


if __name__ == "__main__":
    pass
