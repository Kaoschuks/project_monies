"""
A script responsible for parsing bank statement files, specifically for
Santander text files, and visualising where the money is being used to
better understand where it can be saved.
"""


def parse(data):
    """
    Parses the input of the Santander .txt file into CSV format.

    The format of the bank statement is as follows:

       "From: <date> to <date>"

       "Account: <number>"

       "Date: <date>"
       "Description: <description>"
       "Amount: <amount>"
       "Balance: <amount>"

        <second_transaction_entry>

    :param data: A list containing each line of the bank statement.
    :return: A list containing parsed entries in CSV format.
    """
    sep = 5 * " "

    # Skip headers
    data = data[4:]

    # Remove empty lines
    data = [d.strip() for d in data]
    data = list(filter(None, data))

    # Removing field descriptions
    for i, d in enumerate(data):
        if d.startswith("Date"):
            data[i] = d.replace("Date: ", "").strip()

        if d.startswith("Description"):
            data[i] = d.replace("Description: ", "").strip()

        if d.startswith("Amount"):
            data[i] = d.replace("Amount: ", "").replace(" GBP", "").strip()

        if d.startswith("Balance"):
            data[i] = d.replace("Balance: ", "").replace(" GBP", "").strip()

    # Builds CSV string
    entries = [data[d:d+4] for d in range(0, len(data), 4)]
    entries = [sep.join(e) for e in entries]
    entries = "\n".join(entries)

    return entries


def parseFile(iPath, oPath):
    """
    Parses the file for the given path into CSV format (it is assumed the
    file is a Santander .txt file with ISO-8859-1 encoding).

    :param iPath: The path to the input text file.
    :param oPath: The path to the output csv file.
    """
    with open(iPath, "r", encoding="ISO-8859-1") as i, \
         open(oPath, "w", encoding="UTF-8") as o:

        # Replacing non-breaking space in Latin1 with a UTF-8 space
        ls = i.readlines()
        ls = [l.replace("\xa0", " ") for l in ls]

        o.write(parse(ls))
