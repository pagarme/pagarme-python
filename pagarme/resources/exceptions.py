# encoding: utf-8

class PagarmeApiError(Exception): pass

class PagarmeTransactionError(Exception): pass

class NotPaidException(PagarmeTransactionError): pass

class NotBoundException(PagarmeTransactionError): pass