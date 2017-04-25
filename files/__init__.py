"""Deals with loading and saving for vidalysers

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

import logging
import json

logger = logging.getLogger(__name__)

def load_file(filename, main_window):
    
    """Open the specified file and launch the required launch bars."""
    
    with open(filename) as input_file:
        config = json.load(input_file)
        
    for stream in config["streams"]:
        main_window.add_stream(stream["url"], stream["loc_ip"])
        
    logger.info("Loaded from {}.".format(filename))
        
def save_file(filename, main_window):
    
    """Save the current launch bars to a file for future use."""
    
    config = {"streams": []}
    
    for launch_bar in main_window.launch_bars():
        
        config["streams"].append(launch_bar.save_dict())
        
    with open(filename, "w") as output_file:
        json.dump(config, output_file)
        
    logger.info("Saved to {}.".format(filename))