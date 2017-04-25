"""Vidalyser.

Author: Robert Walker <rrah99@gmail.com>

    This file is part of Vidalyser.
    
    Vidalyser is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Vidalyser is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Vidalyser.  If not, see <http://www.gnu.org/licenses/>.
"""

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