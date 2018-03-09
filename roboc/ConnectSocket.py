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
    >>> c0 = ConnectSocket(False)
    Server is running, listening on port 5555

    >>> c0.list_sockets(False)

    >>> c0.list_sockets()
    0: (localhost-5555)

    >>> c0.count_clients()
    0

    >>> c0.close()
    Server stop

    >>> c0.list_sockets()

    """
    # default connection parameters
    _HOST = 'localhost'
    _PORT = 5555
    _BUFFER = 1024

    # Template messages
    _BROADCAST_MSG = "{}~ {}\n"
    _MSG_DISCONNECTED = "<gone away to infinity, and beyond>"
    _MSG_SALUTE = "Hi, {}, wait for other players\n"
    _MSG_SERVER_STOP = "Server stop"
    _MSG_START_SERVER = "Server is running, listening on port {}"
    _MSG_USER_IN = "<entered the network>"
    _MSG_WELCOME = "Welcome. First do something usefull and type your name: "
    _SERVER_LOG = "{}:{}|{name}|{msg}"

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

        # Init connection list
        self._inputs = []
        self._inputs.append(self._CONNECTION)

        # Init username list
        self._user_name = []
        self._user_name.append("CONNECTION")

        # Print server's activity on console
        print(self._MSG_START_SERVER.format(port))

    def broadcast(self, sender, name, message):
        """
        Send a message to all clients but the sender

        :param obj sender: socket_object of tne sender
        :param str name: name of tne sender
        :param str message: message to send
        """
        message = self._BROADCAST_MSG.format(name, message)
        for sckt in self._inputs:
            if sckt != self._CONNECTION and sckt != sender:
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
        connect = 1  # the 1st entry is the main connection
        unnamed = self._user_name.count(False)  # unnamed clients
        total = len(self._user_name)  # All sockets
        return total - unnamed - connect

    def list_sockets(self, print_it=True):
        """ List connected sckts """
        if print_it:
            for idx, sckt in enumerate(self._inputs):
                if idx == 0:
                    print("{}: ({}-{})".format(
                        idx, self._HOST, self._PORT)
                         )
                else:
                    print("{}: {}".format(idx, sckt))
        else:
            return self._inputs

    def listen(self):
        """
        Listen sockets activity

        Get the list of sockets which are ready to be read and apply:
        - connect a new client
        - return data sended by client

        :return str, str: user_name, data
        """
        rlist, [], [] = select.select(self._inputs, [], [], 0.05)

        for sckt in rlist:
            # Listen for new client connection
            if sckt == self._CONNECTION:
                sckt_object, sckt_addr = sckt.accept()
                self._inputs.append(sckt_object)
                self._user_name.append(False)
                print(self._SERVER_LOG.format(
                    *sckt_addr,
                    name="unknow",
                    msg="connected")
                     )
                sckt_object.send(self._MSG_WELCOME.encode())

            else:  # receiving data
                data = sckt.recv(self._BUFFER).decode().strip()
                peername = sckt.getpeername()
                s_idx = self._inputs.index(sckt)
                uname = self._user_name[s_idx]

                if self._user_name[s_idx] is False:  # setting username
                    # insert username naming rule here
                    # verify if name is already used TODO17
                    self._user_name[s_idx] = data
                    sckt.send(self._MSG_SALUTE.format(
                        self._user_name[s_idx]).encode()
                             )
                    print(self._SERVER_LOG.format(
                        *peername,
                        name=data,
                        msg="set user name")
                         )
                    self.broadcast(
                        sckt, self._user_name[s_idx], self._MSG_USER_IN
                                  )

                elif data.upper() == "QUIT":  # client quit network
                    print(self._SERVER_LOG.format(
                        *peername,
                        name=uname,
                        msg="disconnected")
                         )
                    self.broadcast(sckt, uname, self._MSG_DISCONNECTED)
                    self._inputs.remove(sckt)
                    self._user_name.pop(s_idx)
                    sckt.close()

                elif data:
                    print(self._SERVER_LOG.format(
                        *peername, name=uname, msg=data)
                         )
                    return uname, data

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
