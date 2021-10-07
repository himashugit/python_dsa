#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from builtins import str
from builtins import range
from builtins import object
import sys

import os
from optparse import OptionParser
from lib import configs
import json
from lib import file_tools
import generate_password
from lib import configFile
from lib import PALogging
from lib import key_protect_cluster

logger = PALogging.getLogging(__name__)

#--------------------------------------------------------------------------------
class AddModeler(object):
    '''This script can be used to add an N number of Modelers to the environment'''
    def addModelersToEnv(self, confFilePath, detailsFilePath, modelersToAdd, envName):
        cfgFile = configFile.configFile(confFilePath)
        config = cfgFile.configJson
        if(config == None):
            raise Exception("Configuration was blank when loaded from " + confFilePath)
        generator = generate_password.GeneratePassword()

        #This assumes the modeler Ids are contiguous rather than looking for the one with the highest number
        modelerCount = 0
        for host in config['hosts']:
            for user in host['users']:
                if 'Modeler' in user['roles']:
                   modelerCount += 1

        for i in range(0, modelersToAdd):
            modelerName = "modeler"  + str(modelerCount + 1)
            newModeler = {"password": generator.do(14),
                    "roles": [
                        "Modeler"
                    ],
                    "userName": modelerName}
            
            for host in config['hosts']:
                if 'rich' in host["roles"]:
                    host['users'].insert(modelerCount, newModeler)
                    logger.info("%s: Added %s" %(host['fullyQualifiedDomainName'] , modelerName))
            modelerCount += 1
        key_protect_cluster.KPWritePrettyJSON(config, confFilePath, detailsFilePath)

#--------------------------------------------------------------------------------
def main():
        
        configFilePath = 'config.json'
        defaultDetailsFilePath = 'details.txt'
        parser = OptionParser()
        parser.add_option("-e", "--environment-name-regex",
            dest="environmentNameRegex", default=None, help=
             "Environment name regular expression [default: None, use file name]")

        parser.add_option("", "--details-file-path", dest="detailsFilePath", default=defaultDetailsFilePath, help="Details file path [default: " + defaultDetailsFilePath + "]")
        parser.add_option("-f", "--full-file-path", dest="filePath", default=None, help=
                          "If the full file path is to be used INSTEAD of the environment name")
                          
        parser.add_option("-n", "--numberToAdd", type="int", dest="num", default=1,
                              help="Add this many Modelers. [default: 1]", metavar="INT")
        (options, dummy) = parser.parse_args()

        modelerAdder = AddModeler()

        options.detailsFilePath = os.path.abspath(options.detailsFilePath)
        if not os.path.exists(options.detailsFilePath):
            raise Exception("Unable to locate details file: %s" %options.detailsFilePath)

        if options.environmentNameRegex:
            for dummy, configFilePath in configs.configsForEnvironmentRegEx(options.environmentNameRegex):
                logger.debug("\nEnvironment name: %s \n"% options.environmentNameRegex )
                modelerAdder.addModelersToEnv(configFilePath, options.detailsFilePath, options.num, options.environmentNameRegex)
        else:
                modelerAdder.addModelersToEnv(options.filePath, options.detailsFilePath, options.num, options.filePath)

        logger.info("1-Check-in (and deliver) changes to GitHub ")
        logger.info("2-Run setup_modeler_accounts.ps1")
        logger.info("3-Update and deliver Welcome kit to customer")
    

        
#----------------------------------------
if __name__ == "__main__":
        main()