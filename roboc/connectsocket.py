#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part or roboc project. View `readme.md`
"""
import socket
import select


class ConnectSocket:
    """
    ConnectSocket
    =======

    Provide network connection and management methods

    :Example:
    >>> c0 = ConnectSocket()
    Server is running, listening on port 5555

    >>> c0.list_sockets(False, False)
    []

    >>> c0.list_sockets()
    ''

    >>> c0.count_clients()
    0

    >>> c0.close()
    Server stop
    """
    # default connection parameters
    _HOST = 'localhost'
    _PORT = 5555
    _BUFFER = 1024
    _MAIN_CONNECT = "MAIN_CONNECT"

    # Template messages
    _BROADCAST_MSG = "{}~ {}\n"
    _MSG_DISCONNECTED = "<gone away to infinity, and beyond>"
    _MSG_SALUTE = "Hi, {}, wait for other players\n"
    _MSG_SERVER_STOP = "Server stop"
    _MSG_START_SERVER = "Server is running, listening on port {}"
    _MSG_USER_IN = "<entered the network>"
    _MSG_WELCOME = "Welcome. First do something usefull and type your name: "
    _MSG_UNWELCOME = "Sorry, no more place here.\n"
    _SERVER_LOG = "{}:{}|{name}|{msg}"

    # Others const
    _MAX_CLIENT_NAME_LEN = 8
    _MAX_CLIENT_NB = 5

    def __init__(self, host=_HOST, port=_PORT):
        """
        Set up the server connection using a socket object

        :param str _HOST: domain or IPV4 address
        :param int _PORT: port number
        :return obj: socket
        """

        # Setting up the connection
        self._CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._CONNECTION.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._CONNECTION.bind((host, port))
        self._CONNECTION.listen(5)

        # Init connection list
        self._inputs = []
        self._inputs.append(self._CONNECTION)

        # Init username list, to keep match between inputs & name lists
        self._user_name = []
        self._user_name.append(self._MAIN_CONNECT)

        # Print server's activity on console
        print(self._MSG_START_SERVER.format(port))

    def broadcast(self, sender, message):
        """
        Send a message to all named-clients but the sender

        TODO should replace sckt.send() too

        :param obj sender: sender socket (or 'server' str() for server)
        :param str message: message to send
        """
        # Define senders name
        if sender == 'server':
            name = 'server'.upper()
        else:
            idx = self._inputs.index(sender)
            name = self._user_name[idx].upper()

        message = self._BROADCAST_MSG.format(name, message)
        recipients = self.list_sockets(False, False)

        for sckt in recipients:
            if sckt != sender:
                try:
                    sckt.send(message.encode())
                except:
                    sckt.close()
                    self._inputs.remove(sckt)

    def close(self):
        """ Cleanly closes each socket (clients) of the network """
        self._CONNECTION = self._inputs.pop(0)
        i = 1
        for sckt in self._inputs:
            print(self._SERVER_LOG.format(
                *sckt.getpeername(),
                name=self._user_name[i],
                msg="closed client sckt")
                 )
            sckt.close()
            i += 1
        self._inputs.clear()
        self._CONNECTION.close()
        print(self._MSG_SERVER_STOP)

    def count_clients(self):
        """
        Count connected and named clients

        (to avoid playing with a unamed player)
        """
        return len(self.list_sockets(False, False))

    def list_sockets(self, print_string=True, user_name=True):
        """
        List connected sockets

        :param bool print_string: return txt formated socket list
        :param bool user_name: return user_name
        """
        if user_name:
            client_list = [
                name for name in self._user_name
                if name != self._MAIN_CONNECT and name is not False
            ]
        else:
            client_list = [
                sckt for (idx, sckt) in enumerate(self._inputs)
                if sckt != self._CONNECTION
                and self._user_name[idx] is not False
            ]

        # FIXME maybe there is a better way for the next condition: when
        # client connects it has not yet his name filled in the
        # _user_name attribut, then this method returns only clients
        # with a filled name
        if print_string and len(client_list) == 0:
            client_list = ""
        elif print_string:
            client_list = ", ".join(client_list)

        return client_list

    def listen(self):
        """
        Listen sockets activity

        Get the list of sockets which are ready to be read and apply:
        - connect a new client
        - return data sended by client

        This object only processes data specific to network connections,
        other data (username and message sent) are stored in `u_name` &
        `message` attributes to be used by parent script

        :return str, str: user_name, data
        """
        self.u_name = ""
        self.message = ""

        # listennig…
        rlist, [], [] = select.select(self._inputs, [], [], 0.05)
        for sckt in rlist:
            # Listen for new client connection
            if sckt == self._CONNECTION:
                if len(self._inputs) <= self._MAX_CLIENT_NB:
                    sckt_object, sckt_addr = sckt.accept()
                    sckt_object.send(self._MSG_WELCOME.encode())

                    self._inputs.append(sckt_object)
                    self._user_name.append(False)

                    print(self._SERVER_LOG.format(
                        *sckt_addr,
                        name="unknow",
                        msg="connected")
                         )

                else:
                    sckt_object, sckt_addr = sckt.accept()
                    sckt_object.send(self._MSG_UNWELCOME.encode())
                    print(self._SERVER_LOG.format(
                        *sckt_addr,
                        name="unknow",
                        msg="rejected")
                         )
                    sckt_object.close()
                    break

            else:  # receiving data
                data = sckt.recv(self._BUFFER).decode().strip()
                peername = sckt.getpeername()
                s_idx = self._inputs.index(sckt)
                uname = self._user_name[s_idx]

                if self._user_name[s_idx] is False:  # setting username
                    # insert username naming rule here
                    data = data[0:self._MAX_CLIENT_NAME_LEN]
                    # name is already used
                    if data in self._user_name:
                        data += str(s_idx)

                    self._user_name[s_idx] = data
                    sckt.send(self._MSG_SALUTE.format(
                        self._user_name[s_idx]).encode()
                             )
                    print(self._SERVER_LOG.format(
                        *peername,
                        name=data,
                        msg="set user name")
                         )
                    self.broadcast(sckt, self._MSG_USER_IN)

                elif data.upper() == "QUIT":  # client quit network
                    print(self._SERVER_LOG.format(
                        *peername,
                        name=uname,
                        msg="disconnected")
                         )
                    self.broadcast(sckt, self._MSG_DISCONNECTED)
                    self._inputs.remove(sckt)
                    self._user_name.pop(s_idx)
                    sckt.close()

                elif data:
                    print(self._SERVER_LOG.format(
                        *peername, name=uname, msg=data)
                         )
                    self.u_name, self.message = uname, data

                else:
                    msg = "uncommon transmission:«{}»".format(data)
                    print(self._SERVER_LOG.format(
                        *peername, name=uname, msg=msg)
                         )
                    sckt.send(("server do not transmit: {}\n".format(
                        msg
                    )).encode())


if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
