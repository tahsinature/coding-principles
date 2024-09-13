# Bad example violating ISP

class Printer:
  def print(self, document):
    raise NotImplementedError("print() method must be implemented in concrete classes")

  def fax(self, document):
    raise NotImplementedError("fax() method must be implemented in concrete classes")

  def scan(self, document):
    raise NotImplementedError("scan() method must be implemented in concrete classes")


class MultifunctionalPrinter(Printer):
  def print(self, document):
    print("Printing document:", document)

  def fax(self, document):
    print("Faxing document:", document)

  def scan(self, document):
    print("Scanning document:", document)
