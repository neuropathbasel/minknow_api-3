### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
import minknow_api
from minknow_api.keystore_pb2_grpc import *
import minknow_api.keystore_pb2 as keystore_pb2
from minknow_api.keystore_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging
import sys

__all__ = [
    "KeyStoreService",
    "StoreRequest",
    "StoreResponse",
    "RemoveRequest",
    "RemoveResponse",
    "GetOneRequest",
    "GetOneResponse",
    "GetRequest",
    "GetResponse",
    "WatchRequest",
    "WatchResponse",
    "Lifetime",
    "UNTIL_NEXT_PROTOCOL_START",
    "UNTIL_PROTOCOL_END",
    "UNTIL_INSTANCE_END",
    "PERSIST_ACROSS_RESTARTS",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class KeyStoreService(object):
    """Allows arbitrary data to be associated with this MinKNOW instance.

    This can be used by the protocol to communicate information to the outside world (including a
    user interface), for example.

    Value names should be stored in the form <product>:<name>, where <product> is the name of the
    product that has decided what form the value should take (generally either the software that is
    setting the value, or the software that is consuming it).

    In particular, the prefixes "minknow:", "bream:", "protocol:" and "gui:" are reserved for MinKNOW
    and the software that ships with MinKNOW. Names starting with ":" are also reserved for
    "well-known" values that will be listed in this or related documentation."""
    def __init__(self, channel):
        self._stub = KeyStoreServiceStub(channel)
        self._pb = keystore_pb2
    def store(self, _message=None, _timeout=None, **kwargs):
        """Store one or more values.

        Anyone watching those values will be notified of the change. If they are watching several of
        the values in a single watch() call, all the updates will be sent in a single message.

        

        Args:
            _message (minknow_api.keystore_pb2.StoreRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            values (minknow_api.keystore_pb2.StoreRequest.ValuesEntry): The values to store.

                See the notes in the KeyStore service documentation about names - in short, for any values
                not documented elsewhere, you should be prefixing the name with "<product>:", where <product>
                is the name of your software product.
            lifetime (minknow_api.keystore_pb2.Lifetime, optional): Specify the lifetime of a value.

                When storing values in the manager, the only valid values are `UNTIL_INSTANCE_END` and
                `PERSIST_ACROSS_RESTARTS`.  Using any other value will cause the call to fail with
                `INVALID_ARGUMENT`

                Note that calling remove() will remove the value regardless of this setting.

        Returns:
            minknow_api.keystore_pb2.StoreResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.store,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = minknow_api.keystore_pb2.StoreRequest()

        if "values" in kwargs:
            unused_args.remove("values")
            for key, value in kwargs['values'].items():
                if value.DESCRIPTOR.full_name == 'google.protobuf.Any':
                    _message.values[key].CopyFrom(value)
                else:
                    _message.values[key].Pack(value)
        else:
            raise ArgumentError("store requires a 'values' argument")

        if "lifetime" in kwargs:
            unused_args.remove("lifetime")
            _message.lifetime = kwargs['lifetime']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to store: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.store,
                              _message, _timeout,
                              [],
                              "minknow_api.keystore.KeyStoreService")
    def remove(self, _message=None, _timeout=None, **kwargs):
        """Remove a value from the store.

        

        Args:
            _message (minknow_api.keystore_pb2.RemoveRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            names (str): The names of the values you wish to remove.
            allow_missing (bool, optional): Whether to allow missing values.

                If set, names that are not present in the store will be ignored, but any present values will
                still be removed. Otherwise, missing values will cause an error to be returned (in which case
                nothing will be removed).

                Defaults to 'false'

        Returns:
            minknow_api.keystore_pb2.RemoveResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.remove,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = minknow_api.keystore_pb2.RemoveRequest()

        if "names" in kwargs:
            unused_args.remove("names")
            _message.names.extend(kwargs['names'])
        else:
            raise ArgumentError("remove requires a 'names' argument")

        if "allow_missing" in kwargs:
            unused_args.remove("allow_missing")
            _message.allow_missing = kwargs['allow_missing']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to remove: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.remove,
                              _message, _timeout,
                              [],
                              "minknow_api.keystore.KeyStoreService")
    def get_one(self, _message=None, _timeout=None, **kwargs):
        """Get a single value.

        This is a convenient alternative to get() when you only want a single value. If you want
        multiple values, it is more efficient to request them all in a single get() call.

        If the requested value is not in the store, this will return an error.

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.keystore_pb2.GetOneRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            name (str): The name of the value to fetch.

        Returns:
            minknow_api.keystore_pb2.GetOneResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_one,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = minknow_api.keystore_pb2.GetOneRequest()

        if "name" in kwargs:
            unused_args.remove("name")
            _message.name = kwargs['name']
        else:
            raise ArgumentError("get_one requires a 'name' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_one: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_one,
                              _message, _timeout,
                              [],
                              "minknow_api.keystore.KeyStoreService")
    def get(self, _message=None, _timeout=None, **kwargs):
        """Get any number of values.

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.keystore_pb2.GetRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            names (str, optional): The names of the values you wish to fetch.
            allow_missing (bool, optional): Whether to allow missing values.

                If set, names that are not present in the store will simply be omitted from the response.
                Otherwise, missing values will cause an error to be returned.

                Defaults to 'false'

        Returns:
            minknow_api.keystore_pb2.GetResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = minknow_api.keystore_pb2.GetRequest()

        if "names" in kwargs:
            unused_args.remove("names")
            _message.names.extend(kwargs['names'])

        if "allow_missing" in kwargs:
            unused_args.remove("allow_missing")
            _message.allow_missing = kwargs['allow_missing']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get,
                              _message, _timeout,
                              [],
                              "minknow_api.keystore.KeyStoreService")
    def watch(self, _message=None, _timeout=None, **kwargs):
        """Watch for values being updates.

        On calling this, you will get a message containing the current values, and then messages with
        updates as and when store() is called. The updates will only contain those values that
        changed.

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.keystore_pb2.WatchRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
                Note that this is the time until the call ends, not the time between returned
                messages.
            names (str): The names of the values you wish to watch.
            allow_missing (bool, optional): Whether to allow missing values.

                If set, names that are not present in the store will be omitted from the first response, but
                will still be watched. If and when they are added, a message will be sent with the set
                values. Otherwise, missing values will cause an immediate error.

                Defaults to 'false'

        Returns:
            iter of minknow_api.keystore_pb2.WatchResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.watch,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = minknow_api.keystore_pb2.WatchRequest()

        if "names" in kwargs:
            unused_args.remove("names")
            _message.names.extend(kwargs['names'])
        else:
            raise ArgumentError("watch requires a 'names' argument")

        if "allow_missing" in kwargs:
            unused_args.remove("allow_missing")
            _message.allow_missing = kwargs['allow_missing']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to watch: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.watch,
                              _message, _timeout,
                              [],
                              "minknow_api.keystore.KeyStoreService")
