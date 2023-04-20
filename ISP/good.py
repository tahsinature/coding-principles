# Good example following ISP

class Printer:
  def print(self, document):
    raise NotImplementedError("print() method must be implemented in concrete classes")


class Fax:
  def fax(self, document):
    raise NotImplementedError("fax() method must be implemented in concrete classes")


class Scanner:
  def scan(self, document):
    raise NotImplementedError("scan() method must be implemented in concrete classes")


class MultifunctionalPrinter(Printer, Fax, Scanner):
  def print(self, document):
    print("Printing document:", document)

  def fax(self, document):
    print("Faxing document:", document)

  def scan(self, document):
    print("Scanning document:", document)
