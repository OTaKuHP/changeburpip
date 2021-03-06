# -*- coding: utf-8 -*-

__author__ = 'Ae0lu5'

# !/usr/bin/env python
# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import random
from burp import ITab
from javax.swing import JMenu
from javax.swing import JMenuItem
from burp import IBurpExtender
from burp import IHttpListener
from java.io import PrintWriter
from burp import IContextMenuFactory
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
from java.awt import GridBagLayout, GridBagConstraints
from javax.swing import JLabel, JTextField, JOptionPane, JTabbedPane, JPanel, JButton


class BurpExtender(IBurpExtender, IHttpListener, IContextMenuFactory, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):

        print "[+] #####################################"
        print "[+]    fakeIp for burp V1.0"
        print "[+]    anthor: Ae0lu5"
        print "[+]    email: administrator@aeolus.ccaeo.com"
        print "[+]    gayhub:https://github.com/AeolusTF"
        print "[+] #####################################"

        print "\n[-]fakeIp loading..."

        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("fakeIp")
        callbacks.registerHttpListener(self)
        callbacks.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callbacks.getStdout(), True)
        self.stderr = PrintWriter(callbacks.getStderr(), True)
        callbacks.issueAlert("Loaded Successfull.")

        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()

        # # set our extension name
        # callbacks.setExtensionName("Custom intruder payloads")

        # register ourselves as an Intruder payload generator
        callbacks.registerIntruderPayloadGeneratorFactory(self)

        print "[*]Successfull..."

    def createMenuItems(self, invocation):
        self.menus = []
        self.mainMenu = JMenu("fakeIp")
        self.menus.append(self.mainMenu)
        self.invocation = invocation
        # print invocation.getSelectedMessages()[0].getRequest()
        menuItem = ['inputIP', '127.0.0.1', 'randomIP']
        for tool in menuItem:
            # self.mainMenu.add(JMenuItem(tool))
            if tool == 'inputIP':
                menu = JMenuItem(tool, None, actionPerformed=lambda x: self.modifyHeader(x))
                self.mainMenu.add(menu)
            elif tool == '127.0.0.1':
                menu = JMenuItem(tool, None, actionPerformed=lambda x: self.modifyHeader(x))
                self.mainMenu.add(menu)
            elif tool == 'randomIP':
                menu = JMenuItem(tool, None, actionPerformed=lambda x: self.modifyHeader(x))
                self.mainMenu.add(menu)

        return self.menus if self.menus else None

    def modifyHeader(self, x):
        if x.getSource().text == 'inputIP':  # ??????????????????????????????????????? text ???????????????????????????????????? command
            currentRequest = self.invocation.getSelectedMessages()[0]  # getSelectedMessages()???????????????????????????1????????????2???
            requestInfo = self._helpers.analyzeRequest(currentRequest)  # ???????????????????????????????????????Http?????????
            self.headers = list(requestInfo.getHeaders())
            # self.headers.append(u'X-Forwarded-For:127.0.0.1')
            # self.headers.append(u'X-Client-IP:127.0.0.1')

            # JOptionPane.showMessageDialog(None, "Command line configured!")

            ip = JOptionPane.showInputDialog("Pls input ur ip:");

            self.headers.append(u'X-Forwarded-For:' + ip)
            self.headers.append(u'X-Forwarded-Host:' + ip)
            self.headers.append(u'X-Client-IP:' + ip)
            self.headers.append(u'X-remote-IP:' + ip)
            self.headers.append(u'X-remote-addr:' + ip)
            self.headers.append(u'True-Client-IP:' + ip)
            self.headers.append(u'X-Client-IP:' + ip)
            self.headers.append(u'Client-IP:' + ip)
            self.headers.append(u'X-Real-IP:' + ip)
            # print 'self.headers',self.headers
            bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():]  # bytes[]??????
            self.body = self._helpers.bytesToString(bodyBytes)  # bytes to string????????????
            # print 'self.body:',self.body
            newMessage = self._helpers.buildHttpMessage(self.headers, self.body)
            currentRequest.setRequest(newMessage)  # setRequest() ???????????????setRequest\


        elif x.getSource().text == '127.0.0.1':
            currentRequest = self.invocation.getSelectedMessages()[0]  # getSelectedMessages()???????????????????????????1????????????2???
            requestInfo = self._helpers.analyzeRequest(currentRequest)  # ???????????????????????????????????????Http?????????
            self.headers = list(requestInfo.getHeaders())
            # self.headers.append(u'X-Forwarded-For:127.0.0.1')
            # self.headers.append(u'X-Client-IP:127.0.0.1')

            ip = '127.0.0.1'
            self.headers.append(u'X-Forwarded-For:' + ip)
            self.headers.append(u'X-Forwarded-Host:' + ip)
            self.headers.append(u'X-Client-IP:' + ip)
            self.headers.append(u'X-remote-IP:' + ip)
            self.headers.append(u'X-remote-addr:' + ip)
            self.headers.append(u'True-Client-IP:' + ip)
            self.headers.append(u'X-Client-IP:' + ip)
            self.headers.append(u'Client-IP:' + ip)
            self.headers.append(u'X-Real-IP:' + ip)
            # print 'self.headers',self.headers
            bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():]  # bytes[]??????
            self.body = self._helpers.bytesToString(bodyBytes)  # bytes to string????????????
            # print 'self.body:',self.body
            newMessage = self._helpers.buildHttpMessage(self.headers, self.body)
            currentRequest.setRequest(newMessage)  # setRequest() ???????????????setRequest\

        elif x.getSource().text == 'randomIP':
            currentRequest = self.invocation.getSelectedMessages()[0]  # getSelectedMessages()???????????????????????????1????????????2???
            requestInfo = self._helpers.analyzeRequest(currentRequest)  # ???????????????????????????????????????Http?????????
            self.headers = list(requestInfo.getHeaders())
            # self.headers.append(u'X-Forwarded-For:127.0.0.1')
            # self.headers.append(u'X-Client-IP:127.0.0.1')

            a = str(int(random.uniform(1, 255)))
            b = str(int(random.uniform(1, 255)))
            c = str(int(random.uniform(1, 255)))
            d = str(int(random.uniform(1, 255)))
            ip = a + "." + b + "." + c + "." + d
            self.headers.append(u'X-Forwarded-For:' + ip)
            self.headers.append(u'X-Forwarded-Host:' + ip)
            self.headers.append(u'X-Client-IP:' + ip)
            self.headers.append(u'X-remote-IP:' + ip)
            self.headers.append(u'X-remote-addr:' + ip)
            self.headers.append(u'True-Client-IP:' + ip)
            self.headers.append(u'X-Client-IP:' + ip)
            self.headers.append(u'Client-IP:' + ip)
            self.headers.append(u'X-Real-IP:' + ip)

            # print 'self.headers',self.headers
            bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():]  # bytes[]??????
            self.body = self._helpers.bytesToString(bodyBytes)  # bytes to string????????????
            # print 'self.body:',self.body
            newMessage = self._helpers.buildHttpMessage(self.headers, self.body)
            currentRequest.setRequest(newMessage)  # setRequest() ???????????????setRequest\

    def getGeneratorName(self):
        return "fakeIpPayloads"

    def createNewInstance(self, attack):
        return fakeIpGenerator(self, attack)


# ??????fakeIpGenerator???????????????IIntruderPayloadGenerator???
# ?????????max_payload(?????????payload), num_iterations(????????????)????????????????????????????????????????????????
class fakeIpGenerator(IIntruderPayloadGenerator):
    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payload = 1
        self.num_iterations = 0
        return

    # ??????????????????????????????????????????
    def hasMorePayloads(self):
        if self.num_iterations == self.max_payload:
            return False
        else:
            return True

    # ???????????????HTTP?????????current_payload????????????????????????????????????????????????????????????mutate_payload
    def getNextPayload(self, current_payload):
        a = str(int(random.uniform(1, 255)))
        b = str(int(random.uniform(1, 255)))
        c = str(int(random.uniform(1, 255)))
        d = str(int(random.uniform(1, 255)))

        payload = a + "." + b + "." + c + "." + d

        return payload






