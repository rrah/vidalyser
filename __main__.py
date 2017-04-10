'''
Created on 6 Apr 2017

@author: redsw
'''

import gui

import logging


if __name__ == '__main__':
    
    logging.basicConfig(filename = "vidalyser.log",
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M', level = logging.DEBUG)
    
    stderr_handler = logging.StreamHandler()
    stderr_handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(stderr_handler)
    
    logger = logging.getLogger(__name__)
    
    logger.info("Starting up Vidalyser...")
    root = gui.Main_Window()

    root.mainloop()
    
    logger.info("Exiting Vidalyser.")